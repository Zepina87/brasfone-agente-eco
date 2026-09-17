# Auditoria SEO (para lá do GEO) · www.brasfone.pt
**Data:** 2026-09-17 · **Âmbito:** SEO técnico e on-page. Isto excede o que o `audita_geo.py`
mede por desenho (esse cobre acesso de crawlers de IA, JSON-LD, meta description e pouco mais).
As verificações abaixo são ad-hoc, todas com comando à vista.
**Fora de alcance nesta auditoria:** Core Web Vitals via Lighthouse (a API pública do PageSpeed
Insights devolveu HTTP 429, limite de quota sem chave; precisa de `PAGESPEED_API_KEY` para dar
números reais de LCP/CLS/INP) e dados de posições/impressões reais (aguardam a conta de serviço
do Search Console, `ACTIVACAO-mcp-google.md`). O que se reporta aqui é medido, não estimado.

## 1. Indexação e arquitectura

**38 páginas** em `pages-sitemap.xml`, **73 posts** em `blog-posts-sitemap.xml`, mais sitemaps
próprios para produtos, categorias, equipa e perfis de membro (a maioria vazios ou de template
Wix, não populados). Três sitemaps de língua declarados no robots.txt: `sitemap.xml` (pt),
`en_en-sitemap.xml`, `es_es-sitemap.xml`.

**Achado, com peso para a expansão a Espanha que o Fábio já mencionou:** as URLs `/en` e `/es`
respondem HTTP 200 e existem sitemaps próprios para elas, **mas a homepage não tem uma única
tag `hreflang`**. Verificado directamente no HTML servido, sem ambiguidade. Sem `hreflang`, a
Google não sabe que `/en` e `/es` são versões de língua da mesma página, e ou as trata como
conteúdo duplicado, ou não as liga entre si. Isto é uma correcção técnica pequena com efeito
directo assim que a versão espanhola ganhar conteúdo a sério.

**Duas páginas quase-duplicadas por engano, ambas indexadas e ambas vivas:**
| URL | Título | Meta description |
|---|---|---|
| `/pipedrive-clinicas` | "LP Pipedrive Clinicas" | vazia |
| `/pipedriveclinicas` | "Clinicas youtube" | vazia |

Pelo nome, parecem duas landing pages de campanhas diferentes (uma de anúncio, outra de vídeo)
que ficaram as duas no sitemap principal. Conteúdo de campanha paga não devia estar indexado
para pesquisa orgânica de qualquer forma; hoje está, e concorre consigo mesmo.

**Uma página "blank" no sitemap.** `/blank` está listada em `pages-sitemap.xml` e responde
HTTP 301. É resíduo de template do Wix a ser submetido ao Google como se fosse conteúdo.
Inofensivo por si só, mas é o tipo de ruído que um sitemap limpo não devia ter.

## 2. Consistência de língua: achado que liga directamente ao problema do Wikidata

A página de contacto chama-se **`/contatos`**, com título "CONTATOS", grafia do **português do
Brasil**. Em PT-PT escreve-se "contactos". Dado que o problema central que estamos a resolver
esta semana é precisamente a confusão da marca com entidades brasileiras no Wikidata, ter uma
URL e um título em português do Brasil na própria superfície é o mesmo erro a aparecer noutro
sítio. Vale a pena corrigir a par da entrada no Wikidata, não depois.

## 3. On-page

**Sem canonical em duplicação real.** A homepage tem `<link rel="canonical">` a apontar para
si mesma, correcto. Não verificámos canonical nas 38 páginas uma a uma; dado o achado do ponto 1
(duas landing pages quase-idênticas sem canonical cruzado), vale a pena confirmar aí primeiro.

**Hierarquia de cabeçalhos, na homepage:** 1 `h1`, 4 `h2`, zero `h3` ou abaixo. O `h1` está em
maiúsculas fixas no HTML ("CRM, COMUNICAÇÃO E PRODUTIVIDADE") com entidades HTML mal decodificadas
na leitura crua (`&Ccedil;&Atilde;O`), o que é normal em maiúsculas via CSS mas confirmar que o
texto real por baixo está em português correcto, não em maiúsculas forçadas que depois um motor
lê literalmente.

**Imagens:** 10 na homepage, **0 sem atributo `alt`**. Isto está bem feito.

**Conteúdo por página, medido, não estimado:** as páginas verticais por sector não são finas.
`crm-academico` tem 377 palavras visíveis, `crm-banca` 424, `contatos` 174 (aceitável para uma
página de contacto). Os títulos e as meta descriptions das seis páginas verticais de CRM
(imobiliário, académico, tecnologia, serviços, banca, saúde) são **todos únicos**, sem duplicação
entre si — hipótese que levantei e que a verificação afastou.

## 4. Performance, o que se conseguiu medir sem a API

**Peso da homepage: 1,76 MB de HTML** para 751 palavras visíveis (já reportado pelo `audita_geo`).
**Compressão gzip activa**, confirmado no cabeçalho `content-encoding`. Isso ajuda a transferência,
não ajuda o processamento no browser: o peso é sobretudo markup e scripts do Wix, não texto.

**Sem número de Core Web Vitals real nesta auditoria.** Não inventar LCP nem CLS sem medição.
Para ter isso, ou se pede uma `PAGESPEED_API_KEY` (gratuita, quota generosa), ou espera-se pela
conta de serviço do Search Console, que dá dados de campo reais em vez de laboratório.

## 5. Segurança e cabeçalhos
`x-content-type-options: nosniff` presente. `server: Pepyaka` (infra-estrutura do Wix, normal).
Não verificado: CSP, HSTS, cabeçalhos de segurança adicionais — fora do âmbito GEO/SEO, referir
só se relevante para uma auditoria de segurança à parte.

## Prioridades, por esforço e impacto

| Item | Esforço | Porque importa |
|---|---|---|
| `hreflang` entre pt/en/es | baixo | condição para a expansão ES não canibalizar o pt |
| Corrigir `/contatos` → `/contactos` | baixo | mesmo erro de identidade que estamos a corrigir no Wikidata |
| Remover uma das duas páginas `pipedrive*clinicas` do sitemap | baixo | pára a auto-concorrência |
| Retirar `/blank` do sitemap | trivial | limpeza |
| Medir Core Web Vitals reais | precisa de chave ou GSC | decide se o peso de 1,76 MB é problema real ou cosmético |

Isto soma-se, não substitui, à lista já aberta com o Fábio (JSON-LD, meta description e cç no
inubia.pt, entidade Wikidata). Nenhum destes itens tem prazo definido; ficam registados aqui até
haver decisão sobre prioridade.

---
**Versão 1.0 (2026-09-17).**
