# Auditoria do repo externo `AgriciDaniel/claude-seo` para O Eco
**Data:** 2026-09-14 · **Pedido de José:** avaliar encaixe, âmbito restrito ao Eco
**Veredicto:** ADOPÇÃO SELECTIVA POR EXTRACÇÃO. Não instalar o plugin nem correr `install.sh`.

## 1. Identidade do alvo
| Item | Valor verificado |
|---|---|
| Repo | github.com/AgriciDaniel/claude-seo, MIT, v2.3.1 |
| Vivo? | Sim. Último commit 2026-09-11 (3 dias antes desta auditoria) |
| Dimensão | 7,7 MB, 25 skills, 18 sub-agentes, 57 scripts Python, 8 extensões MCP opcionais |
| Telemetria | Nenhuma declarada no PRIVACY.md ("No telemetry, analytics, or usage tracking"). Sem código de envio encontrado |

## 2. Segurança: a auditoria automática falhou, os achados são falsos positivos
`audit-externo.sh` saiu com 1 (cc-audit 306 erros, gitleaks 1 fuga), 359 ficheiros lidos.
Li os achados, como manda a regra da casa. Nenhum é verdadeiro positivo:

- **cc-audit MW-006 "Browser Data Theft" (134 críticos):** dispara por regex sobre PROSA, não sobre
  código. Acerta em frases de markdown como "Chrome UX Report History API" (API pública do Google
  para Core Web Vitals) e num comentário de `scripts/url_safety.py` onde a palavra "cookies" aparece
  a descrever protecção contra SSRF. Grep dirigido a caminhos reais de perfis de browser
  (`Login Data`, `Local State`, `~/Library/Application Support/Google/Chrome`, keychain,
  `browser_cookie`) devolve ZERO ocorrências em todo o repo.
- **gitleaks:** a "chave" é `opr_live_SECRET123` em `tests/test_keywordseverywhere_api.py:145`, uma
  fixture cujo propósito é afirmar `assert "opr_live_SECRET123" not in str(result)`. É um teste de
  que as chaves são redigidas dos erros. Sinal de higiene, não de fuga.
- **`curl | bash`:** só dentro de strings de documentação a explicar a instalação ao utilizador.
  Nenhum executado.

**Conclusão de segurança: repo limpo.** O que o barra não é malícia, é arquitectura.

## 3. Riscos reais, que não são de segurança
1. **O hook é global e bloqueante.** `hooks/hooks.json` regista `PostToolUse` com matcher
   `Edit|Write` e `validate-schema.py` devolve exit 2 para BLOQUEAR. Instalado como plugin, passa a
   correr em TODAS as escritas de ficheiro de TODA a casa, não só nas do Eco. Um agente a escrever
   uma nota de CRM ou um deck ficaria sujeito a um validador de JSON-LD de terceiro.
2. **"Só no Eco" é incompatível com a forma de instalação.** `install.sh` copia 25 skills para
   `~/.claude/skills/seo*` e 18 agentes para `~/.claude/agents/`, todos globais. Não há modo de
   instalação por agente. Instalar isto é dar 25 skills novas a todos os agentes da casa.
3. **Dependências pesadas para o que se aproveita:** playwright, weasyprint, matplotlib, numpy,
   google-ads, google-analytics-data. Instalar tudo para usar 3 scripts não se justifica.
4. **Registo anglófono e SEO-cêntrico.** PT-PT, prova social, tratamento formal e os portões da casa
   não vêm no pacote; teriam de ser reimpostos por cima.

## 4. Sobreposição funcional: o que o Eco já faz melhor
O activo central do Eco NÃO existe neste repo e não é substituível por ele.

| Capacidade | Eco | claude-seo |
|---|---|---|
| Share of voice medido contra concorrentes nomeados, série temporal, bateria congelada, scoring determinístico por regex | SIM, é o núcleo | NÃO |
| Citabilidade de uma página nossa (qualidades da página) | fraco | SIM, é o núcleo |
| Monitor de regressão on-page (`seo-drift`) | NÃO | SIM, e não colide com o Modo 2 |
| Tracking de menções em LLM | motor próprio a custo de OpenRouter | só via SaaS pago (Profound, DataForSEO) |

São agentes complementares, não concorrentes. O Eco mede o que os motores dizem de nós; o
claude-seo avalia se a nossa página merece ser citada. Nenhum dos dois faz o trabalho do outro.

## 5. O que vale a pena levar, e o que isso corrige no Eco
Cinco achados. Os dois primeiros são correcções a erros vivos do Eco, não melhorias opcionais.

### 5.1 A auditoria de 25-08 nunca nomeou um crawler (CORRECÇÃO)
O Eco escreveu "robots OK (IA permitida)" para as duas superfícies. Grep a todo o `o-eco/`:
zero ocorrências de GPTBot, OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot ou
Google-Extended. O resultado calhou estar certo (verifiquei os robots hoje: ambos os sites têm
`User-agent: *` permissivo), mas foi asserção sem medição, e mistura duas capacidades distintas:

