from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent

CSS = """
:root{--bg:#f6f1e8;--paper:rgba(255,255,255,.78);--ink:#161311;--muted:#6c655e;--line:rgba(22,19,17,.12);--accent:#d95d39;--accent-2:#145b7d;--accent-3:#f2b134;--glow:0 30px 90px rgba(18,16,14,.16)}
*{box-sizing:border-box}html,body{margin:0;min-height:100%}body{font-family:'Trebuchet MS','Segoe UI',sans-serif;background:var(--bg);color:var(--ink)}
.page{min-height:100vh;padding:22px;background:radial-gradient(circle at 0% 0%,rgba(255,255,255,.55),transparent 28%),radial-gradient(circle at 100% 100%,rgba(255,255,255,.35),transparent 32%),var(--bg)}
.canvas{position:relative;width:min(100%,var(--w));aspect-ratio:var(--ratio);min-height:620px;margin:0 auto;border-radius:34px;overflow:hidden;box-shadow:var(--glow);background:linear-gradient(180deg,rgba(255,255,255,.45),rgba(255,255,255,.1)),var(--bg2,var(--bg))}
.canvas.dark{--paper:rgba(12,16,24,.66);--ink:#f5efe8;--muted:rgba(245,239,232,.76);--line:rgba(245,239,232,.12);--glow:0 30px 90px rgba(0,0,0,.38)}
.canvas::before,.canvas::after{content:'';position:absolute;pointer-events:none}
.inner{position:relative;z-index:2;width:100%;height:100%;padding:54px 58px}
.stack{display:grid;gap:18px}.row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}.between{display:flex;justify-content:space-between;gap:20px;align-items:flex-start}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
h1,h2,h3,p{margin:0}h1{font-size:clamp(38px,4vw,82px);line-height:.94;letter-spacing:-.05em}h2{font-size:clamp(28px,3vw,56px);line-height:1;letter-spacing:-.035em}h3{font-size:20px;line-height:1.1}p,li{font-size:18px;line-height:1.5;color:var(--muted)}
.lede{font-size:22px;max-width:58ch}.eyebrow{font-size:13px;text-transform:uppercase;letter-spacing:.2em;font-weight:800;color:var(--accent-2)}
.badge{display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:999px;border:1px solid var(--line);background:rgba(255,255,255,.32);backdrop-filter:blur(12px);font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.08em}
.card{border:1px solid var(--line);border-radius:26px;padding:22px;background:var(--paper);backdrop-filter:blur(16px)}
.metric{padding:20px;border-radius:22px;border:1px solid var(--line);background:var(--paper)}.metric strong{display:block;font-size:34px;line-height:1;margin-bottom:8px}
.slot{position:relative;overflow:hidden;border-radius:28px;min-height:280px;background:linear-gradient(135deg,color-mix(in srgb,var(--accent) 82%,white),color-mix(in srgb,var(--accent-2) 78%,white));border:1px solid rgba(255,255,255,.18)}
.slot.tall{min-height:100%}.slot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.slot::after{content:attr(data-label);position:absolute;left:18px;bottom:18px;padding:10px 12px;border-radius:14px;background:rgba(255,255,255,.74);border:1px solid rgba(22,19,17,.08);font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.14em;color:#161311}
.dark .slot::after{background:rgba(12,16,24,.72);border-color:rgba(245,239,232,.12);color:#f5efe8}
.outline{border:1px dashed var(--line);border-radius:24px;padding:18px}.number-list{display:grid;gap:14px}.number-item{display:grid;grid-template-columns:52px 1fr;gap:14px}.num{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;background:color-mix(in srgb,var(--accent) 16%,white);font-weight:800}
.footer{position:absolute;left:58px;bottom:28px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.catalog{max-width:1360px;margin:0 auto}.catalog-section{margin-top:24px;padding:24px;border-radius:30px;background:rgba(255,255,255,.5);box-shadow:var(--glow)}.catalog-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}.catalog-card{display:block;text-decoration:none;padding:18px;border-radius:24px;border:1px solid rgba(22,19,17,.08);background:rgba(255,255,255,.72)}.thumb{height:136px;border-radius:18px;margin-top:14px;background:linear-gradient(135deg,color-mix(in srgb,var(--accent) 82%,white),color-mix(in srgb,var(--accent-2) 76%,white))}
.fx-aurora::before{inset:-10% -5% auto auto;width:46%;height:54%;border-radius:999px;background:radial-gradient(circle,rgba(255,255,255,.36),transparent 60%),linear-gradient(140deg,var(--accent),var(--accent-2));filter:blur(8px);opacity:.58}.fx-aurora::after{inset:auto auto -16% -10%;width:38%;height:44%;border-radius:999px;background:linear-gradient(140deg,var(--accent-3),var(--accent));opacity:.3;filter:blur(16px)}
.fx-editorial::before{top:42px;right:48px;width:160px;height:160px;border-radius:999px;background:var(--accent);opacity:.16}.fx-editorial::after{left:42px;bottom:40px;width:240px;height:10px;border-radius:999px;background:var(--accent-2);opacity:.16}
.fx-brutal::before{inset:28px 28px auto auto;width:180px;height:180px;background:var(--accent);border-radius:30px;transform:rotate(12deg);opacity:.18}.fx-brutal::after{left:36px;bottom:36px;width:220px;height:56px;background:var(--accent-2);border-radius:16px;opacity:.14}
.fx-neon::before{inset:18px auto auto 18px;width:46%;height:2px;background:linear-gradient(90deg,var(--accent),transparent)}.fx-neon::after{right:26px;bottom:26px;width:220px;height:220px;border:1px solid rgba(255,255,255,.28);border-radius:999px;box-shadow:0 0 0 12px rgba(255,255,255,.04),0 0 60px color-mix(in srgb,var(--accent) 46%,transparent)}
.fx-luxe::before{inset:24px 24px auto auto;width:180px;height:180px;border:1px solid color-mix(in srgb,var(--accent-3) 42%,transparent);border-radius:999px}.fx-luxe::after{left:24px;bottom:24px;width:260px;height:260px;border:1px solid color-mix(in srgb,var(--accent-3) 22%,transparent);border-radius:30px}
.fx-paper::before{top:-40px;right:-40px;width:320px;height:220px;background:var(--accent);border-radius:44% 56% 34% 66%/38% 40% 60% 62%;opacity:.16}.fx-paper::after{left:-20px;bottom:-30px;width:300px;height:200px;background:var(--accent-2);border-radius:58% 42% 61% 39%/45% 51% 49% 55%;opacity:.12}
.fx-mesh::before{inset:-10% auto auto -10%;width:52%;height:52%;border-radius:999px;background:radial-gradient(circle,var(--accent),transparent 62%);opacity:.35;filter:blur(10px)}.fx-mesh::after{inset:auto -10% -10% auto;width:52%;height:52%;border-radius:999px;background:radial-gradient(circle,var(--accent-2),transparent 62%);opacity:.35;filter:blur(12px)}
.fx-botanical::before{left:28px;top:20px;width:160px;height:280px;border-radius:100px 100px 20px 100px;background:linear-gradient(180deg,color-mix(in srgb,var(--accent-2) 64%,white),transparent);transform:rotate(-18deg);opacity:.18}.fx-botanical::after{right:40px;bottom:20px;width:120px;height:220px;border-radius:100px 100px 100px 20px;background:linear-gradient(180deg,color-mix(in srgb,var(--accent) 64%,white),transparent);transform:rotate(14deg);opacity:.16}
.fx-retro::before{left:-6%;top:-8%;width:44%;height:44%;border-radius:999px;background:var(--accent-3);opacity:.28}.fx-retro::after{right:6%;bottom:10%;width:22%;height:22%;border-radius:999px;background:var(--accent-2);opacity:.18}
.fx-blueprint::before{inset:0;background-image:linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px);background-size:26px 26px;opacity:.5}.fx-blueprint::after{inset:24px;border:1px solid rgba(255,255,255,.14);border-radius:22px}
.fx-cinema::before{inset:auto auto 0 0;width:100%;height:32%;background:linear-gradient(0deg,rgba(0,0,0,.34),transparent)}.fx-cinema::after{top:24px;right:24px;width:120px;height:120px;border-radius:999px;background:radial-gradient(circle,rgba(255,255,255,.44),transparent 62%)}
@media (max-width:980px){.page{padding:12px}.inner{padding:28px}.grid2,.grid3,.grid4{grid-template-columns:1fr}.canvas{min-height:auto}.footer{position:static;margin-top:18px}}
"""

