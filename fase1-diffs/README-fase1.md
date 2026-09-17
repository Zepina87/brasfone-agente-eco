# Fase 1 — diffs técnicos (2026-08-25)
Narrativa canónica (José 2026-08-25): tier **Platinum** · **"Inubia, marca do grupo Brasfone"**.
Nada disto publica sozinho: cada item aplica-se pela pessoa/via indicada e verifica-se depois.

| # | Item | Onde aplicar | Ficheiro |
|---|---|---|---|
| 1 | Substituir o texto do llms.txt auto do Wix (hoje diz "Elite Partner" e "Inubia (anteriormente Brasfone)", ambos ERRADOS) | Wix → SEO Tools → llms.txt (secção MCP do Wix mantém-se, é gerada) | `llms-brasfone.txt` |
| 2 | Criar llms.txt no WordPress | inubia.pt raiz (plugin ou ficheiro) | `inubia-llms.txt` |
| 3 | JSON-LD Organization + Service | `<head>` de inubia.pt | `inubia-jsonld.html` (2 placeholders ⚠ a preencher: logo e LinkedIn) |
| 4 | Meta descriptions homepages | Wix SEO + WP SEO plugin | abaixo |
| 5 | **Erros ortográficos na homepage inubia.pt.** A 25-08 contámos 2 ("Integracção", "Mediacção"). **Medido a 15-09: são 59 ocorrências em 35 palavras distintas, todas o mesmo padrão "cç" onde o PT-PT escreve "ç"** (implementacção, documentacção, formacção, automacções, comunicacção...). Não é gralha, é erro sistémico de quem escreveu o site. Vinte dias depois, zero corrigidas. Tabela completa em `ENTREGA-fase1-para-colar.md` | WP editor, procurar e substituir "cç" → "ç" página a página, com revisão a olho | — |
| 6 | ~~FAQ da homepage carrega por JS → invisível a crawlers~~ **Correcção 15-09: os 8 pares pergunta/resposta ESTÃO no HTML servido** (classes `inh-faq-q`/`inh-faq-a`). A nota de 25-08 estava errada ou o site mudou. Schema FAQPage gerado a partir do texto visível, com o "cç" corrigido | `<head>` de inubia.pt, DEPOIS de corrigir o "cç" no texto visível (o schema tem de espelhar a página) | `inubia-faqpage.html` · `faq-homepage-corrigido.json` |
| 7 | **Slug do marketplace Pipedrive.** Todos os ficheiros desta pasta apontavam para `partners/brasfone`, que dá 404. O slug real é `partners/inubia-brasfone-group` e responde 200 (verificado 15-09; o próprio Sonar o cita). Corrigido nos 3 ficheiros | — | `llms-brasfone.txt` · `inubia-llms.txt` · `inubia-jsonld.html` |

## Meta descriptions propostas
**brasfone.pt:** "Brasfone: Parceiro Oficial Platinum do Pipedrive em Portugal. Implementação de CRM, comunicações cloud, produtividade e cibersegurança para empresas portuguesas. Sede em Faro."
**inubia.pt:** "Inubia, marca do grupo Brasfone: implementação de CRM Pipedrive, automação de vendas e RevOps para PMEs em Portugal. Especialistas em saúde, imobiliário, crédito e agências. Consultoria gratuita de 30 minutos."

## Verificação pós-aplicação (O Eco corre `eco audita`)
curl aos 2 llms.txt · validator.schema.org ao JSON-LD · view-source às meta descriptions · grep aos typos.
