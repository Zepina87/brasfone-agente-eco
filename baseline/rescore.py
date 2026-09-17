#!/usr/bin/env python3
"""O Eco - reprocessa um raw JSONL ja gravado com os aliases de outra versao da bateria.
Zero chamadas de API. Existe porque o scoring e regex deterministico sobre respostas gravadas,
logo acrescentar um concorrente aos aliases NAO exige medir de novo: mede-se o passado.

v1.1 (2026-09-15): acrescenta QUOTA RELATIVA ao lado do absoluto, com a MESMA definicao do
motor cloud (triggerdev-jobs/src/lib/geo/scoring.ts), para que manual e cloud deem o mesmo
numero sobre o mesmo raw. Porque: entre 25-08 e 09-09 todas as marcas dobraram no Sonar; em
absoluto parecia vitoria, em quota nos caimos de 55,6% para 48,8%. Quando todas sobem na mesma
proporcao, o motor mudou de comportamento, nao nos. Regra de ausencia: sem base nao ha numero.
n=0 da None em abs; soma de mencoes 0 da None em quota. Nunca 0 silencioso.

Formato de saida (compativel para tras): os campos absolutos ficam como estavam, com a chave
da marca a apontar para o numero; a quota entra em "quota" ao lado, e "_mencoes" conta o bolo.

Uso: rescore.py <raw.jsonl> <prompts-baseline-vX.json> <saida-sov.json>"""
import json, re, sys, unicodedata, os
raw_f, bat_f, out_f = sys.argv[1], sys.argv[2], sys.argv[3]
BASE = os.path.dirname(os.path.abspath(__file__))
BAT = json.load(open(bat_f if os.path.isabs(bat_f) else os.path.join(BASE, "..", bat_f)))
ENGINES = ["perplexity/sonar", "openai/gpt-5-mini", "google/gemini-3.7-flash"]
def norm(t): return unicodedata.normalize("NFKD", t.lower()).encode("ascii","ignore").decode()
def mentions(text, names):
    n = norm(text)
    return {x: bool(re.search(r"\b"+re.escape(norm(x)), n)) for x in names}

def bloco(rs, names):
    """Absoluto (% de respostas que mencionam) e quota (fatia do total de mencoes)."""
    n = len(rs)
    cont = {x: sum(1 for r in rs if r["mentions"][x]) for x in names}
    soma = sum(cont.values())
    out = {x: (round(100*cont[x]/n, 1) if n else None) for x in names}
    out["_n"] = n
    out["_mencoes"] = soma
    out["quota"] = {x: (round(100*cont[x]/soma, 1) if soma else None) for x in names}
    return out

names = BAT["marcas_alvo"] + BAT["concorrentes"]
rows = [json.loads(l) for l in open(raw_f, encoding="utf-8")]
for r in rows: r["mentions"] = mentions(r["answer"], names)
sov = [r for r in rows if r["sov"] and not r["answer"].startswith("__ERRO__")]
data = os.path.basename(raw_f).replace("raw-","").replace(".jsonl","")
agg = {"data": data, "versao_bateria": BAT["versao"],
       "reprocessado_de": os.path.basename(raw_f),
       "erros": sum(1 for r in rows if r["answer"].startswith("__ERRO__")),
       "por_motor": {eng: bloco([r for r in sov if r["engine"] == eng], names) for eng in ENGINES},
       "total": bloco(sov, names)}
json.dump(agg, open(out_f,"w"), ensure_ascii=False, indent=2)
print("FEITO:", out_f)
nos = [n for n in BAT["marcas_alvo"]]
q = agg["total"]["quota"]
fatia = sum(q[n] for n in nos if q[n] is not None) if any(q[n] is not None for n in nos) else None
print(f"total absoluto: " + ", ".join(f"{n}={agg['total'][n]}" for n in names))
print(f"total quota:    " + ", ".join(f"{n}={q[n]}" for n in names))
print(f"NOSSA FATIA (brasfone+inubia): {fatia}%")
