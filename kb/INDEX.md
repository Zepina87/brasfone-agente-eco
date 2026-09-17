# Base de conhecimento do Eco
**Origem:** extracção da auditoria ao repo `AgriciDaniel/claude-seo` (MIT), 2026-09-14, por ordem
de José. O repo não está instalado e não deve ser: traz um hook `PostToolUse` bloqueante em
`Edit|Write` que correria em todas as escritas da casa, e 25 skills globais, incompatíveis com o
âmbito "só no Eco". O que valia foi extraído para aqui, em PT-PT.

| Ficheiro | Serve para | Estado de verificação |
|---|---|---|
| `posicao-google.md` | posição oficial da Google, mitos que ela rejeita, teste Quem/Como/Porquê, piso de elegibilidade, fan-out | **fonte primária, lida por nós** |
| `crawlers-ia.md` | treino vs citabilidade, tabela dos 13 bots, os que ignoram robots.txt, como se mede | taxonomia de terceiro; **estado dos nossos domínios medido por nós** |
| `llmstxt-veredicto.md` | porque o llms.txt tem peso zero e o que isso muda na nossa fila | **afirmação central verificada por nós na fonte** |
| `citabilidade.md` | forma da passagem citável, 5 dimensões com peso, frescura, menções de marca | números de terceiro, **não verificados** |
| `superficies-ia.md` | AI Overviews vs AI Mode, fontes de citação por plataforma, o que declarar | números de terceiro, **não verificados** |
| `paginas-para-agentes.md` | árvore de acessibilidade, elementos interactivos reais, WebMCP e UCP | contexto, ainda não oferta |

## Regra de uso
Um facto marcado "não verificado" serve para desenhar método interno e NUNCA entra em peça de
cliente sem verificação na fonte original. Citar a nossa própria base de conhecimento é ecoar,
não verificar.

## Ferramentas que acompanham
- `../scripts/audita_geo.py` - auditoria técnica determinística de um domínio: crawlers por nome
  com três estados, llms.txt, JSON-LD, meta description, suspeita de render no cliente.
  Stdlib apenas, sem dependências.
- `../scripts/gera_jsonld.py` - gera Organization, Service e FAQPage com a entidade canónica
  fixada por José, e avisa quando uma resposta de FAQ está fora da janela de citabilidade.
  `--wikidata QID` acrescenta o `sameAs` para o Wikidata quando a entidade existir.
- `../scripts/audita_entidade.py` - vigia a entidade no Wikidata, nossa e dos concorrentes, com
  veredicto em quatro estados. Snapshot em `../baseline/entidade-*.json`.
- `../entidade/PACOTE-wikidata-inubia.md` - pacote preparado para criar as entidades Brasfone e
  Inubia, por terceiro e por ordem de José. Não criado.
- `dados/ai-robots.json` - cópia local da lista canónica de 175 bots (`ai-robots-txt/ai.robots.txt`,
  MIT). Actualizar só por `../scripts/actualiza_bots.sh`.
- Série temporal no Supabase (tabelas `geo_runs`, `geo_respostas`, `geo_citacoes`), atrás de
  `GEO_PERSIST=1`. Motor em `~/triggerdev-jobs/src/lib/geo/`.

## Revisão
Rever por trimestre. O guia de IA da Google é documento vivo e a taxonomia de crawlers muda quando
os donos publicam bots novos. Última verificação: 2026-09-14.