STYLES = {
    "aurora-glass": {"cls": "fx-aurora", "bg": "#eef4ff", "bg2": "#e5eef9", "accent": "#6b5cff", "accent2": "#00a6a6", "accent3": "#ff8a5b"},
    "editorial-sand": {"cls": "fx-editorial", "bg": "#f4eadf", "bg2": "#f8f1e8", "accent": "#c35f3d", "accent2": "#1b5c65", "accent3": "#efbf62"},
    "brutalist-pop": {"cls": "fx-brutal", "bg": "#fff5ec", "bg2": "#fff0da", "accent": "#ff5a36", "accent2": "#111111", "accent3": "#ffd84d"},
    "midnight-neon": {"cls": "fx-neon", "bg": "#0b1020", "bg2": "#11182a", "accent": "#0ff0ff", "accent2": "#7b61ff", "accent3": "#ff4fd8", "dark": True},
    "mono-luxe": {"cls": "fx-luxe", "bg": "#161514", "bg2": "#1d1b19", "accent": "#f0d7a1", "accent2": "#9d8b70", "accent3": "#fff5de", "dark": True},
    "paper-cut": {"cls": "fx-paper", "bg": "#f9f4ee", "bg2": "#f3ece4", "accent": "#e07152", "accent2": "#2d6e73", "accent3": "#f3ba7b"},
    "mesh-gradient": {"cls": "fx-mesh", "bg": "#eef6ff", "bg2": "#f7f3ff", "accent": "#4f75ff", "accent2": "#ff6b8f", "accent3": "#7ce0d3"},
    "botanical-soft": {"cls": "fx-botanical", "bg": "#eef4e8", "bg2": "#f7faf2", "accent": "#798f4a", "accent2": "#2f5d44", "accent3": "#e5b97a"},
    "retro-sun": {"cls": "fx-retro", "bg": "#fff1db", "bg2": "#ffe8cb", "accent": "#ea6c2d", "accent2": "#3559a3", "accent3": "#ffd166"},
    "blueprint-tech": {"cls": "fx-blueprint", "bg": "#0f2741", "bg2": "#173453", "accent": "#7fd3ff", "accent2": "#5ae5c4", "accent3": "#d6f3ff", "dark": True},
    "cinema-red": {"cls": "fx-cinema", "bg": "#201111", "bg2": "#311919", "accent": "#ff6a55", "accent2": "#f7d7b5", "accent3": "#ffffff", "dark": True},
}

