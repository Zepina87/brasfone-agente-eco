#!/usr/bin/env python3
"""O Eco - baseline share of voice. 25 prompts x 4 motores x 2 amostras via OpenRouter.
Output: JSONL bruto + agregado JSON. Deterministico: o scoring e' regex de aliases, nunca LLM.

Claude entrou a 2026-09-17 (ordem de Jose: "e vital"). A missao do Eco ja o nomeava desde
2026-08-25 ("ChatGPT, Perplexity, Gemini, Copilot e Claude") mas a bateria so testava 3; o
Claude nunca tinha sido medido. Usa-se claude-haiku-4.5, nao o Sonnet: os outros dois motores
raw (gpt-5-mini, gemini-3.7-flash) sao as variantes pequenas dos respectivos fabricantes, e
comparar o Claude topo de gama contra "minis" enviesava a leitura a favor do Claude so por
tamanho. Testado por chamada real antes de entrar: responde, nao cita fontes (e' modelo raw,
sem pesquisa, como os outros dois), custo ~0,0006 USD por chamada. Falta o Copilot: sem API
aberta equivalente, fica registado como limitacao, nao descartado."""
import json, os, re, sys, time, unicodedata, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

KEY = os.environ["OPENROUTER_API_KEY"]
BASE = os.path.dirname(os.path.abspath(__file__))
BATFILE = os.environ.get("ECO_BATERIA", "prompts-baseline.json")
BAT = json.load(open(os.path.join(BASE, "..", BATFILE)))
SUF = os.environ.get("ECO_SUFIXO", "")
ENGINES = ["perplexity/sonar", "openai/gpt-5-mini", "google/gemini-3.7-flash", "anthropic/claude-haiku-4.5"]
SAMPLES = 2
OUT_RAW = os.path.join(BASE, f"raw-{date.today().isoformat()}{SUF}.jsonl")
OUT_AGG = os.path.join(BASE, f"sov-{date.today().isoformat()}{SUF}.json")

def norm(t):
    return unicodedata.normalize("NFKD", t.lower()).encode("ascii", "ignore").decode()

def mentions(text, names):
    n = norm(text)
    return {name: bool(re.search(r"\b" + re.escape(norm(name)), n)) for name in names}

def call(engine, prompt, attempt=0):
    body = json.dumps({"model": engine, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 3000}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        if "error" in d: raise RuntimeError(d["error"])
        msg = d["choices"][0]["message"]
        content = msg.get("content") or ""
        if not content.strip(): raise RuntimeError("content vazio (reasoning comeu o budget)")
        # As citacoes do Sonar vivem em message.annotations (url_citation), NAO no texto.
        # Sem as guardar, a pergunta central do GEO ("a nossa pagina e a fonte?") fica sem resposta:
        # foi o que aconteceu as corridas de 25-08 e 09-09, cujas fontes se perderam.
        cites = [an.get("url_citation", {}).get("url", "")
                 for an in (msg.get("annotations") or []) if an.get("type") == "url_citation"]
        return content, d.get("usage", {}), [c for c in cites if c]
    except Exception as e:
        if attempt < 2:
            time.sleep(5 * (attempt + 1))
            return call(engine, prompt, attempt + 1)
        return f"__ERRO__ {e}", {}, []

done_keys = set()
if os.path.exists(OUT_RAW):
    for line in open(OUT_RAW):
        try:
            r = json.loads(line)
            if not r["answer"].startswith("__ERRO__"): done_keys.add((r["id"], r["engine"], r["sample"]))
        except Exception: pass
jobs = [(p, e, s) for p in BAT["prompts"] for e in ENGINES for s in range(SAMPLES)
        if (p["id"], e, s) not in done_keys]
print(f"{len(jobs)} chamadas planeadas", flush=True)
results, done = [], 0
with ThreadPoolExecutor(max_workers=4) as ex:
    futs = {ex.submit(call, e, p["q"]): (p, e, s) for p, e, s in jobs}
    with open(OUT_RAW, "a") as f:
        for fut in as_completed(futs):
            p, e, s = futs[fut]
            text, usage, cites = fut.result()
            rec = {"id": p["id"], "cat": p["cat"], "sov": p["sov"], "engine": e, "sample": s,
                   "q": p["q"], "answer": text, "usage": usage, "citations": cites,
                   "mentions": mentions(text, BAT["marcas_alvo"] + BAT["concorrentes"])}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n"); f.flush()
            results.append(rec); done += 1
            if done % 15 == 0: print(f"{done}/{len(jobs)}", flush=True)

# Agregado: % de respostas SOV que mencionam cada marca, por motor e total
names = BAT["marcas_alvo"] + BAT["concorrentes"]
agg = {"data": date.today().isoformat(), "versao_bateria": BAT["versao"], "erros": 0,
       "por_motor": {}, "total": {}}
results = [json.loads(l) for l in open(OUT_RAW)]
sov = [r for r in results if r["sov"] and not r["answer"].startswith("__ERRO__")]
agg["erros"] = sum(1 for r in results if r["answer"].startswith("__ERRO__"))
for eng in ENGINES:
    rs = [r for r in sov if r["engine"] == eng]
    agg["por_motor"][eng] = {n: round(100 * sum(r["mentions"][n] for r in rs) / max(len(rs), 1), 1) for n in names}
    agg["por_motor"][eng]["_n"] = len(rs)
agg["total"] = {n: round(100 * sum(r["mentions"][n] for r in sov) / max(len(sov), 1), 1) for n in names}
agg["total"]["_n"] = len(sov)
tok = sum(r["usage"].get("total_tokens", 0) for r in results)
agg["tokens_totais"] = tok
json.dump(agg, open(OUT_AGG, "w"), ensure_ascii=False, indent=2)
print("FEITO. Agregado:", OUT_AGG, flush=True)
print(json.dumps(agg["total"], ensure_ascii=False), flush=True)
