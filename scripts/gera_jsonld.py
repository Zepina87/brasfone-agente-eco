#!/usr/bin/env python3
"""O Eco - gera o JSON-LD que falta as nossas superficies.

Porque existe: a auditoria de 2026-09-14 mediu inubia.pt com ZERO JSON-LD e meta description
vazia, e www.brasfone.pt so com LocalBusiness e WebSite. Faltam Organization, Service e FAQPage.
O gerador do repo claude-seo nao servia: so cobre reserva, encomenda, forum e perfil.

A entidade canonica esta fixada por Jose a 2026-08-25 e NAO se inventa aqui:
  tier = "Platinum Partner Pipedrive"  ·  relacao = "Inubia, marca do grupo Brasfone"
Nunca "Elite", nunca "anteriormente Brasfone".

Uso:  python3 gera_jsonld.py organization inubia
      python3 gera_jsonld.py faq perguntas.json
      python3 gera_jsonld.py service --nome "Implementacao Pipedrive" --descricao "..."
Saida: JSON-LD pronto a colar, ja dentro de <script type="application/ld+json">.
"""
import argparse
import json
import sys

# Entidade canonica. Alterar so por ordem de Jose.
ENTIDADES = {
    "inubia": {
        "name": "Inubia",
        "legalName": "Brasfone",
        "url": "https://inubia.pt",
        "description": ("Inubia, marca do grupo Brasfone. Platinum Partner Pipedrive em Portugal: "
                        "implementacao de CRM, automacao comercial e consultoria de inteligencia artificial."),
        "slogan": "Platinum Partner Pipedrive",
        "areaServed": ["PT", "ES"],
        # LinkedIn corrigido 2026-09-15: a Inubia TEM pagina propria (medido no HTML da homepage).
        "sameAs": ["https://www.brasfone.pt", "https://www.linkedin.com/company/inubia-pt"],
        "logo": "https://inubia.pt/wp/wp-content/uploads/2026/05/inubia-logo.png",
    },
    "brasfone": {
        "name": "Brasfone",
        "url": "https://www.brasfone.pt",
        "description": ("Brasfone, Platinum Partner Pipedrive em Portugal. Solucoes tecnologicas, "
                        "CRM, comunicacoes e consultoria de inteligencia artificial. Inubia e a marca do grupo."),
        "slogan": "Platinum Partner Pipedrive",
        "areaServed": ["PT", "ES"],
        "sameAs": ["https://inubia.pt", "https://www.linkedin.com/company/brasfone/"],
    },
}


def organization(chave, wikidata=None, wikidata_mae=None):
    """`wikidata` e `wikidata_mae` sao QIDs (ex. Q123). So existem no dia em que a entidade
    existir no Wikidata; ate la o comportamento e o de sempre. Um sameAs para o Wikidata e o
    sinal de desambiguacao mais forte que um JSON-LD pode dar: diz ao motor QUAL Inubia somos,
    quando o nome no grafo aponta hoje para quatro entidades brasileiras (medido 2026-09-14)."""
    e = ENTIDADES[chave]
    d = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": e["name"],
        "url": e["url"],
        "description": e["description"],
        "slogan": e["slogan"],
        "areaServed": e["areaServed"],
        "sameAs": e["sameAs"],
        "knowsAbout": ["Pipedrive", "CRM", "Automacao comercial", "Inteligencia artificial aplicada a vendas"],
    }
    if "logo" in e:
        d["logo"] = e["logo"]
    if wikidata:
        d["sameAs"] = [*d["sameAs"], f"https://www.wikidata.org/wiki/{wikidata}"]
    if "legalName" in e:
        mae = {"@type": "Organization", "name": e["legalName"], "url": "https://www.brasfone.pt"}
        if wikidata_mae:
            mae["sameAs"] = [f"https://www.wikidata.org/wiki/{wikidata_mae}"]
        d["parentOrganization"] = mae
    return d


def service(nome, descricao, entidade="inubia"):
    e = ENTIDADES[entidade]
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": nome,
        "description": descricao,
        "provider": {"@type": "Organization", "name": e["name"], "url": e["url"]},
        "areaServed": e["areaServed"],
        "serviceType": nome,
    }


def faq(pares):
    """pares: lista de {"pergunta": ..., "resposta": ...}.

    A resposta cabe em 134 a 167 palavras e responde nas primeiras 40 a 60 (kb/citabilidade.md).
    O script avisa quando sai fora, porque e esse o ponto de escrever FAQ para ser citada.
    """
    itens, avisos = [], []
    for i, p in enumerate(pares, 1):
        n = len(p["resposta"].split())
        if n < 40:
            avisos.append(f"  pergunta {i}: resposta com {n} palavras, curta demais para ser citada (alvo 134 a 167)")
        elif n > 200:
            avisos.append(f"  pergunta {i}: resposta com {n} palavras, longa demais para extraccao limpa (alvo 134 a 167)")
        itens.append({
            "@type": "Question",
            "name": p["pergunta"],
            "acceptedAnswer": {"@type": "Answer", "text": p["resposta"]},
        })
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": itens}, avisos


def imprime(d, avisos=None):
    print('<script type="application/ld+json">')
    print(json.dumps(d, ensure_ascii=False, indent=2))
    print("</script>")
    if avisos:
        print("\nAVISOS de citabilidade (kb/citabilidade.md):", file=sys.stderr)
        for a in avisos:
            print(a, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("organization", help="Organization para uma das nossas marcas")
    o.add_argument("entidade", choices=sorted(ENTIDADES))
    o.add_argument("--wikidata", metavar="QID", help="QID da entidade no Wikidata, quando existir (ex. Q123456)")
    o.add_argument("--wikidata-mae", metavar="QID", help="QID da Brasfone no Wikidata, para o parentOrganization")

    s = sub.add_parser("service", help="Service prestado por uma das marcas")
    s.add_argument("--nome", required=True)
    s.add_argument("--descricao", required=True)
    s.add_argument("--entidade", choices=sorted(ENTIDADES), default="inubia")

    f = sub.add_parser("faq", help="FAQPage a partir de um JSON com pergunta e resposta")
    f.add_argument("ficheiro", help='JSON: [{"pergunta": "...", "resposta": "..."}]')

    a = ap.parse_args()
    if a.cmd == "organization":
        imprime(organization(a.entidade, a.wikidata, a.wikidata_mae))
    elif a.cmd == "service":
        imprime(service(a.nome, a.descricao, a.entidade))
    else:
        with open(a.ficheiro, encoding="utf-8") as fh:
            pares = json.load(fh)
        d, avisos = faq(pares)
        imprime(d, avisos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