ITEMS = {
    "apresentacoes": [
        ("ia-apresentacao-aurora-hero-split", "Apresentacao aurora hero split", "Para abertura de deck com energia, translucidez e imagem lateral.", 1600, 900, "hero-split", "aurora-glass"),
        ("ia-apresentacao-editorial-magazine", "Apresentacao editorial magazine", "Para brand deck sofisticado com hierarquia tipografica e recorte de imagem.", 1600, 900, "magazine", "editorial-sand"),
        ("ia-apresentacao-brutalist-kpi-ribbon", "Apresentacao brutalist KPI ribbon", "Para pitch comercial com blocos fortes, contraste e dados em destaque.", 1600, 900, "kpi-ribbon", "brutalist-pop"),
        ("ia-apresentacao-neon-dashboard", "Apresentacao neon dashboard", "Para startup, SaaS e tecnologia com glow, linhas e cartoes transparentes.", 1600, 900, "dashboard", "midnight-neon"),
        ("ia-apresentacao-luxe-monolith", "Apresentacao luxe monolith", "Para mercado premium, luxo e posicionamento aspiracional.", 1600, 900, "monolith", "mono-luxe"),
        ("ia-apresentacao-paper-overlap", "Apresentacao paper overlap", "Para storytelling criativo com camadas suaves e area principal para imagem.", 1600, 900, "overlap", "paper-cut"),
        ("ia-apresentacao-mesh-diagonal", "Apresentacao mesh diagonal", "Para apresentacoes modernas com cor viva e painel diagonal.", 1600, 900, "diagonal", "mesh-gradient"),
        ("ia-apresentacao-botanical-frame", "Apresentacao botanical frame", "Para wellness, interior, moda organica ou gastronomia natural.", 1600, 900, "frame", "botanical-soft"),
        ("ia-apresentacao-retro-poster", "Apresentacao retro poster", "Para campanhas divertidas, eventos ou portfolio com solidos e circulos.", 1600, 900, "poster", "retro-sun"),
        ("ia-apresentacao-blueprint-roadmap", "Apresentacao blueprint roadmap", "Para planejamento, produto e estrategia com leitura tecnica.", 1600, 900, "roadmap", "blueprint-tech"),
        ("ia-apresentacao-cinema-quote", "Apresentacao cinema quote", "Para manifesto, opening statement ou slide de impacto emocional.", 1600, 900, "quote-stage", "cinema-red"),
        ("ia-apresentacao-aurora-cascade", "Apresentacao aurora cascade", "Para deck inspiracional com cards em cascata e imagem vertical.", 1600, 900, "cascade", "aurora-glass"),
    ],
    "instagram-posts": [
        ("ia-instagram-mesh-product-square", "Instagram mesh product square", "Para feed de produto com imagem grande e CTA limpo.", 1080, 1080, "social-product", "mesh-gradient"),
        ("ia-instagram-retro-sale-burst", "Instagram retro sale burst", "Para promocao vibrante com selo visual e composicao pop.", 1080, 1080, "social-burst", "retro-sun"),
        ("ia-instagram-neon-quote-grid", "Instagram neon quote grid", "Para frase curta com glow e molduras finas.", 1080, 1080, "social-quote", "midnight-neon"),
        ("ia-instagram-botanical-editorial", "Instagram botanical editorial", "Para lifestyle, moda ou beauty com espaco para foto e copy.", 1080, 1080, "social-editorial", "botanical-soft"),
        ("ia-instagram-brutalist-announcement", "Instagram brutalist announcement", "Para anuncio de evento ou lancamento com blocos grandes.", 1080, 1080, "social-block", "brutalist-pop"),
        ("ia-instagram-luxe-monogram", "Instagram luxe monogram", "Para marca premium com minimalismo e atmosfera sofisticada.", 1080, 1080, "social-monogram", "mono-luxe"),
        ("ia-instagram-paper-collage", "Instagram paper collage", "Para conteudo criativo com recortes e area para imagem central.", 1080, 1080, "social-collage", "paper-cut"),
        ("ia-instagram-blueprint-card", "Instagram blueprint card", "Para conteudo educativo, checklist ou teaser tecnico.", 1080, 1080, "social-card", "blueprint-tech"),
    ],
    "cartaz-panfleto": [
        ("ia-cartaz-cinema-premiere", "Cartaz cinema premiere", "Para cartaz impactante com imagem dominante e faixa dramatica.", 900, 1273, "poster-hero", "cinema-red"),
        ("ia-cartaz-retro-festival", "Cartaz retro festival", "Para eventos culturais com elementos circulares e headline forte.", 900, 1273, "poster-burst", "retro-sun"),
        ("ia-cartaz-editorial-gallery", "Cartaz editorial gallery", "Para exposicoes, mostras e eventos refinados.", 900, 1273, "poster-editorial", "editorial-sand"),
        ("ia-cartaz-neon-night", "Cartaz neon night", "Para festas, shows e divulgacao noturna com glow e linhas.", 900, 1273, "poster-grid", "midnight-neon"),
        ("ia-panfleto-botanical-market", "Panfleto botanical market", "Para feiras, cafe, organicos e eventos locais.", 900, 1273, "poster-frame", "botanical-soft"),
        ("ia-panfleto-brutalist-offer", "Panfleto brutalist offer", "Para promocao direta, impacto visual e beneficio claro.", 900, 1273, "poster-stack", "brutalist-pop"),
    ],
    "convites": [
        ("ia-convite-luxe-gala", "Convite luxe gala", "Para jantares, galas e eventos premium com moldura refinada.", 1200, 1800, "invite-ornate", "mono-luxe"),
        ("ia-convite-aurora-wedding", "Convite aurora wedding", "Para eventos delicados com brilho suave e composicao limpa.", 1200, 1800, "invite-soft", "aurora-glass"),
        ("ia-convite-retro-party", "Convite retro party", "Para festa com energia quente, formas organicas e data em destaque.", 1200, 1800, "invite-poster", "retro-sun"),
        ("ia-convite-paper-exhibition", "Convite paper exhibition", "Para inauguracao, mostra ou evento criativo com recortes.", 1200, 1800, "invite-collage", "paper-cut"),
        ("ia-convite-botanical-dinner", "Convite botanical dinner", "Para jantar, degustacao ou encontro intimista.", 1200, 1800, "invite-frame", "botanical-soft"),
        ("ia-convite-blueprint-launch", "Convite blueprint launch", "Para evento corporativo, tech ou networking com ar tecnico.", 1200, 1800, "invite-panel", "blueprint-tech"),
    ],
    "cartoes": [
        ("ia-cartao-editorial-front", "Cartao editorial front", "Para identidade profissional minimalista com area de imagem.", 1050, 600, "card-split", "editorial-sand"),
        ("ia-cartao-neon-identity", "Cartao neon identity", "Para criativos, musica, tecnologia ou moda noturna.", 1050, 600, "card-glow", "midnight-neon"),
        ("ia-cartao-retro-thanks", "Cartao retro thanks", "Para agradecimento com calor visual e circulos marcantes.", 1050, 600, "card-stamp", "retro-sun"),
        ("ia-cartao-paper-gift", "Cartao paper gift", "Para voucher, gift card e lembranca com camadas suaves.", 1050, 600, "card-layer", "paper-cut"),
        ("ia-cartao-luxe-signature", "Cartao luxe signature", "Para luxo, imobiliario, joalheria ou consultoria premium.", 1050, 600, "card-frame", "mono-luxe"),
        ("ia-cartao-brutalist-visit", "Cartao brutalist visit", "Para presencia marcante com contraste e tipografia forte.", 1050, 600, "card-block", "brutalist-pop"),
    ],
    "briefings": [
        ("ia-briefing-blueprint-ops", "Briefing blueprint ops", "Para alinhamento tecnico com blocos, grade e areas de prova.", 1600, 900, "brief-grid", "blueprint-tech"),
        ("ia-briefing-editorial-client", "Briefing editorial client", "Para reunioes elegantes com lista de pontos e mood image.", 1600, 900, "brief-magazine", "editorial-sand"),
        ("ia-briefing-mesh-creative", "Briefing mesh creative", "Para kickoff criativo com cor viva e secao de referencias.", 1600, 900, "brief-columns", "mesh-gradient"),
        ("ia-briefing-botanical-brand", "Briefing botanical brand", "Para wellness, hospitality e marcas sensoriais.", 1600, 900, "brief-frame", "botanical-soft"),
    ],
    "emails": [
        ("ia-email-aurora-news", "Email aurora news", "Para newsletter moderna com hero leve e CTA transparente.", 1440, 900, "email-hero", "aurora-glass"),
        ("ia-email-brutalist-offer", "Email brutalist offer", "Para oferta direta com blocos fortes e contraste visual.", 1440, 900, "email-slab", "brutalist-pop"),
        ("ia-email-luxe-launch", "Email luxe launch", "Para lancamento premium com moldura fina e foto de destaque.", 1440, 900, "email-frame", "mono-luxe"),
        ("ia-email-paper-story", "Email paper story", "Para editorial de conteudo com recortes e area generosa para imagem.", 1440, 900, "email-story", "paper-cut"),
    ],
    "folders": [
        ("ia-folder-editorial-trifold", "Folder editorial trifold", "Para institucional com ritmo de revista e tres paineis claros.", 1600, 900, "folder-trifold", "editorial-sand"),
        ("ia-folder-retro-catalog", "Folder retro catalog", "Para colecoes, menus ou catalogos com energia calorosa.", 1600, 900, "folder-poster", "retro-sun"),
        ("ia-folder-blueprint-services", "Folder blueprint services", "Para servicos, arquitetura, engenharia ou consultoria tech.", 1600, 900, "folder-grid", "blueprint-tech"),
        ("ia-folder-aurora-showcase", "Folder aurora showcase", "Para produto ou portfolio com cards transparentes e brilho suave.", 1600, 900, "folder-showcase", "aurora-glass"),
    ],
}


