# As superfícies de IA não são uma só, e citam de forma diferente
**Estado:** números de terceiros extraídos de `AgriciDaniel/claude-seo` (MIT), NÃO verificados por
nós nas fontes originais. Servem para desenhar método interno. **Não entram em peça de cliente sem
verificação**, e nunca com promessa de resultado.

## Duas máquinas de citação dentro da Google
AI Overviews e AI Mode chegam à mesma conclusão cerca de 86% das vezes, mas citam os mesmos URL
apenas cerca de 13,7% das vezes (Ahrefs, 540 mil pares de perguntas). São superfícies distintas:

| | AI Overviews | AI Mode |
|---|---|---|
| Relação com o ranking clássico | forte: cita páginas que já posicionam bem | fraca: conjunto muito mais largo |
| Domínios citados por pergunta | poucos | cerca de 9 (Ahrefs) |
| O que pesa mais | SEO tradicional e optimização de passagem | frescura, autoridade de entidade, passagens citáveis para lá da posição 5 |

Em Maio de 2026 a Google juntou as duas na mesma experiência de utilização (pergunta, depois AI
Overview, depois seguimento em AI Mode). **A experiência é uma, as máquinas de citação continuam
duas.** Pontuar as duas separadamente.

Números de contexto, todos de terceiros: as AI Overviews cobrem cerca de metade das perguntas
(medição de terceiros, varia por país); 92% das citações em AI Overviews vêm de páginas no top 10,
mas 47% vêm de páginas abaixo da posição 5, o que mostra lógica de selecção diferente da do
ranking puro.

## Por plataforma
| Plataforma | De onde cita mais | Onde se trabalha |
|---|---|---|
| Google AI Overviews | páginas que já posicionam | SEO clássico mais optimização de passagem |
| Google AI Mode | conjunto largo, Gemini 2.5 adaptado | frescura, entidade, passagens citáveis |
| ChatGPT | Wikipédia (47,9%), Reddit (11,3%) | presença de entidade, fontes autoritativas |
| Perplexity | Reddit (46,7%), Wikipédia | validação por comunidade, discussões |
| Bing Copilot | índice do Bing | SEO no Bing, IndexNow |

**Só 11% dos domínios são citados ao mesmo tempo pelo ChatGPT e pelas AI Overviews para a mesma
pergunta.** É por isto que a bateria do Eco mede motores separados e nunca agrega tudo numa
percentagem só.

## O que isto obriga a declarar nos nossos relatórios
A bateria congelada mede hoje três motores via OpenRouter (`perplexity/sonar`,
`openai/gpt-5-mini`, `google/gemini-3.7-flash`). Duas limitações a declarar sempre, não uma:
1. **Já registada:** modelo em bruto sem pesquisa mede presença nos dados de treino, não o que o
   utilizador vê no produto com pesquisa ligada. Só o Sonar faz pesquisa em directo.
2. **Nova:** medimos um só Google. Não separamos AI Overviews de AI Mode, que citam de forma
   diferente. Nenhuma conclusão nossa sobre "a Google" pode ser apresentada como cobrindo as duas.

## Superfícies que deixaram de ser só texto
O AI Mode passou a ser superfície de reserva e compra (voos com alertas de preço em mais de 180
países, hotéis por parceiros integrados). Nada disto é alteração documentada de ranking, mas muda
o que um cliente de turismo ou hotelaria deve verificar. Para nós, hoje, é contexto, não acção.

A Google acrescentou ainda "Preferred Sources", em que um utilizador escolhe um domínio e o torna
mais provável nas notícias dele. **É preferência por utilizador, não sinal geral de ranking.**
Nunca prometer subida geral a partir disto. Há também distintivos de "muito citado" ganhos por
reportagem original, e "Community Perspectives" que eleva conteúdo de Reddit e fóruns.

**Não existe ficheiro de opt-out específico para IA.** A aparição em AI Overviews e AI Mode
governa-se pelas directivas normais de pré-visualização e indexação: `nosnippet`, `data-nosnippet`,
`max-snippet`, `noindex`. Isto é distinto do controlo dos crawlers de IA de terceiros no
robots.txt, e confundir as duas coisas dá conselho errado.

---
**Versão 1.0 (2026-09-14).**
