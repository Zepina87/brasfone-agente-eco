# Estratégia GEO Brasfone/Inubia — v1.0 (2026-08-25)
**Dono:** José Pina (Head of AI) · **Executor:** O Eco (#27) · **Aprovações:** plano 2026-08-24, canal Trigger.dev 2026-08-25

## Objectivo
Quando um decisor português pergunta a um motor generativo "quem implementa Pipedrive em
Portugal", "quem faz consultoria de IA para PMEs" ou "qual o melhor CRM para o meu sector",
a resposta menciona a Inubia/Brasfone com factos correctos. Métrica: **share of voice** na
bateria congelada de 20 prompts SoV (+5 de exactidão de entidade), medida por motor, 2+
amostras, série temporal semanal. **Reportado em QUOTA RELATIVA (fatia do total de menções) com
o absoluto ao lado** (desde 2026-09-15): só a quota resiste a mudanças de comportamento do motor.

## Porque temos vantagem estrutural
1. **Platinum Partner Pipedrive** com página no marketplace oficial — os motores confiam no
   domínio pipedrive.com muito mais do que no nosso; é o nosso backlink GEO mais valioso.
2. O baseline informal (2026-08-25) já mostra o Sonar a citar a Brasfone como nº1 — não
   partimos do zero, partimos de defender e alargar.
3. ~~Site Wix expõe llms.txt + endpoint MCP automaticamente — diferenciador técnico raro.~~
   **Retirado 2026-09-15:** a Google declara na documentação oficial que o `llms.txt` não ajuda
   nem prejudica a visibilidade (verificado na fonte a 14-09). Não é vantagem. O que substitui
   este ponto: **nenhum concorrente português tem entidade no Wikidata** (medido 14-09), logo quem
   lá chegar primeiro, ligado ao Pipedrive Q24054211, fica com a única âncora de terceiro do mercado.

## As 4 fases

### Fase 0 — Baseline (FEITA 2026-08-25)
Auditoria técnica dos 2 domínios + primeira medição SoV (`baseline/sov-2026-08-25.json`,
150 chamadas, 0 erros). Leitura: **Sonar (pesquisa live)** Brasfone 15% / Inubia 10% /
SmartLinks 10% — lideramos por pouco. **GPT-5-mini e Gemini raw ≈0% para todo o mercado**:
nenhum parceiro PT está nos dados de treino, o terreno está por conquistar. Dois problemas
de entidade confirmados: o Gemini confunde a Brasfone com uma homónima brasileira de VoIP,
e "Inubia" colide com a inúbia (instrumento indígena) e Inúbia Paulista (município BR) —
a desambiguação da Fase 1 (JSON-LD, llms.txt, "em Portugal" explícito) não é cosmética,
é a condição de existência da marca nos motores.
Concorrentes medidos: SmartLinks (Premier), SoulSales, Neeaconsulting, Digital Xperience,
Priceless Consulting.

### Fase 1 — Entidade e fundações (semanas 1-2, esforço baixo, efeito composto)
**Reordenada 2026-09-15.** A entidade passou para o topo porque é condição de existência, não
optimização: "Inubia" no Wikidata devolve quatro entidades brasileiras e "Brasfone" não existe.
Nada do resto desta fase resolve isso. Estado a 15-09: **nenhum item aplicado desde 25-08**.
| Acção | Site | Nota |
|---|---|---|
| **Entidade Wikidata: Brasfone primeiro, Inubia depois, ligadas ao Pipedrive Q24054211 e com `P1889 different from` Inúbia Paulista** | grafo | ⚠ GATE: só por ordem de José e por terceiro (RFC de notoriedade em curso). Pacote em `entidade/PACOTE-wikidata-inubia.md` |
| Corrigir 59 erros "cç" na homepage do inubia.pt (eram "2 typos" a 25-08; medido 15-09) | inubia.pt | `ENTREGA-fase1-para-colar.md` |
| Marketplace Pipedrive: slug real é `inubia-brasfone-group` (200); corrigir onde apontava para `brasfone` (404) | ficheiros nossos | feito a 15-09 |
| Resolver inconsistência de entidade (Elite vs Platinum; "Inubia anteriormente Brasfone" vs "Inubia, marca do grupo Brasfone") | ambos | ⚠ GATE: José define a narrativa canónica primeiro |
| JSON-LD Organization + Service + FAQPage | inubia.pt | hoje tem ZERO structured data |
| ~~llms.txt manual e curado~~ opcional, fim da lista | inubia.pt | peso zero no Google (fonte oficial, 14-09) |
| Meta descriptions em todas as páginas-chave | ambos | homepages vazias hoje |
| Rever llms.txt auto do Wix (texto é editável via SEO Tools) | brasfone.pt | corrigir tier + narrativa |

### Fase 2 — Conteúdo citável (semanas 2-8)
Uma página por pergunta da bateria que hoje não respondemos, no formato que os motores citam:
pergunta como H1, resposta directa nos primeiros 60 palavras, estatísticas com fonte,
citação de perito (José), FAQ schema. Prioridade: A04 (tier de certificação — só nós podemos
responder), A05 (custos — ticket 4-6 k€ por acção, único conteúdo de preço honesto do mercado),
B01-B06 (consultoria de IA — espaço quase vazio em PT), C01-C06 (sectoriais, com prova social
APENAS de casos.md via fact-gate).
Pipeline por página: O Eco draft → fact-gate → ghost-check → José → publicação.

### Fase 3 — Autoridade externa (semanas 4-12, contínua)
1. Perfil marketplace Pipedrive optimizado (reviews de clientes reais pedidos pós-projecto).
2. Directórios PT relevantes com entidade consistente.
3. Imprensa/blogs sectoriais: 1 artigo citável por trimestre (dados originais nossos, ex.
   benchmarks anonimizados de implementações — só com aprovação José).
4. Flywheel Sombra: posts LinkedIn do José apontam às páginas GEO (LinkedIn é fonte frequente
   de citação do Sonar em PT).

### Fase 4 — Loop contínuo (a partir da semana 2)
Motor `geoShareOfVoice` em Trigger.dev (padrão bdrAnalyticsWeekly): cron semanal segunda 08:00
Europe/Lisbon → 200 chamadas via OpenRouter (4 motores desde 2026-09-17, ver decisão abaixo) →
agregado datado em repo → Claude lê e escreve o relatório mensal (Modo 4). Alerta imediato se:
SoV da marca cai >10 pontos num motor, ou um motor afirma facto FALSO sobre nós (categoria D).

## Custos (contas à vista)
- Medição: 200 chamadas/semana ≈ 340k tokens (3 motores originais) + a fatia do Claude Haiku
  4.5, medida por chamada real a 0,0006 USD ≈ cerca de €0,03/semana extra pelas 50 chamadas
  novas. Sonar $1/$1 por M tokens + taxa de pesquisa por pedido; GPT-5-mini $0,25/$2,00; Gemini
  3.7 Flash $0,38/$1,88; Claude Haiku 4.5 $1/$5 por M tokens → **< €3,5/mês** em tokens; a taxa
  de pesquisa do Sonar (50 pedidos/semana) é o item dominante, na ordem de €2-4/mês. Total
  estimado **€3,5-7,5/mês** ⚠ a confirmar na primeira factura OpenRouter com os 4 motores.
- Conteúdo e relatórios: tokens Claude da sessão, sem custo novo.
- Zero SaaS novo: sem Profound/Semrush/Otterly — o motor próprio faz o mesmo para este âmbito.

## O que NÃO fazemos
- Prometer rankings ou prazos de citação garantidos.
- **Vender GEO como disciplina nova com tácticas próprias e resultado garantido** (2026-09-15). O
  C-SEO Bench (NeurIPS 2025) mediu que a maioria dos métodos de optimização para motores
  conversacionais é inefectiva e que o SEO tradicional foi cerca de 7,6 vezes mais eficaz. A Google
  diz que "continua a ser SEO". A nossa posição defensável é medir presença e trabalhar fundamentos.
- **Ler share of voice em absoluto sem a quota ao lado.** Entre 25-08 e 09-09 todas as marcas
  dobraram em absoluto no Sonar; em quota nós caímos de 52,7% para 46,5% da fatia total. Quando
  todas sobem na mesma proporção, o motor mudou, não nós.
- **Migrar para `inubia.com` sem a entidade criada antes e sem redireccionamentos permanentes página
  a página.** O `.pt` é hoje o único sinal geográfico que nos separa de Inúbia Paulista.
- Publicar prova social fora de casos.md (fact-gate é bloqueante).
- Gerar conteúdo em massa sem ghost-check: slop indexado não tem rollback.
- Tocar em Amperia ou ES nesta fase.

## Decisões registadas
| Data | Decisão | Quem |
|---|---|---|
| 2026-08-24 | Fase 1 = PT + Inubia; Brasfone entidade-mãe; Amperia fora | José |
| 2026-08-24 | Medição em motores não-Claude autorizada (análise só Claude) | José |
| 2026-08-25 | Canal do loop: híbrido Trigger.dev (motor) + Claude (leitura); n8n fora | José |
| 2026-08-25 | Narrativa canónica: tier **Platinum**; relação **"Inubia, marca do grupo Brasfone"** (nunca "anteriormente Brasfone") | José |
| pendente | Chaves nativas dos 4 motores p/ fidelidade máxima (ou manter OpenRouter) | José |
| **2026-09-17** | **REVOGA PARCIALMENTE a decisão de 24-08.** Claude entra na bateria como motor MEDIDO, não só analista ("é vital"). A missão do Eco já o nomeava desde 25-08 ("ChatGPT, Perplexity, Gemini, Copilot e Claude"); a bateria só testava 3, lacuna aberta 3 semanas. `claude-haiku-4.5`, para comparar tamanho com tamanho contra os outros raw (`gpt-5-mini`, `gemini-3.7-flash`), nunca o Sonnet. Papel de análise/veredicto continua só Claude; medir a própria presença do Claude é coisa distinta e agora autorizada. Falta o Copilot, sem API aberta equivalente: limitação registada. | José |
| 2026-09-15 | Métrica passa a quota relativa com absoluto ao lado; job cloud refeito (motor puro + série no Supabase atrás de `GEO_PERSIST`) | Cérebro, plano aprovado por José |
| 2026-09-15 | Entidade Wikidata sobe para o topo da Fase 1; `llms.txt` desce para opcional | Cérebro, com fonte Google e medição própria |
| pendente | Deploy do job v1.1 (leva 9 ficheiros BDR alheios não commitados) | José |
| pendente | Ordem para criar entidade Wikidata, por terceiro | José |
| pendente | Estado real de `inubia.com` e data de migração | Fábio + José |

---
**v1.1 (2026-09-15):** deltas sobre a v1.0, não reescrita. O que mudou está marcado em linha com a
data. Ver `MASTER-PROMPT-ECO.md` v2.0 para a doutrina operacional.