def svg_data(style):
    a, b, c = style["accent"], style["accent2"], style["accent3"]
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 900 700'><rect width='900' height='700' fill='{style['bg2']}'/><circle cx='700' cy='180' r='160' fill='{a}' opacity='.72'/><circle cx='240' cy='520' r='180' fill='{b}' opacity='.58'/><rect x='180' y='140' width='460' height='420' rx='40' fill='{c}' opacity='.12'/><path d='M240 430c58-102 152-208 276-208 86 0 152 36 210 80-88 10-138 76-194 138-64 72-134 128-240 120-30-4-52-10-52-18z' fill='{a}' opacity='.22'/></svg>"
    return "data:image/svg+xml;utf8," + quote(svg, safe="(),.-_:/#%='\" ")


def slot(label, art, tall=False):
    klass = "slot tall" if tall else "slot"
    return f"<div class='{klass}' data-label='{label}'><img src='{art}' alt=''/></div>"


def layout(name, subtitle, art, kind):
    if kind == "hero-split":
        return f"<div class='grid2' style='height:100%'><section class='stack' style='align-content:center'><p class='eyebrow'>Hero Split</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='row'><span class='badge'>impacto</span><span class='badge'>imagem lateral</span><span class='badge'>capa</span></div></section><section>{slot('image area hero', art, True)}</section></div>"
    if kind == "magazine":
        return f"<div class='grid2' style='height:100%'><section class='stack'><p class='eyebrow'>Magazine Layout</p><h2>{name}</h2><p class='lede'>{subtitle}</p><div class='outline'><p>Bloco para contexto, subtitulo, resumo executivo ou narrativa da secao.</p></div><div class='grid2'><div class='card'><h3>Ponto 01</h3><p>Destaque de argumento ou caso.</p></div><div class='card'><h3>Ponto 02</h3><p>Espaco para dado ou beneficio.</p></div></div></section><section class='stack'><div class='card' style='padding:14px'>{slot('image area portrait', art)}</div><div class='row'><span class='badge'>editorial</span><span class='badge'>refinado</span></div></section></div>"
    if kind == "kpi-ribbon":
        return f"<div class='stack'><div class='between'><div class='stack' style='max-width:760px'><p class='eyebrow'>KPI Ribbon</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><span class='badge'>alta leitura</span></div><div class='grid4'><div class='metric'><strong>82%</strong><p>retencao</p></div><div class='metric'><strong>24h</strong><p>setup</p></div><div class='metric'><strong>12</strong><p>modulos</p></div><div class='metric'><strong>1</strong><p>narrativa</p></div></div>{slot('image area ribbon', art)}</div>"
    if kind == "dashboard":
        return f"<div class='grid2' style='height:100%'><section class='stack'><p class='eyebrow'>Dashboard</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='grid2'><div class='metric'><strong>+48%</strong><p>engajamento</p></div><div class='metric'><strong>09</strong><p>areas visuais</p></div><div class='metric'><strong>3x</strong><p>clareza</p></div><div class='metric'><strong>72h</strong><p>iteracao</p></div></div></section><section class='stack'><div class='card'>{slot('image area dashboard', art)}</div><div class='grid2'><div class='card'><h3>Insight</h3><p>Espaco para explicacao curta.</p></div><div class='card'><h3>Acao</h3><p>Proximo passo ou CTA.</p></div></div></section></div>"
    if kind == "monolith":
        return f"<div class='grid2' style='height:100%;grid-template-columns:.82fr 1.18fr'><section class='stack'><div class='card' style='height:100%;display:grid;align-content:space-between'><div class='stack'><p class='eyebrow'>Monolith</p><h1>{name}</h1><p class='lede'>{subtitle}</p></div><div class='row'><span class='badge'>luxe</span><span class='badge'>premium</span></div></div></section><section>{slot('image area monolith', art, True)}</section></div>"
    if kind == "overlap":
        return f"<div class='stack' style='height:100%'><div class='between'><div class='stack' style='max-width:760px'><p class='eyebrow'>Overlap</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><span class='badge'>camadas</span></div><div style='position:relative;height:100%'><div class='card' style='position:absolute;inset:40px 160px 60px 0'>{slot('image area back', art, True)}</div><div class='card' style='position:absolute;inset:0 0 130px 380px'><div class='stack'><h3>Camada superior</h3><p>Texto, quote, beneficio ou detalhe de proposta.</p><div class='outline'><p>Area de destaque.</p></div></div></div></div></div>"
    if kind == "diagonal":
        return f"<div class='grid2' style='height:100%;grid-template-columns:1.1fr .9fr'><section class='stack' style='align-content:center'><p class='eyebrow'>Diagonal</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='row'><span class='badge'>moderno</span><span class='badge'>dinamico</span></div></section><section style='clip-path:polygon(18% 0,100% 0,100% 100%,0 100%)'>{slot('image area diagonal', art, True)}</section></div>"
    if kind == "frame":
        return f"<div class='stack center' style='height:100%;text-align:center'><div class='card' style='width:min(100%,980px);padding:24px'><p class='eyebrow'>Frame</p><h1>{name}</h1><p class='lede' style='margin:0 auto'>{subtitle}</p><div style='margin-top:20px'>{slot('image area framed', art)}</div></div></div>"
    if kind == "poster":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='stack'><p class='eyebrow'>Poster</p><h1>{name}</h1><p class='lede'>{subtitle}</p></div>{slot('image area poster', art)}<div class='row'><span class='badge'>headline</span><span class='badge'>data</span><span class='badge'>cta</span></div></div>"
    if kind == "roadmap":
        return f"<div class='stack'><div class='stack' style='max-width:860px'><p class='eyebrow'>Roadmap</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><div class='grid4'><div class='card'><h3>01</h3><p>Diagnostico</p></div><div class='card'><h3>02</h3><p>Direcao</p></div><div class='card'><h3>03</h3><p>Producao</p></div><div class='card'><h3>04</h3><p>Entrega</p></div></div>{slot('image area roadmap', art)}</div>"
    if kind == "quote-stage":
        return f"<div class='grid2' style='height:100%'><section class='stack' style='align-content:center'><p class='eyebrow'>Quote Stage</p><h1>\"Uma ideia forte precisa de palco visual.\"</h1><p class='lede'>{subtitle}</p><span class='badge'>manifesto</span></section><section class='card'>{slot('image area cinematic', art, True)}</section></div>"
    if kind == "cascade":
        return f"<div class='grid2' style='height:100%'><section class='stack'><p class='eyebrow'>Cascade</p><h2>{name}</h2><p class='lede'>{subtitle}</p><div class='card' style='margin-left:0'><h3>Card 01</h3><p>Mensagem principal</p></div><div class='card' style='margin-left:44px'><h3>Card 02</h3><p>Prova ou detalhe</p></div><div class='card' style='margin-left:88px'><h3>Card 03</h3><p>CTA ou fechamento</p></div></section><section>{slot('image area cascade', art, True)}</section></div>"
    if kind == "social-product":
        return f"<div class='stack center' style='height:100%;text-align:center'><p class='eyebrow'>Instagram Product</p><h1>{name}</h1><div style='width:78%'>{slot('image area square', art)}</div><p class='lede' style='max-width:20ch'>{subtitle}</p><span class='badge'>arraste para salvar</span></div>"
    if kind == "social-burst":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='between'><div class='stack'><p class='eyebrow'>Sale Burst</p><h2>{name}</h2></div><div class='badge'>-30%</div></div>{slot('image area promo', art)}<p class='lede'>{subtitle}</p></div>"
    if kind == "social-quote":
        return f"<div class='stack center' style='height:100%;text-align:center'><p class='eyebrow'>Quote Grid</p><div class='card' style='width:100%'><h1>Design chama. Conteudo segura.</h1></div><div class='grid2' style='width:100%'><div class='card'><p>{subtitle}</p></div>{slot('image area quote', art)}</div></div>"
    if kind == "social-editorial":
        return f"<div class='grid2' style='height:100%'><section class='stack' style='align-content:center'><p class='eyebrow'>Editorial Post</p><h1>{name}</h1><p class='lede'>{subtitle}</p></section><section>{slot('image area editorial', art, True)}</section></div>"
    if kind == "social-block":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='card' style='background:var(--accent);color:#fff'><p style='color:rgba(255,255,255,.74)' class='eyebrow'>Block Post</p><h1>{name}</h1></div>{slot('image area announcement', art)}<div class='row'><span class='badge'>evento</span><span class='badge'>data</span><span class='badge'>local</span></div></div>"
    if kind == "social-monogram":
        return f"<div class='stack center' style='height:100%;text-align:center'><div class='card' style='width:100%;padding:34px'><p class='eyebrow'>Monogram</p><div style='font-size:120px;letter-spacing:-.06em;font-weight:800'>M</div><h2>{name}</h2><p class='lede' style='max-width:18ch;margin:0 auto'>{subtitle}</p></div></div>"
    if kind == "social-collage":
        return f"<div class='stack'><div class='between'><div class='stack'><p class='eyebrow'>Collage</p><h2>{name}</h2></div><span class='badge'>recortes</span></div><div style='position:relative;height:700px'><div class='card' style='position:absolute;inset:0 120px 160px 0'>{slot('image area collage main', art, True)}</div><div class='card' style='position:absolute;inset:260px 0 0 240px'><h3>Texto</h3><p>{subtitle}</p></div></div></div>"
    if kind == "social-card":
        return f"<div class='stack'><p class='eyebrow'>Card Layout</p><div class='card'><h1>{name}</h1><p class='lede'>{subtitle}</p></div><div class='grid2'><div class='card'><h3>Checklist</h3><p>1. ponto</p><p>2. ponto</p><p>3. ponto</p></div>{slot('image area reference', art)}</div></div>"
    if kind == "poster-hero":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='card' style='padding:18px'>{slot('image area hero poster', art)}</div><div class='stack'><p class='eyebrow'>Premiere</p><h1>{name}</h1><p class='lede'>{subtitle}</p></div><div class='row'><span class='badge'>sexta 21h</span><span class='badge'>ingressos</span></div></div>"
    if kind == "poster-burst":
        return f"<div class='stack'><div class='between'><div class='badge'>festival</div><div class='badge'>2026</div></div><h1>{name}</h1>{slot('image area poster main', art)}<p class='lede'>{subtitle}</p></div>"
    if kind == "poster-editorial":
        return f"<div class='stack'><p class='eyebrow'>Gallery Poster</p><h1>{name}</h1><div class='grid2'><div class='card'><p>{subtitle}</p><div class='outline' style='margin-top:18px'><p>Local, data e contato.</p></div></div>{slot('image area gallery', art)}</div></div>"
    if kind == "poster-grid":
        return f"<div class='stack'><div class='grid2'><div class='card'><p class='eyebrow'>Night Event</p><h1>{name}</h1><p class='lede'>{subtitle}</p></div><div class='card'>{slot('image area headliner', art)}</div></div><div class='grid3'><div class='metric'><strong>22:00</strong><p>abertura</p></div><div class='metric'><strong>03</strong><p>sets</p></div><div class='metric'><strong>VIP</strong><p>lista</p></div></div></div>"
    if kind == "poster-frame":
        return f"<div class='stack'><div class='card' style='padding:16px'>{slot('image area framed poster', art)}</div><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='row'><span class='badge'>sabado</span><span class='badge'>rua central</span></div></div>"
    if kind == "poster-stack":
        return f"<div class='stack'><div class='card' style='background:var(--accent);color:#fff'><h1>{name}</h1></div><div class='card'>{slot('image area offer', art)}</div><div class='card'><p>{subtitle}</p></div></div>"
    if kind == "invite-ornate":
        return f"<div class='stack center' style='height:100%;text-align:center'><div class='card' style='width:100%;padding:34px;border-radius:34px'><div class='outline' style='padding:26px'><p class='eyebrow'>Invitation</p><h1>{name}</h1><p class='lede' style='max-width:18ch;margin:0 auto'>{subtitle}</p><div style='margin-top:22px'>{slot('image area cover', art)}</div><div class='row' style='justify-content:center'><span class='badge'>22 maio</span><span class='badge'>19h</span><span class='badge'>rsvp</span></div></div></div></div>"
    if kind == "invite-soft":
        return f"<div class='stack center' style='height:100%;text-align:center'><p class='eyebrow'>Soft Invitation</p><h1>{name}</h1><p class='lede' style='max-width:18ch'>{subtitle}</p><div style='width:100%'>{slot('image area invitation', art)}</div></div>"
    if kind == "invite-poster":
        return f"<div class='stack'><div class='between'><div class='badge'>save the date</div><div class='badge'>festa</div></div><h1>{name}</h1>{slot('image area party', art)}<p class='lede'>{subtitle}</p></div>"
    if kind == "invite-collage":
        return f"<div style='position:relative;height:100%'><div class='card' style='position:absolute;inset:0 180px 240px 0'>{slot('image area collage', art, True)}</div><div class='card' style='position:absolute;inset:220px 0 0 300px'><p class='eyebrow'>Exhibition Invite</p><h2>{name}</h2><p>{subtitle}</p><div class='row'><span class='badge'>abertura</span><span class='badge'>local</span></div></div></div>"
    if kind == "invite-frame":
        return f"<div class='stack center' style='height:100%;text-align:center'><div class='outline' style='width:100%;padding:24px;border-radius:34px'><p class='eyebrow'>Dinner Invite</p><h1>{name}</h1><p class='lede' style='max-width:18ch;margin:0 auto'>{subtitle}</p><div style='margin-top:20px'>{slot('image area menu', art)}</div></div></div>"
    if kind == "invite-panel":
        return f"<div class='grid2' style='height:100%'><section class='card'><p class='eyebrow'>Launch Invite</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='grid2'><div class='metric'><strong>12/06</strong><p>data</p></div><div class='metric'><strong>20h</strong><p>hora</p></div></div></section><section>{slot('image area launch', art, True)}</section></div>"
    if kind == "card-split":
        return f"<div class='grid2' style='height:100%'><section class='stack' style='align-content:center'><p class='eyebrow'>Editorial Card</p><h2>{name}</h2><p>{subtitle}</p><p style='font-size:14px;letter-spacing:.12em;text-transform:uppercase'>nome | cargo | contato</p></section><section>{slot('image area signature', art, True)}</section></div>"
    if kind == "card-glow":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='between'><div class='stack'><p class='eyebrow'>Glow Card</p><h2>{name}</h2></div><span class='badge'>identity</span></div>{slot('image area glow', art)}<p>{subtitle}</p></div>"
    if kind == "card-stamp":
        return f"<div class='grid2' style='height:100%'><section class='card' style='background:var(--accent);color:#fff'><p style='color:rgba(255,255,255,.72)' class='eyebrow'>Thanks Card</p><h2>{name}</h2><p style='color:rgba(255,255,255,.82)'>{subtitle}</p></section><section>{slot('image area stamp', art, True)}</section></div>"
    if kind == "card-layer":
        return f"<div style='position:relative;height:100%'><div class='card' style='position:absolute;inset:24px 240px 24px 0'><h2>{name}</h2><p>{subtitle}</p></div><div class='card' style='position:absolute;inset:60px 0 60px 420px'>{slot('image area gift', art, True)}</div></div>"
    if kind == "card-frame":
        return f"<div class='stack center' style='height:100%;text-align:center'><div class='outline' style='width:100%;padding:22px;border-radius:30px'><h2>{name}</h2><p>{subtitle}</p><div class='row' style='justify-content:center'><span class='badge'>luxo</span><span class='badge'>minimal</span></div></div></div>"
    if kind == "card-block":
        return f"<div class='grid3' style='height:100%'><section class='card' style='background:var(--accent);color:#fff'><h2>{name}</h2></section><section class='card'><p>{subtitle}</p></section><section>{slot('image area block', art, True)}</section></div>"
    if kind == "brief-grid":
        return f"<div class='stack'><div class='between'><div class='stack'><p class='eyebrow'>Brief Grid</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><span class='badge'>ops</span></div><div class='grid3'><div class='card'><h3>Objetivo</h3><p>O que precisa acontecer.</p></div><div class='card'><h3>Publico</h3><p>Quem precisa ser impactado.</p></div><div class='card'><h3>Escopo</h3><p>Formatos, prazo e dono.</p></div></div>{slot('image area evidence', art)}</div>"
    if kind == "brief-magazine":
        return f"<div class='grid2' style='height:100%'><section class='stack'><p class='eyebrow'>Client Brief</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='number-list'><div class='number-item'><div class='num'>01</div><div><h3>Meta</h3><p>Defina o objetivo principal.</p></div></div><div class='number-item'><div class='num'>02</div><div><h3>Tom</h3><p>Como a marca quer soar.</p></div></div><div class='number-item'><div class='num'>03</div><div><h3>Ref</h3><p>Quais referencias ajudam.</p></div></div></div></section><section>{slot('image area moodboard', art, True)}</section></div>"
    if kind == "brief-columns":
        return f"<div class='grid3' style='height:100%'><section class='card'><p class='eyebrow'>Contexto</p><h3>Desafio</h3><p>{subtitle}</p></section><section class='card'><p class='eyebrow'>Mensagem</p><h3>Direcao</h3><p>Espaco para narrativa central e tom.</p></section><section>{slot('image area refs', art, True)}</section></div>"
    if kind == "brief-frame":
        return f"<div class='stack'><div class='card'><p class='eyebrow'>Brand Brief</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><div class='grid2'><div class='outline'><p>Essencia</p><p>Publico</p><p>Oferta</p><p>Diferencial</p></div>{slot('image area atmosphere', art)}</div></div>"
    if kind == "email-hero":
        return f"<div class='stack' style='height:100%;justify-content:space-between'><div class='row'><span class='badge'>newsletter</span><span class='badge'>email</span></div><div class='grid2'><section class='stack' style='align-content:center'><h1>{name}</h1><p class='lede'>{subtitle}</p><span class='badge'>saiba mais</span></section><section>{slot('image area email hero', art, True)}</section></div></div>"
    if kind == "email-slab":
        return f"<div class='grid3' style='height:100%'><section class='card' style='background:var(--accent);color:#fff'><h2>{name}</h2><p style='color:rgba(255,255,255,.8)'>{subtitle}</p></section><section class='card'>{slot('image area offer', art)}</section><section class='card'><h3>CTA</h3><p>Botao, beneficio, prova.</p></section></div>"
    if kind == "email-frame":
        return f"<div class='stack'><div class='outline' style='padding:20px'><div class='between'><div class='stack'><p class='eyebrow'>Launch Mail</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><span class='badge'>premium</span></div></div>{slot('image area launch story', art)}</div>"
    if kind == "email-story":
        return f"<div class='grid2' style='height:100%'><section>{slot('image area article', art, True)}</section><section class='stack' style='align-content:center'><p class='eyebrow'>Story Mail</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='card'><p>Bloco para texto, CTA e nota complementar.</p></div></section></div>"
    if kind == "folder-trifold":
        return f"<div class='grid3' style='height:100%'><section class='card'><p class='eyebrow'>Panel 01</p><h2>{name}</h2><p>{subtitle}</p></section><section>{slot('image area central fold', art, True)}</section><section class='card'><h3>Panel 03</h3><p>Contato, agenda, servicos ou colecao.</p></section></div>"
    if kind == "folder-poster":
        return f"<div class='stack'><div class='between'><div class='stack'><p class='eyebrow'>Catalog Fold</p><h2>{name}</h2></div><span class='badge'>3 paineis</span></div><div class='grid3'><div class='card'><p>{subtitle}</p></div>{slot('image area showcase', art)}<div class='card'><h3>Detalhes</h3><p>Preco, locais, horario ou diferenciais.</p></div></div></div>"
    if kind == "folder-grid":
        return f"<div class='grid2' style='height:100%'><section class='stack'><p class='eyebrow'>Services Fold</p><h1>{name}</h1><p class='lede'>{subtitle}</p><div class='grid2'><div class='card'><h3>Servico 1</h3></div><div class='card'><h3>Servico 2</h3></div><div class='card'><h3>Servico 3</h3></div><div class='card'><h3>Servico 4</h3></div></div></section><section>{slot('image area systems', art, True)}</section></div>"
    if kind == "folder-showcase":
        return f"<div class='stack'><div class='card'><p class='eyebrow'>Showcase Fold</p><h2>{name}</h2><p class='lede'>{subtitle}</p></div><div class='grid3'>{slot('image area hero fold', art)}<div class='card'><p>Bloco de descricao ou beneficio.</p></div><div class='card'><p>Contato, CTA ou detalhe tecnico.</p></div></div></div>"
    return f"<div class='stack'><h1>{name}</h1><p>{subtitle}</p>{slot('image area', art)}</div>"