| Afirmação | Bot que a suporta | Bot que NÃO a suporta |
|---|---|---|
| Citável no ChatGPT Search | `OAI-SearchBot` | `GPTBot` |
| Disponível para treino da OpenAI | `GPTBot` | `OAI-SearchBot` |
| Citável na pesquisa do Claude | `Claude-SearchBot` | `ClaudeBot` |
| Elegível para Google Search e AI Overviews | `Googlebot` | `Google-Extended` |

`Google-Extended` governa treino e grounding do Gemini, NUNCA inclusão em AI Overviews, que são
servidas do índice do `Googlebot`. Um relatório que confunda isto diz ao cliente que ele está
invisível quando não está.

### 5.2 O llms.txt não é alavanca no Google (CORRECÇÃO DE PRIORIDADE)
Verificado por mim na fonte primária, não no repo:
developers.google.com/search/docs/fundamentals/ai-optimization-guide diz textualmente
"You don't need to create new machine readable files, AI text files, markup, or Markdown to appear
in Google Search" e, sobre o llms.txt, "Doing so will neither harm nor help your site's visibility".
O mesmo documento diz que "optimizing for generative AI search is optimizing for the search
experience, and thus still SEO".

Consequência para o Eco: `fase1-diffs/inubia-llms.txt` e `fase1-diffs/llms-brasfone.txt` têm
prioridade quase nula para o Google. Medido hoje: inubia.pt/llms.txt dá 404, brasfone.pt/llms.txt
dá 200 (auto do Wix).

**Mas o Eco tinha razão em querer mexer no do Wix, por outra razão.** O llms.txt auto do Wix diz
"Elite" e "anteriormente Brasfone", e a entidade canónica fixada por si a 25-08 é
"Platinum Partner Pipedrive" e "Inubia, marca do grupo Brasfone". Isso é inconsistência de entidade
numa superfície pública, e consistência de entidade CONTA. Corrige-se por ser falso, não por ser
alavanca de ranking. A distinção muda a ordem do roadmap, não a decisão de corrigir.

### 5.3 Critérios de citabilidade quantificados (ADIÇÃO)
Passagem óptima de 134 a 167 palavras; ~44% das citações saem dos primeiros 30% da página;
conteúdo com menos de 3 meses tem ~3x mais probabilidade de ser citado e 6+ meses de estagnação
perde elegibilidade (SE Ranking, estudo de 1,3M citações). O Modo 3 do Eco tem os números do
Aggarwal KDD 2024 (estatísticas +25,9%, peritos +27,8%, fontes +24,9%) mas não tem a forma
operacional. Os dois conjuntos somam-se.

### 5.4 AI Mode e AI Overviews são duas superfícies (ADIÇÃO)
Chegam à mesma conclusão ~86% das vezes mas citam os mesmos URLs só 13,7% das vezes (Ahrefs, 540K
pares de query). AI Overviews correlaciona com ranking clássico; AI Mode puxa de um conjunto mais
largo onde frescura e autoridade de entidade pesam mais que a posição. O Eco mede hoje um só
Google. Marcar como limitação declarada até haver forma de medir os dois.

### 5.5 Três scripts isolados que resolvem lacunas conhecidas (ADIÇÃO OPCIONAL)
`schema_generate.py` (inubia.pt tem zero JSON-LD), `consistency_check.py` (consistência de entidade,
exactamente o problema "Elite") e `render_page.py` (verificação de SSR, e os crawlers de IA não
executam JavaScript). Copiam-se isolados para `o-eco/scripts/`, com as suas dependências, sem
instalar o resto.

## 6. Recomendação
1. **NÃO** correr `install.sh`, **NÃO** instalar como plugin. Motivo: hook global bloqueante e 25
   skills globais, incompatíveis com o âmbito "só no Eco" que definiu.
2. **SIM** a extrair os 5 achados acima para `MASTER-PROMPT-ECO.md`, com a taxonomia de crawlers e
   a nota do llms.txt como correcções datadas, não como reescrita (proibido reescrever o prompt
   inteiro: context collapse).
3. O clone fica no scratchpad e desaparece com a sessão. Se quiser guardar como referência de
   leitura, diga e passo para `o-eco/referencias/` sem o tornar executável.
4. Alterar o master prompt de um agente é HITL: o delta está proposto em
   `DELTA-ECO-crawlers-llmstxt-20260914.md` e aguarda ordem sua.

## 7. Registo de decisão
| Afirmação | Fonte |
|---|---|
| llms.txt não ajuda nem prejudica no Google | Fonte primária Google, lida hoje por WebFetch |
| robots.txt de inubia.pt e www.brasfone.pt permitem IA | curl directo, hoje, `User-agent: *` permissivo |
| inubia.pt sem llms.txt (404), brasfone.pt com (200) | curl directo, hoje |
| Eco nunca nomeou um crawler | grep a todo o `o-eco/`, zero ocorrências |
| Estatísticas de citabilidade (134-167 palavras, 44%, 3x recência) | claude-seo citando SE Ranking. NÃO verificado na fonte primária, marcar como a validar antes de entrar em peça de cliente |
| 13,7% de sobreposição AI Mode vs AI Overviews | claude-seo citando Ahrefs. NÃO verificado na fonte primária, idem |
| Repo sem telemetria e sem código malicioso | PRIVACY.md + grep dirigido + leitura dos 306 achados do cc-audit |
