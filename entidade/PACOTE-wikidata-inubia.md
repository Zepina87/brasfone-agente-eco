# Pacote de entidade Wikidata · Inubia e Brasfone
**Data:** 2026-09-15 · **Estado:** PREPARADO, NÃO CRIADO. Criar é acto público e irreversível à
vista de terceiros; só por ordem expressa de José, e não pela própria empresa.

## Porque este pacote existe
Medido a 2026-09-14 (`scripts/audita_entidade.py`, snapshot em `baseline/entidade-2026-09-14.json`):
- "Inubia" no Wikidata devolve quatro entidades, todas brasileiras: Q10303405 (a inúbia, instrumento),
  Q1761742 e Q22064719 (Inúbia Paulista, município e povoação), Q29554265 (página de desambiguação).
- "Brasfone" não existe.
- Nenhum concorrente português tem entidade. O Pipedrive tem: **Q24054211**.

Quando um modelo procura quem somos, encontra o Brasil. Isto explica a confusão do Gemini com uma
homónima brasileira e o zero dos motores sem pesquisa em directo. Não se resolve com conteúdo no
site: resolve-se com entidade própria, ligada a uma âncora que já é notória.

## Ordem de criação
1. **Brasfone primeiro** (entidade-mãe, sem colisão de nome). 2. **Inubia depois**, com
`P749 parent organization` a apontar para a Brasfone. Criar a Inubia sem a mãe é criar uma
entidade órfã com nome ambíguo, que é o pior dos dois mundos.

## Quem cria, e a armadilha com relógio
O critério de notoriedade do Wikidata (`Wikidata:Notability`) não exige imprensa: basta ser
entidade claramente identificável, descritível com referências sérias e públicas. Registo comercial
e NIF servem. **Mas há uma consulta em curso (`Requests_for_comment/Notability_policy_reform`,
2026) para apertar o critério e proibir explicitamente que a própria empresa crie o seu item.**
Verificado a 14-09 por pesquisa; reverificar o estado da RFC no dia em que se avançar.
Consequência: quem cria não pode ser a Inubia nem a Brasfone. Terceiro, com as referências já
prontas no momento da criação, porque item sem referência é apagado.

## Item 1 · Brasfone

| Campo | Valor | Fonte |
|---|---|---|
| Label pt / en / es | Brasfone | site |
| Descrição pt | empresa portuguesa de soluções tecnológicas e CRM, sediada em Faro, Platinum Partner Pipedrive | site + marketplace |
| Descrição en | Portuguese technology and CRM company based in Faro, Pipedrive Platinum Partner | idem |
| P31 instance of | Q4830453 business | |
| P17 country | Q45 Portugal | |
| P159 headquarters location | **Q3344655** Faro (cidade, P17=Q45) | JSON-LD existente (8005-528). **A v1.0 deste pacote dizia Q207431, que é Louis van Gaal:** apanhado a 16-09 ao verificar cada QID na API antes de gerar o QuickStatements. Nenhum QID entra sem verificação |
| P856 official website | https://www.brasfone.pt | |
| P1454 legal form | **Q115399164** sociedade por quotas (Lda.), confirmado por José 16-09 e QID verificado na API | publicacoes.mj.pt |
| P3608 / NIF | **PT506079031**, fornecido por José 16-09; dígito de controlo validado (mod 11), prefixo 5 = pessoa colectiva | publicacoes.mj.pt |
| P452 industry | Q11661 information technology | |
| P1327 partner in business or sport | **Q24054211 Pipedrive** | marketplace, slug `inubia-brasfone-group` |
| P4264 LinkedIn company ID | brasfone | https://www.linkedin.com/company/brasfone/ |
| P571 inception | ⚠ a confirmar | registo comercial |

## Item 2 · Inubia

| Campo | Valor | Fonte |
|---|---|---|
| Label pt / en / es | Inubia | site |
| Descrição pt | marca do grupo Brasfone para implementação de CRM Pipedrive e automação comercial em Portugal; não confundir com Inúbia Paulista | site |
| Descrição en | Portuguese CRM implementation brand of the Brasfone group; not to be confused with Inúbia Paulista, Brazil | idem |
| P31 instance of | **Q167270** marca comercial. José confirmou 16-09: a Inubia é marca registada dentro do grupo Brasfone, sem pessoa jurídica própria. Não leva NIF próprio; o NIF é o da Brasfone via P749 | |
| P17 country | Q45 Portugal | |
| P749 parent organization | → item Brasfone (criado no passo 1) | |
| P856 official website | https://inubia.pt | |
| P1327 partner in business or sport | Q24054211 Pipedrive | marketplace |
| P4264 LinkedIn company ID | inubia-pt | https://www.linkedin.com/company/inubia-pt (medido no HTML 15-09) |
| P154 logo image | só se o logo for carregado no Commons com licença compatível; senão omitir | |
| P1889 different from | Q1761742 Inúbia Paulista · Q10303405 inúbia | **é a desambiguação explícita; não omitir** |

A descrição em pt e en leva o "não confundir com" de propósito: é a única linha que um modelo lê
quando escolhe entre homónimos.

## Referências a anexar em cada statement
1. publicacoes.mj.pt: razão social, NIF, sede (quando José fornecer o NIF).
2. Site oficial (brasfone.pt, inubia.pt), páginas de contactos e de quem somos.
3. Página de parceiro no marketplace Pipedrive: `https://www.pipedrive.com/en/marketplace/partners/inubia-brasfone-group`
   (responde 200 a 15-09; é a referência de terceiro mais forte que temos).
4. Páginas LinkedIn das duas.

## Depois de existirem os QIDs
- `python3 scripts/gera_jsonld.py organization inubia --wikidata QID_INUBIA --wikidata-mae QID_BRASFONE`
  produz o JSON-LD com `sameAs` para o Wikidata. É o sinal de desambiguação mais forte que um site
  pode dar.
- `scripts/audita_entidade.py` deve passar de NOME OCUPADO para TALVEZ NOSSA na Inubia e de AUSENTE
  para TALVEZ NOSSA na Brasfone. Se não passar, algo ficou mal ligado.
- Actualizar `kb/crawlers-ia.md` não é preciso; actualizar `ESTRATEGIA-GEO.md` sim (Fase 1 fechada).

## Ligação à migração para inubia.com
Se a migração avançar, a entidade tem de existir ANTES e o `P856` muda depois, com o `.pt` a
redireccionar permanentemente. Trocar de domínio sem entidade é trocar o único sinal geográfico
(`.pt`) por nada, numa marca cujo nome no grafo aponta para o Brasil.

---
**Versão 1.0 (2026-09-15).**
