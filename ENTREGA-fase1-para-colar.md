# Fase 1 do Eco, pronta a colar
**Data:** 2026-09-15 · **Para:** quem tiver acesso ao WordPress do inubia.pt e ao painel do Wix do brasfone.pt
**Regra:** nada disto publica sozinho. Cada bloco cola-se à mão, e no fim corre-se a verificação.
**Estado a 15-09:** o diagnóstico é de 25 de Agosto. Vinte dias depois, nenhum item foi aplicado.

## Ordem recomendada
1. Erros ortográficos do inubia.pt (é o que mais custa à credibilidade e é procurar e substituir)
2. Meta description do inubia.pt
3. JSON-LD Organization + Service no inubia.pt
4. JSON-LD FAQPage no inubia.pt (só depois do ponto 1, porque o schema tem de espelhar o texto visível)
5. llms.txt do brasfone.pt no Wix (corrige "Elite" e "anteriormente Brasfone")
6. Opcional e no fim: llms.txt no inubia.pt

## 1. Erros ortográficos no inubia.pt · 59 ocorrências, 35 palavras
Medido no HTML servido da homepage a 2026-09-15. Padrão único: **"cç" onde o PT-PT escreve "ç"**.
No editor do WordPress, procurar `cç` e substituir por `ç`, página a página, com revisão a olho
(não há palavra portuguesa que leve "cç"; a substituição cega é segura, mas confirmar não custa).

| Vezes | Está | Deve estar |
|---|---|---|
| 5 | Integracção | Integração |
| 5 | implementacção | implementação |
| 4 | documentacção | documentação |
| 3 | Integracções | Integrações |
| 3 | Mediacção | Mediação |
| 3 | comunicacção | comunicação |
| 3 | integracção | integração |
| 3 | formacção | formação |
| 2 | Automatizacção | Automatização |
| 2 | Ligacção | Ligação |
| 2 | automacções | automações |
| 1 cada | Operacções, simulacção, Normalizacção, Organizacção, operacção, colaboracção, aprovacção, Padronizacção, aplicacções, Sincronizacção, Validacção, monitorizacção, Recomendacção, Satisfacção, operacções, faturacção, implementacções, integracções, eliminacção, criacção, organizacção, mediacção, recomendacção, Informacções | o mesmo, sem o "c" |

Porque importa para o Eco: os motores citam texto com erro ou descartam a fonte. Uma FAQ com
"implementacção" três vezes é uma FAQ que um modelo prefere não citar.

## 2. Meta descriptions
**inubia.pt (hoje VAZIA, medido 15-09):**
```
Inubia, marca do grupo Brasfone: implementação de CRM Pipedrive, automação de vendas e RevOps para PMEs em Portugal. Especialistas em saúde, imobiliário, crédito e agências. Consultoria gratuita de 30 minutos.
```
**brasfone.pt:** já tem uma, diferente da proposta de Agosto ("Implementamos soluções tecnológicas
que garantem que o seu negócio nunca pára..."). Está preenchida e é aceitável. Recomendação: manter,
a não ser que se queira o "Platinum Partner Pipedrive" logo na meta, e nesse caso a proposta de
Agosto está no `fase1-diffs/README-fase1.md`. Não é prioridade.

## 3. JSON-LD Organization + Service no inubia.pt
Ficheiro pronto, sem placeholders: `fase1-diffs/inubia-jsonld.html`. Cola-se no `<head>` via
plugin de SEO (Rank Math ou Yoast, secção de schema personalizado) ou no tema.
Preenchido a 15-09 com valores medidos: logo `https://inubia.pt/wp/wp-content/uploads/2026/05/inubia-logo.png`,
LinkedIn `https://www.linkedin.com/company/inubia-pt` (a Inubia tem página própria), marketplace
`https://www.pipedrive.com/en/marketplace/partners/inubia-brasfone-group` (o slug antigo dava 404).
Depois de colar: validar em `validator.schema.org` colando o URL da homepage.

## 4. JSON-LD FAQPage no inubia.pt
Ficheiro pronto: `fase1-diffs/inubia-faqpage.html`, gerado a partir dos 8 pares pergunta e resposta
que ESTÃO no HTML servido da homepage, já com o "cç" corrigido. **Só se cola depois do ponto 1**,
porque o schema tem de espelhar o texto visível, e hoje o texto visível tem os erros.

Duas notas para quem decidir sobre o conteúdo, não bloqueiam a colagem:
- As 8 respostas têm entre 31 e 39 palavras. A janela de citação que a doutrina do Eco adoptou é
  134 a 167 palavras por bloco auto-contido. São FAQ curtas, boas para leitura humana, fracas para
  citação. Reescrever é trabalho da Fase 2, não desta entrega.
- A pergunta 5 afirma "aumento de 40% na produtividade comercial e 45% em ganhos de receita nos
  primeiros 6 meses". O benchmark da casa é "+40% de contas geridas pela mesma equipa, sem cliente
  nomeado". **O "45% em ganhos de receita" não está na prova social canónica.** Passa o fact-gate
  porque não nomeia cliente, mas é um número público sem fonte registada. Decisão de José: manter
  com fonte, ou retirar.

## 5. llms.txt do brasfone.pt (Wix)
Ficheiro: `fase1-diffs/llms-brasfone.txt`. No Wix: Dashboard, SEO Tools, llms.txt (a secção MCP
gerada pelo Wix mantém-se).
**Porquê, com precisão:** o ficheiro automático do Wix afirma um tier de parceria que não é o
nosso (diz "Elite" onde a entidade canónica diz **Platinum Partner Pipedrive**) e descreve a
Inubia como "anteriormente Brasfone", quando a relação canónica fixada por José a 25-08 é
"Inubia, marca do grupo Brasfone". **Corrige-se por estar errado numa superfície pública, não por
render posições:** a Google declara na documentação oficial que o `llms.txt` não ajuda nem
prejudica a visibilidade. A consistência de entidade é que conta.

## 6. llms.txt no inubia.pt · opcional, fim da lista
Ficheiro: `fase1-diffs/inubia-llms.txt`. Peso zero no Google (verificado na fonte a 14-09). Serve
de opcionalidade a custo zero para outros sistemas. Se for feito, é o último item; se não for,
não se perde nada mensurável.

## Verificação depois de colar
```
python3 agents/o-eco/scripts/audita_geo.py inubia.pt www.brasfone.pt
```
O que tem de mudar no output do inubia.pt: `meta description` deixa de dizer VAZIA; `JSON-LD`
passa a listar Organization, Service e FAQPage. E `curl -s https://inubia.pt/ | grep -c "cç"` tem
de dar 0.

## O que NÃO está nesta entrega, e porquê
- Entidade no Wikidata: acto público, prepara-se em `entidade/PACOTE-wikidata-inubia.md`, cria-se
  só por ordem de José e por terceiro.
- Migração para inubia.com: o domínio não responde (medido 14-09) e a decisão é do Fábio e de José.
- As 14 páginas GEO da Fase 2: passaram o fact-gate uma a uma, aguardam veredicto editorial na
  tarefa ClickUp `86cb9jz8v`.

---
**Versão 1.0 (2026-09-15).**
