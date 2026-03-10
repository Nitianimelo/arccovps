import React, { useState } from 'react';
import { FileText, Download, Loader2, ChevronDown, ChevronUp } from 'lucide-react';

interface TextDocCardProps {
  title: string;
  content: string;
}

async function downloadExport(text: string, title: string, format: 'docx' | 'pdf') {
  const res = await fetch('/api/agent/export-doc', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, title, format }),
  });
  if (!res.ok) throw new Error(await res.text());
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${title.replace(/\s+/g, '_')}.${format}`;
  a.click();
  URL.revokeObjectURL(url);
}

const TextDocCard: React.FC<TextDocCardProps> = ({ title, content }) => {
  const [loading, setLoading] = useState<'docx' | 'pdf' | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [expanded, setExpanded] = useState(false);

  const preview = content.slice(0, 280).trim();
  const hasMore = content.length > 280;

  const handleDownload = async (fmt: 'docx' | 'pdf') => {
    setLoading(fmt);
    setError(null);
    try {
      await downloadExport(content, title, fmt);
    } catch (e: any) {
      setError(`Erro ao gerar ${fmt.toUpperCase()}: ${e.message}`);
    } finally {
      setLoading(null);
    }
  };

  return (
    <div className="my-3 rounded-xl border border-indigo-500/25 bg-[#0d0d0f] overflow-hidden shadow-lg shadow-indigo-500/5 w-full max-w-xl">
      {/* Header */}
      <div className="flex items-center gap-3 px-4 py-3 bg-indigo-500/8 border-b border-indigo-500/20">
        <div className="p-1.5 bg-indigo-500/15 rounded-lg">
          <FileText size={15} className="text-indigo-400" />
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-xs font-semibold text-indigo-100 truncate">{title}</p>
          <p className="text-[10px] text-indigo-400/60 mt-0.5">Documento de texto</p>
        </div>
      </div>

      {/* Preview */}
      <div className="px-4 pt-3 pb-2">
        <p className="text-xs text-neutral-400 leading-relaxed whitespace-pre-wrap font-mono">
          {expanded ? content : preview}
          {!expanded && hasMore && '...'}
        </p>
        {hasMore && (
          <button
            onClick={() => setExpanded(p => !p)}
            className="mt-1 flex items-center gap-1 text-[10px] text-neutral-600 hover:text-neutral-400 transition-colors"
          >
            {expanded ? <><ChevronUp size={11} /> Recolher</> : <><ChevronDown size={11} /> Ver tudo</>}
          </button>
        )}
      </div>

      {/* Actions */}
      <div className="flex gap-2 px-4 pb-3 pt-1">
        <button
          onClick={() => handleDownload('docx')}
          disabled={!!loading}
          className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-lg bg-[#1a1a2e] hover:bg-[#22223a] border border-indigo-500/30 text-indigo-300 text-xs font-medium transition-all disabled:opacity-50"
        >
          {loading === 'docx' ? <Loader2 size={12} className="animate-spin" /> : <Download size={12} />}
          Word (DOCX)
        </button>
        <button
          onClick={() => handleDownload('pdf')}
          disabled={!!loading}
          className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-lg bg-[#1a1a2e] hover:bg-[#22223a] border border-indigo-500/30 text-indigo-300 text-xs font-medium transition-all disabled:opacity-50"
        >
          {loading === 'pdf' ? <Loader2 size={12} className="animate-spin" /> : <Download size={12} />}
          PDF
        </button>
      </div>

      {error && (
        <p className="px-4 pb-3 text-[10px] text-red-400">{error}</p>
      )}
    </div>
  );
};

export default TextDocCard;
