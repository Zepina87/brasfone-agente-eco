# Delta proposto ao MASTER-PROMPT-ECO.md
**Origem:** auditoria de `AgriciDaniel/claude-seo`, 2026-09-14 (ver `AUDITORIA-claude-seo-20260914.md`)
**Estado:** PROPOSTA. Alterar master prompt de outro agente é HITL (Regra Absoluta 6 do Cérebro).
**Método:** acrescentar, nunca reescrever o ficheiro (ACE: deltas, não substituição).

## D1. Modo 1 (AUDITORIA), substituir a linha dos crawlers
Onde hoje se lê "robots.txt (crawlers de IA permitidos?)", passar a:

> robots.txt verificado POR NOME DE BOT, com treino e citabilidade reportados em linhas separadas.
> Nunca escrever "IA permitida" sem a lista. Citabilidade: `OAI-SearchBot` (ChatGPT Search),
> `Claude-SearchBot` (pesquisa do Claude), `PerplexityBot`, `Googlebot` (Google Search e
> AI Overviews). Treino: `GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`, `Applebot-Extended`.
> `Google-Extended` governa treino e grounding do Gemini e NUNCA elegibilidade para AI Overviews,
> que saem do índice do `Googlebot`. Bloquear treino não tira citabilidade; confundir os dois faz
> o relatório dizer a um cliente que ele está invisível quando não está.
> Fetchers accionados por utilizador (`ChatGPT-User`, `Claude-User`, `Google-Agent`,
> `Google-NotebookLM`) ignoram o robots.txt por desenho: não se bloqueiam aí, só no servidor.

## D2. Modo 1 e ESTADO INICIAL, nota sobre llms.txt
Acrescentar:

> **llms.txt não é alavanca de citação no Google (verificado na fonte primária, 2026-09-14).**
> O guia de AI optimization da Google diz "You don't need to create new machine readable files,
> AI text files, markup, or Markdown to appear in Google Search" e, sobre estes ficheiros,
> "Doing so will neither harm nor help your site's visibility". Reportar presença, atribuir peso
> ZERO a ranking ou citação no Google. Pode servir outros sistemas, e diz-se isso sem prometer.
> O mesmo documento fixa que "optimizing for generative AI search is optimizing for the search
> experience, and thus still SEO": enquadrar achados GEO como SEO aplicado a superfícies de IA,
> nunca como disciplina separada, e nunca vender GEO como coisa nova que substitui SEO.
> **Consequência para a fila de trabalho:** `fase1-diffs/inubia-llms.txt` desce de prioridade.
> O `fase1-diffs/llms-brasfone.txt` MANTÉM-SE, por razão diferente da original: o llms.txt auto do
> Wix afirma "Elite" e "anteriormente Brasfone", contra a entidade canónica fixada por José a
> 2026-08-25 ("Platinum Partner Pipedrive", "Inubia, marca do grupo Brasfone"). Corrige-se por ser
> falso numa superfície pública, não por render ranking.

## D3. Modo 3 (CONTEÚDO GEO), acrescentar a forma operacional
Acrescentar às tácticas existentes (Aggarwal KDD 2024, que se mantêm):

> Forma da passagem citável: blocos auto-contidos de 134 a 167 palavras, resposta directa nas
> primeiras 40 a 60 palavras da secção, cabeçalhos em forma de pergunta. ~44% das citações saem dos
> primeiros 30% da página: a conclusão vai ao topo, nunca ao fundo. Recência é alavanca de primeira
> ordem, com conteúdo abaixo de 3 meses cerca de 3x mais citado e 6+ meses de estagnação a perder
> elegibilidade: um programa de refrescamento agendado vale mais que uma página nova.
> ⚠ Estes números vêm de estudo de terceiro (SE Ranking) citado por `claude-seo`, NÃO verificados
> por nós na fonte primária. Servem para desenhar a nossa forma de escrever; não entram em peça de
> cliente sem verificação, e nunca com promessa de resultado.

## D4. Modo 2 e GOTCHAS, duas superfícies Google
Acrescentar aos GOTCHAS:

> AI Overviews e AI Mode são duas superfícies de citação distintas: concordam na conclusão cerca de
> 86% das vezes mas citam os mesmos URLs só cerca de 13,7% (Ahrefs, 540K pares; terceiro, não
> verificado por nós). AI Overviews segue de perto o ranking clássico; AI Mode puxa de um conjunto
> mais largo onde frescura e autoridade de entidade pesam mais que a posição. A bateria mede hoje
> um só Google (`google/gemini-3.7-flash` via OpenRouter): declarar isso como limitação em todos os
> relatórios, ao lado da limitação já registada de que raw sem search não é o produto que o
> utilizador vê.

## D5. Ferramentas, opcional e só a pedido
Não instalar o `claude-seo`. Se e quando fizerem falta, copiar isolados para `o-eco/scripts/`:
`schema_generate.py` (inubia.pt tem zero JSON-LD), `consistency_check.py` (consistência de entidade)
e `render_page.py` (verificação de SSR; os crawlers de IA não executam JavaScript). Cada um traz as
suas dependências e nenhum traz hooks.

## O que NÃO se propõe
Nada que toque na bateria congelada, nos aliases, no scoring por regex, no âmbito Portugal/Inubia
ou nas regras absolutas. Nenhum prompt muda. A série temporal fica intacta.
