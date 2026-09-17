# Crawlers de IA: treino e citabilidade não são a mesma coisa
**Estado:** taxonomia extraída de `AgriciDaniel/claude-seo` (MIT) a 2026-09-14, com as fontes
primárias listadas no fim. Estado dos nossos domínios MEDIDO por nós (ver `../baseline/`).
**Porque existe:** a auditoria do Eco de 2026-08-25 escreveu "robots OK (IA permitida)" para as
duas superfícies da casa sem nomear um único crawler. Era asserção sem medição, e juntava numa
linha duas capacidades que são distintas.

## A distinção que muda relatórios

Cada afirmação só pode ser sustentada pelo bot que a governa. Trocar os bots faz o relatório
dizer a um cliente que ele está invisível quando não está.

| Afirmação que se quer fazer | Bot que a suporta | Bot que NÃO a suporta |
|---|---|---|
| Citável no ChatGPT Search | `OAI-SearchBot` | `GPTBot` |
| Disponível para treino da OpenAI | `GPTBot` | `OAI-SearchBot` |
| Citável na pesquisa do Claude | `Claude-SearchBot` | `ClaudeBot` |
| Disponível para treino da Anthropic | `ClaudeBot` | `Claude-SearchBot` |
| Elegível para Google Search, AI Overviews e AI Mode | `Googlebot` | `Google-Extended` |
| Utilizável para treino e grounding do Gemini e Vertex | `Google-Extended` | `Googlebot` |
| Descoberto por Siri, Spotlight e Safari | `Applebot` | `Applebot-Extended` |
| Utilizável para treino da Apple Intelligence | `Applebot-Extended` | `Applebot` |

Os três erros que se cometem mais:
1. **`Google-Extended` lido como sinal de Google Search.** Não é. As AI Overviews e o AI Mode são
   servidos do índice do `Googlebot`. Bloquear `Google-Extended` recusa treino e grounding do
   Gemini e não tira uma única aparição em AI Overviews.
2. **`GPTBot` lido como sinal de ChatGPT.** Não é. Um site que bloqueia `GPTBot` e permite
   `OAI-SearchBot` continua plenamente citável no ChatGPT Search.
3. **`Applebot-Extended` lido como crawler.** Não é sequer um crawler que vá buscar páginas: é um
   sinal de opt-out de treino aplicado a conteúdo que o `Applebot` já trouxe.

## Tabela completa

| Crawler | Dono | Governa | Obedece ao robots.txt? |
|---|---|---|---|
| `OAI-SearchBot` | OpenAI | citabilidade no ChatGPT Search | sim |
| `Claude-SearchBot` | Anthropic | citabilidade na pesquisa do Claude | sim |
| `PerplexityBot` | Perplexity | citabilidade na Perplexity | sim |
| `Googlebot` | Google | Google Search, AI Overviews, AI Mode | sim |
| `Bingbot` | Microsoft | Bing e Copilot | sim |
| `Applebot` | Apple | Siri, Spotlight, Safari | sim |
| `GPTBot` | OpenAI | treino de modelos | sim |
| `ClaudeBot` | Anthropic | treino de modelos | sim |
| `Google-Extended` | Google | treino e grounding Gemini e Vertex | sim |
| `Applebot-Extended` | Apple | opt-out de treino Apple Intelligence | sim |
| `CCBot` | Common Crawl | dados de treino | sim |
| `Bytespider` | ByteDance | treino de modelos | **NÃO** |
| `cohere-ai` | Cohere | respostas a pedidos do utilizador | **por esclarecer** |

**`anthropic-ai` foi removido de propósito.** O artigo de suporte actual da Anthropic documenta
apenas `ClaudeBot`, `Claude-User` e `Claude-SearchBot`. Um bot que não está na documentação do
dono não entra na nossa tabela como palpite.

## Os que ignoram o robots.txt por desenho
`ChatGPT-User`, `Claude-User`, `Perplexity-User`, `Google-Agent` (navegação agêntica),
`Google-NotebookLM`, `Google Messages`. O `Bytespider` da ByteDance também não obedece, e esse
não é sequer accionado por utilizador: é rastreio para treino que ignora a directiva. São accionados por um utilizador, não são rastreio automático, e por isso o
robots.txt não os trava. Quem os quiser travar tem de o fazer no servidor. Nunca prometer a um
cliente que o robots.txt bloqueia estes.

**Web Bot Auth (RFC 9421)** está a emergir como forma de um bot se autenticar por cabeçalho
`Signature-Agent` mais directório de chaves (já usado pelo `Google-Agent`). A verificação por DNS
inverso continua a ser o método de recurso.

## Recomendação da casa
Permitir sempre os de citabilidade: `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`,
`Googlebot`, `Bingbot`, `Applebot`. Os de treino (`GPTBot`, `ClaudeBot`, `Google-Extended`,
`CCBot`, `Applebot-Extended`) permitem-se ou bloqueiam-se por decisão de licenciamento do
proprietário do site, nunca por argumento de visibilidade. Se um cliente quiser recusar treino
sem perder citação, isso é possível e é exactamente esta a conversa a ter.

## Como se mede, nesta casa
`python3 scripts/audita_geo.py <dominio> [--json saida.json]`

Determinístico, sem dependências externas, agrupa correctamente o robots.txt e resolve o
allow/disallow por correspondência mais longa. Devolve três estados por bot, e a diferença entre
o segundo e o terceiro é o ponto todo:
- `PERMITIDO` ou `BLOQUEADO`: lido de um robots.txt que respondeu 200.
- `PERMITIDO (inferido)`: não existe robots.txt (404). Pela norma tudo é permitido, mas isto é
  inferência, não leitura.
- `NAO VERIFICADO`: o robots.txt não respondeu. **Nunca se lê como permitido.** Ausência de
  medição não é facto. Esta distinção é a razão de ser do script.

## Estado medido das nossas superfícies (2026-09-14)
`inubia.pt` e `www.brasfone.pt`: ambos com `User-agent: *` permissivo, portanto os 13 bots da
tabela estão permitidos, citabilidade e treino incluídos. A conclusão de Agosto estava certa; a
forma de lá chegar é que não servia. Bruto em `../baseline/geo-tecnico-2026-09-14.json`.

## Fontes primárias
- OpenAI: platform.openai.com/docs/bots
- Google: developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
  (referência canónica migrada para developers.google.com/crawling em 2025-11-20; os ficheiros de
  gamas de IP passaram para `/crawling/ipranges/` e o `googlebot.json` deu lugar a
  `common-crawlers.json`)
- Anthropic: support.anthropic.com, artigo sobre rastreio e bloqueio do crawler
- Apple: support.apple.com/en-us/119829

---
**v1.1 (2026-09-14):** TRÊS CORRECÇÕES a erros da v1.0, apanhadas ao cruzar com a lista
comunitária `ai-robots-txt/ai.robots.txt` (175 bots, 68 contribuidores). A v1.0 dizia que o
`Bytespider` obedece ao robots.txt: **não obedece**. Dizia que o `cohere-ai` obedece: está **por
esclarecer**, e afirmar certeza onde não há é o mesmo erro de fundo que este ficheiro existe para
corrigir. E faltava o `Perplexity-User` na lista dos que ignoram a directiva. A taxonomia da v1.0
veio do `claude-seo`, que errou nos dois primeiros; uma lista mantida por 68 pessoas ganha a uma
tabela escrita por um.
**Versão 1.0 (2026-09-14).**
