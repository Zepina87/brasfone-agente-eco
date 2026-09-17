# Páginas para agentes: a onda a seguir à citação
**Estado:** extraído de `AgriciDaniel/claude-seo` (MIT), que por sua vez sintetiza o guia de IA da
Google e um artigo do web.dev. Não verificado por nós na fonte. **Contexto, ainda não oferta.**

## Porque isto entra na doutrina do Eco agora
O GEO que medimos hoje é sobre ser citado numa resposta. A camada seguinte são agentes que agem
em nome do utilizador: procuram, comparam, marcam, compram. Aí o que conta deixa de ser só a
qualidade do texto e passa a ser se a página é **operável por uma máquina**.

Não é oferta nossa hoje e não se vende. Fica registado para não sermos apanhados de surpresa, e
porque a verificação é barata quando já se está a auditar um site.

## Os três canais por onde um agente lê uma página
1. **Captura de ecrã mais modelo de visão:** interpreta hierarquia visual e proeminência dos
   botões. Lento e caro em tokens.
2. **HTML em bruto:** aninhamento, identificadores, classes, atributos de dados.
3. **Árvore de acessibilidade:** a destilação semântica do próprio navegador (papéis, nomes,
   estados). É o sinal mais limpo dos três.

Os agentes modernos combinam os três. **Optimizar a árvore de acessibilidade é o movimento de
maior alavancagem:** se ela estiver partida, nenhum polimento visual salva a página.

Há aqui uma simetria que vale a pena dizer a um cliente: isto é acessibilidade. O trabalho que
torna um site utilizável por quem usa leitor de ecrã é o mesmo que o torna operável por agentes.
Quem fez o trabalho de acessibilidade a sério já está preparado e não sabe.

## Lista de verificação
**Elementos interactivos a sério.** `<button>` para acções, `<a href>` para navegação, `<input>`,
`<select>`, `<textarea>` para formulários. Um `<div onclick>` aparece na árvore de acessibilidade
sem papel nenhum, e os agentes saltam-no. Quando não é possível usar a etiqueta real, dar
`role="button"`, `tabindex="0"` e tratar `Enter` e `Espaço`.

**Etiquetas associadas.** Todo o campo precisa de `<label for>` ou `aria-label`. Sem isso, o
agente lê um campo sem propósito, ou seja, um vazio.

**Tamanho do alvo.** As análises visuais descartam elementos interactivos com menos de cerca de 8
píxeis quadrados de área desobstruída. Os mínimos de acessibilidade (24 por 24 no WCAG AA, 44 por
44 nas normas da Apple) passam esse portão por construção. Qualquer clicável abaixo de 24 por 24
é candidato a falhar com agentes.

## WebMCP e UCP
**WebMCP**: norma proposta para interacção directa entre site e agente. Estado por resolver
(ensaio de origem no Chrome 149). **UCP** (Universal Commerce Protocol): norma aberta de comércio
com Shopify, Etsy, Wayfair, Target e Walmart, com implementação de referência confirmada pela
Google no AI Mode. Ambas em movimento. Não construir sobre elas hoje; reavaliar por trimestre.

---
**Versão 1.0 (2026-09-14).**
