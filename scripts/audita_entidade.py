#!/usr/bin/env python3
"""O Eco - vigia da entidade no Wikidata.

Porque existe: a 2026-09-14 medimos que procurar "Inubia" no Wikidata devolve QUATRO entidades,
todas brasileiras (o instrumento, o municipio de Inubia Paulista, a povoacao e uma pagina de
desambiguacao), e que "Brasfone" nao existe de todo. Nenhum concorrente tem entidade; o Pipedrive
tem (Q24054211). Isto explica mecanicamente porque o Gemini nos confunde com uma homonima
brasileira: quando um modelo procura quem somos, encontra o Brasil.

Porque NAO usamos o mcp-wikidata (zzaebok, 48 estrelas, parado desde Marco de 2026): ele faz
search e SPARQL genericos, que sao 2 chamadas curl. O que o Eco precisa e outra coisa, e ele nao
da: vigiar a MESMA pergunta ao longo do tempo, connosco e com os concorrentes, e gritar quando
alguem aparecer. Isso e serie temporal, nao e uma consulta.

Stdlib apenas. Nao escreve no Wikidata: escrever la e acto publico e leva ordem de Jose.

Uso:  python3 audita_entidade.py [--json baseline/entidade-DATA.json]
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import date

API = "https://www.wikidata.org/w/api.php"
UA = "EcoGEO/1.0 (https://inubia.pt; auditoria de entidade)"

# Quem vigiamos. Ordem: nos primeiro, depois quem disputa o mesmo espaco.
NOSSOS = ["Inubia", "Brasfone"]
CONCORRENTES = ["SmartLinks", "SoulSales", "Neeaconsulting", "Digital Xperience",
                "Priceless Consulting", "revaliQ"]
ANCORA = ("Pipedrive", "Q24054211")  # a entidade que ja existe e a que nos podemos ligar

# Sinais de que um resultado NAO e nosso. Se todos os resultados baterem aqui, o nome esta ocupado.
SINAIS_ALHEIOS = ("brasil", "brazil", "paulista", "município", "municipio", "instrumento",
                  "desambigua", "human settlement", "wikimedia")


def consulta(termo, lingua="pt", limite=8):
    q = urllib.parse.urlencode({
        "action": "wbsearchentities", "search": termo, "language": lingua,
        "uselang": lingua, "format": "json", "limit": limite,
    })
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("search", []), None
    except Exception as e:
        return None, str(e)


def classifica(termo, resultados):
    """Quatro estados. A consulta falhada nao e 'nao existe', e a descricao vazia nao e 'e nossa'.

    Defeito corrigido a 2026-09-14, apanhado no primeiro teste: a versao anterior classificava
    "Inubia" como TALVEZ NOSSA por causa de Q10303405, que tem descricao VAZIA e por isso nao
    batia em nenhum sinal alheio. Ausencia de informacao a ser lida como prova a favor, que e
    exactamente o erro que estes scripts existem para nao cometer. Sem descricao, indeterminado.
    """
    if resultados is None:
        return "NAO VERIFICADO"
    if not resultados:
        return "AUSENTE"
    candidatas = 0
    for r in resultados:
        desc = (r.get("description") or "").strip()
        if not desc:
            continue  # sem descricao nao conta a favor nem contra
        texto = f"{r.get('label','')} {desc}".lower()
        if not any(s in texto for s in SINAIS_ALHEIOS):
            candidatas += 1
    if candidatas:
        return "TALVEZ NOSSA"   # candidata a confirmar a olho, nunca automatico
    return "NOME OCUPADO"


def main():
    saida = None
    if "--json" in sys.argv:
        i = sys.argv.index("--json")
        if i + 1 < len(sys.argv):
            saida = sys.argv[i + 1]

    r = {"data": date.today().isoformat(), "nossos": {}, "concorrentes": {}, "ancora": {}}
    print(f"\n{'='*70}\n  ENTIDADE NO WIKIDATA   {r['data']}\n{'='*70}")

    print("\n  NOS")
    for t in NOSSOS:
        res, err = consulta(t)
        est = classifica(t, res)
        r["nossos"][t] = {"estado": est, "erro": err,
                          "resultados": [{"id": x["id"], "label": x.get("label"),
                                          "desc": x.get("description")} for x in (res or [])]}
        print(f"    {t:<22} {est}")
        for x in (res or [])[:4]:
            print(f"        {x['id']:<11} {x.get('label','')} | {(x.get('description') or '(sem descricao)')[:52]}")

    print("\n  CONCORRENTES")
    for t in CONCORRENTES:
        res, err = consulta(t)
        est = classifica(t, res)
        r["concorrentes"][t] = {"estado": est, "erro": err, "n": len(res or [])}
        print(f"    {t:<22} {est}")

    nome, qid = ANCORA
    res, err = consulta(nome)
    tem = any(x["id"] == qid for x in (res or []))
    r["ancora"] = {"nome": nome, "qid": qid, "existe": tem, "erro": err}
    print(f"\n  ANCORA\n    {nome} ({qid}): {'existe' if tem else 'NAO ENCONTRADA'}")

    # Veredicto: uma linha que se le sem pensar.
    ocupados = [t for t, v in r["nossos"].items() if v["estado"] == "NOME OCUPADO"]
    ausentes = [t for t, v in r["nossos"].items() if v["estado"] == "AUSENTE"]
    conc_com = [t for t, v in r["concorrentes"].items() if v["estado"] == "TALVEZ NOSSA"]
    print(f"\n{'-'*70}\n  VEREDICTO")
    if ocupados:
        print(f"    NOME OCUPADO por entidades alheias: {', '.join(ocupados)}")
        print("    Um modelo que procure quem somos encontra outra coisa. Isto nao se resolve")
        print("    com conteudo no nosso site: resolve-se com entidade propria e sameAs.")
    if ausentes:
        print(f"    SEM ENTIDADE NENHUMA: {', '.join(ausentes)}")
    if conc_com:
        print(f"    ATENCAO: concorrentes que podem ja ter entidade: {', '.join(conc_com)}")
    else:
        print("    Nenhum concorrente tem entidade. O terreno esta vazio para todos.")
    if r["ancora"]["existe"]:
        print(f"    Ancora disponivel: ligar a nossa entidade a {qid} ({nome}) da-nos apoio")
        print("    num item que ja e notorio, em vez de nascermos isolados.")
    print(f"{'-'*70}")

    if saida:
        with open(saida, "w", encoding="utf-8") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        print(f"  JSON: {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
