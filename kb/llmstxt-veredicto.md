# llms.txt: o veredicto, e o que ele muda na nossa fila de trabalho
**Estado:** afirmação central VERIFICADA POR NÓS na fonte primária a 2026-09-14. Evidência de
apoio extraída de `AgriciDaniel/claude-seo` (MIT), não re-verificada estudo a estudo.

## O que a Google diz, nas palavras dela
Guia oficial de optimização para IA (developers.google.com/search/docs/fundamentals/ai-optimization-guide):

> "You don't need to create new machine readable files, AI text files, markup, or Markdown to
> appear in Google Search"

E especificamente sobre estes ficheiros:

> "Doing so will neither harm nor help your site's visibility"

Não ajuda nem prejudica. Peso zero. Isto não é leitura de terceiros: foi lido por nós na página.

## Evidência de apoio (terceiros, não re-verificada por nós)
| Fonte | Data | O que disse |
|---|---|---|
| John Mueller, Google | 2026 | chamou "beco sem saída" ao caso de uso de descoberta |
| John Mueller, Google | 2025 | "nenhum sistema de IA usa hoje o llms.txt"; comparou-o às meta keywords |
| Gary Illyes, Google | Jul 2025 | a Google não tem planos de suportar llms.txt |
| SE Ranking, estudo de 300 mil domínios | Nov 2025 | dos 50 domínios mais citados por IA, só UM tinha llms.txt |
| OtterlyAI, auditoria a logs de servidor | 2025 | 0,1% do tráfego de bots de IA procura o llms.txt (84 de 62.100 pedidos) |
| Anthropic, Stripe, Cloudflare, NVIDIA | 2024-2025 | todos publicam llms.txt; nenhum declarou que os seus crawlers consomem o de terceiros |

## Onde o ficheiro serve mesmo
Em sites de documentação técnica, consumido por agentes de programação (Cursor, Cline, Claude
Code) ao carregar documentação de bibliotecas. Para um site de negócio que não vende ferramentas
de programação, o valor é puramente defensivo: custo zero, opção de futuro se algum fornecedor o
vier a adoptar.

## O que isto muda na fila do Eco
1. **`fase1-diffs/inubia-llms.txt` desce de prioridade.** Medido a 2026-09-14: `inubia.pt/llms.txt`
   dá 404. Continua a valer a pena criar, por opcionalidade a custo zero, mas vai para o fundo da
   lista e nunca é apresentado como alavanca. A prioridade real do `inubia.pt` é outra: meta
   description vazia e zero JSON-LD (medido no mesmo dia).
2. **`fase1-diffs/llms-brasfone.txt` mantém-se, por razão diferente da original.** Medido:
   `www.brasfone.pt/llms.txt` responde 200, gerado automaticamente pelo Wix, e afirma "Elite" e
   "anteriormente Brasfone". A entidade canónica fixada por José a 2026-08-25 é "Platinum Partner
   Pipedrive" e "Inubia, marca do grupo Brasfone". Corrige-se porque está FALSO numa superfície
   pública, não porque dê posições. A consistência de entidade conta; o ficheiro em si não.

A distinção importa: muda a ordem do roadmap, não a decisão de corrigir.

## Como se reporta, sempre
Reportar presença e boa formação. Nunca atribuir peso de citação ou ranking no Google. Se um
cliente pedir para gerar um, entrega-se com a ressalva à vista: a Google ignora-o, nenhum
fornecedor grande confirmou que o consome, e serve para opcionalidade, não para citação.

## Quando este ficheiro deixa de valer
Reabrir quando: um sistema grande de pesquisa por IA documentar que o consome; a OtterlyAI ou a
SE Ranking publicarem seguimento com inflexão medida no tráfego ao ficheiro; ou Mueller e Illyes
retirarem o que disseram. Enquanto nada disso acontecer, o veredicto mantém-se.

---
**Versão 1.0 (2026-09-14).**