def page(title, category, style_name, size, layout_html):
    style = STYLES[style_name]
    w, h = size
    dark = " dark" if style.get("dark") else ""
    return f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'/><meta name='viewport' content='width=device-width, initial-scale=1.0'/><title>{title}</title><link rel='stylesheet' href='../styles.css'/></head><body><div class='page'><main class='canvas {style['cls']}{dark}' style='--w:{w}px;--ratio:{w}/{h};--bg:{style['bg']};--bg2:{style['bg2']};--accent:{style['accent']};--accent-2:{style['accent2']};--accent-3:{style['accent3']}'><div class='inner'>{layout_html}<p class='footer'>{category} | {style_name}</p></div></main></div></body></html>"


def build_index(manifest):
    parts = ["<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'/><meta name='viewport' content='width=device-width, initial-scale=1.0'/><title>Biblioteca IA de templates</title><link rel='stylesheet' href='./styles.css'/></head><body><div class='page'><div class='catalog'><div class='stack'><p class='eyebrow'>AI Template Library</p><h1>50 templates visuais com estilos realmente diferentes</h1><p class='lede'>Arquivos nomeados para um agente de IA identificar rapido por categoria, linguagem visual e estrutura. Cada um tem area de imagem, sobreposicoes, bordas finas, transparencia e composicao propria.</p></div>"]
    for category, items in manifest.items():
        parts.append(f"<section class='catalog-section'><div class='between'><div class='stack'><p class='eyebrow'>{category}</p><h2>{category.title()}</h2></div><span class='badge'>{len(items)} modelos</span></div><div class='catalog-grid'>")
        for title, rel, style_name in items:
            style = STYLES[style_name]
            parts.append(f"<a class='catalog-card' href='./{rel}' style='--accent:{style['accent']};--accent-2:{style['accent2']}'><h3>{title}</h3><p>{style_name}</p><div class='thumb'></div></a>")
        parts.append("</div></section>")
    parts.append("</div></div></body></html>")
    return "".join(parts)


def main():
    (ROOT / "styles.css").write_text(CSS, encoding="utf-8")
    manifest = {}
    total = 0
    for category, items in ITEMS.items():
        manifest[category] = []
        for slug, title, subtitle, w, h, kind, style_name in items:
            style = STYLES[style_name]
            art = svg_data(style)
            html = page(title, category, style_name, (w, h), layout(title, subtitle, art, kind))
            path = ROOT / category / f"{slug}.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(html, encoding="utf-8")
            manifest[category].append((title, f"{category}/{slug}.html", style_name))
            total += 1
    (ROOT / "index.html").write_text(build_index(manifest), encoding="utf-8")
    print(f"Generated {total} templates.")


if __name__ == "__main__":
    main()
