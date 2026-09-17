#!/bin/bash
# Actualiza a copia local da lista canonica de bots de IA.
# Deliberadamente MANUAL: o auditor nao vai a rede sozinho, para a medicao ser reproduzivel.
# Fonte: ai-robots-txt/ai.robots.txt (MIT, 68 contribuidores). Correu a primeira vez em 2026-09-14.
set -eu
D="$(cd "$(dirname "$0")/.." && pwd)/kb/dados/ai-robots.json"
T=$(mktemp)
curl -fsSL -m 60 "https://raw.githubusercontent.com/ai-robots-txt/ai.robots.txt/main/robots.json" -o "$T"
ANTES=$(python3 -c "import json;d=json.load(open('$D'));print(len([k for k in d if not k.startswith('_')]))" 2>/dev/null || echo 0)
python3 - "$T" "$D" <<'PY'
import json,sys,datetime
novo=json.load(open(sys.argv[1]))
try: velho=json.load(open(sys.argv[2]))
except Exception: velho={}
meta=velho.get('_proveniencia',{})
meta.update({'fonte':'https://github.com/ai-robots-txt/ai.robots.txt','ficheiro':'robots.json',
 'licenca':'MIT','descarregado':datetime.date.today().isoformat(),
 'nota':'Copia local deliberada. O auditor NAO vai a rede em cada execucao.'})
out={'_proveniencia':meta}; out.update(novo)
json.dump(out, open(sys.argv[2],'w'), ensure_ascii=False, indent=1)
print(f"  {len(novo)} bots gravados")
PY
DEPOIS=$(python3 -c "import json;d=json.load(open('$D'));print(len([k for k in d if not k.startswith('_')]))")
echo "  antes: $ANTES  depois: $DEPOIS"
rm -f "$T"
