"""
Serviço de templates de design pré-construídos.

Fluxo:
  1. get_template_html(slug) → lê o arquivo HTML do template + inlina styles.css
  2. apply_content(html, content, color_overrides, image_url) → preenche conteúdo real
  3. search_pexels_image(query) → busca imagem relevante no Pexels e retorna URL
"""

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Mesma chave usada no frontend (lib/pexels.ts)
_PEXELS_API_KEY = "26CU1rMkQHVmTL9pWDeHgyWuaM2kRt5JbGqiyWtsNjTPSo0IfOBsjxL3"

# Caminho base dos templates (relativo a este arquivo: backend/services/ → raiz do repo)
_BASE = Path(__file__).parent.parent.parent / "Repositório de templates de design"
_STYLES_PATH = _BASE / "styles.css"


def _read_styles() -> str:
    try:
        return _STYLES_PATH.read_text(encoding="utf-8")
    except Exception:
        return ""


_STYLES_CSS: str = _read_styles()


def get_template_html(slug: str) -> str:
    """
    Lê o arquivo HTML do template e substitui o <link> externo por um <style> inline,
    tornando o HTML autossuficiente para uso em iframe ou exportação.

    Args:
        slug: Caminho relativo sem extensão, ex: "apresentacoes/ia-apresentacao-aurora-hero-split"

    Returns:
        HTML completo com CSS inline.

    Raises:
        FileNotFoundError: Se o slug não corresponder a nenhum arquivo.
    """
    filepath = _BASE / (slug + ".html")
    if not filepath.exists():
        raise FileNotFoundError(f"Template não encontrado: '{slug}'. Verifique o catálogo.")

    html = filepath.read_text(encoding="utf-8")

    # Substitui a referência externa ao styles.css por um bloco <style> inline
    html = html.replace(
        "<link rel='stylesheet' href='../styles.css'/>",
        f"<style>{_STYLES_CSS}</style>",
    )

    return html


def apply_content(
    html: str,
    content: dict,
    color_overrides: dict | None = None,
    image_url: str | None = None,
) -> str:
    """
    Aplica conteúdo real ao template HTML.

    Args:
        html: HTML do template (já com CSS inline).
        content: Dicionário com campos semânticos:
            - title       → substitui conteúdo do <h1>
            - eyebrow     → substitui conteúdo do <p class='eyebrow'>
            - subtitle    → substitui conteúdo do <p class='lede'>
            - footer      → substitui conteúdo do <p class='footer'>
            - heading     → substitui conteúdo do <h2>
            - extra_patches → lista de {"find": "...", "replace": "..."} para textos adicionais
        color_overrides: Dicionário de variáveis CSS ex: {"--accent": "#e63946"}
        image_url: URL de imagem para substituir os placeholders SVG data-URI.

    Returns:
        HTML com conteúdo aplicado.
    """
    # Substitui <h1>
    if content.get("title"):
        title = _escape_replacement(content["title"])
        html = re.sub(
            r'(<h1[^>]*>).*?(</h1>)',
            rf'\g<1>{title}\g<2>',
            html,
            flags=re.DOTALL,
        )

    # Substitui .eyebrow
    if content.get("eyebrow"):
        eyebrow = _escape_replacement(content["eyebrow"])
        html = re.sub(
            r"(<p class='eyebrow'>)[^<]*(</p>)",
            rf'\g<1>{eyebrow}\g<2>',
            html,
        )

    # Substitui .lede (subtítulo/descrição)
    if content.get("subtitle"):
        subtitle = _escape_replacement(content["subtitle"])
        html = re.sub(
            r"(<p class='lede'>)[^<]*(</p>)",
            rf'\g<1>{subtitle}\g<2>',
            html,
        )

    # Substitui .footer
    if content.get("footer"):
        footer = _escape_replacement(content["footer"])
        html = re.sub(
            r"(<p class='footer'>)[^<]*(</p>)",
            rf'\g<1>{footer}\g<2>',
            html,
        )

    # Substitui <h2>
    if content.get("heading"):
        heading = _escape_replacement(content["heading"])
        html = re.sub(
            r'(<h2[^>]*>).*?(</h2>)',
            rf'\g<1>{heading}\g<2>',
            html,
            flags=re.DOTALL,
        )

    # Patches adicionais (find/replace literal)
    for patch in content.get("extra_patches", []):
        find = patch.get("find", "")
        replace = patch.get("replace", "")
        if find:
            html = html.replace(find, replace)

    # Substitui imagem placeholder (SVG data-URI → URL real)
    if image_url:
        html = re.sub(r"src='data:image/svg\+xml;[^']*'", f"src='{image_url}'", html)
        html = re.sub(r'src="data:image/svg\+xml;[^"]*"', f'src="{image_url}"', html)

    # Injeta overrides de cor como variáveis CSS no <head>
    if color_overrides:
        css_vars = ";".join(f"{k}:{v}" for k, v in color_overrides.items())
        style_override = f"<style>.canvas{{{css_vars}}}</style>"
        html = html.replace("</head>", f"{style_override}</head>", 1)

    return html


def _escape_replacement(text: str) -> str:
    """Escapa barras invertidas e referências de grupo para uso em re.sub replacement."""
    return text.replace("\\", "\\\\")


async def search_pexels_image(
    query: str,
    orientation: str = "landscape",
) -> str:
    """
    Busca uma imagem relevante no Pexels e retorna a URL direta (large ~940px).
    Retorna string vazia se a busca falhar ou não encontrar resultado.

    Args:
        query: Termos de busca em inglês para melhores resultados. Ex: "wedding flowers elegant"
        orientation: "landscape" | "portrait" | "square"
    """
    import httpx

    try:
        params = {"query": query, "per_page": 1, "orientation": orientation}
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get(
                "https://api.pexels.com/v1/search",
                params=params,
                headers={"Authorization": _PEXELS_API_KEY},
            )
        if resp.status_code != 200:
            logger.warning(f"[Pexels] HTTP {resp.status_code} para query '{query}'")
            return ""
        data = resp.json()
        photos = data.get("photos", [])
        if not photos:
            logger.warning(f"[Pexels] Nenhuma foto encontrada para '{query}'")
            return ""
        return photos[0]["src"]["large"]
    except Exception as e:
        logger.warning(f"[Pexels] Erro na busca '{query}': {e}")
        return ""
