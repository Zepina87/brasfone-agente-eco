# Posição oficial da Google sobre GEO e IA na pesquisa
**Fonte primária:** developers.google.com/search/docs/fundamentals/ai-optimization-guide
**Estado:** VERIFICADO POR NÓS na fonte primária a 2026-09-14 (WebFetch). Re-verificar trimestralmente.
**Origem da síntese:** extraída de `AgriciDaniel/claude-seo` (MIT) e confirmada na fonte.

## A frase que muda o enquadramento comercial

> "From Google Search's perspective, optimizing for generative AI search is optimizing for the
> search experience, and thus still SEO."

Consequência para nós: GEO apresenta-se como SEO aplicado às superfícies de IA, nunca como
disciplina nova que substitui o SEO. Quem vende "GEO" como coisa separada está a vender uma
etiqueta. Nós vendemos medição de presença, que é coisa diferente e verificável.

## Piso de elegibilidade
Uma página só aparece em qualquer funcionalidade de IA se estiver indexada e elegível para ser
mostrada com snippet na pesquisa normal. **Não existe índice de IA separado.** Duas técnicas
assentam por cima: RAG com grounding (recupera páginas indexadas e gera resposta com links) e
query fan-out (dispara sub-perguntas relacionadas e puxa mais resultados antes de responder).

O fan-out tem uma consequência prática: a página não é recuperada só pela pergunta que o
utilizador fez, mas pelas sub-perguntas que o motor inventou à volta dela. Cobrir a vizinhança
semântica de um tema vale mais do que acertar numa frase exacta.

## Mitos que a Google rejeita explicitamente
Serve de portão a qualquer recomendação de comunidade. Se uma sugestão bate contra esta lista,
sinaliza-se a contradição em vez de a repetir.

| A Google diz que NÃO é preciso | Nota |
|---|---|
| Criar `llms.txt` ou ficheiros de texto para IA | ver `llmstxt-veredicto.md` |
| Cortar conteúdo em pedaços pequenos para a IA | o "chunking" é do lado do motor, não nosso |
| Reescrever conteúdo com fraseados especiais ou cauda longa para IA | |
| Perseguir menções inautênticas em blogues, fóruns e vídeos | ver nota de tensão abaixo |
| Sobre-investir em dados estruturados só por causa da IA | JSON-LD serve para outras coisas, e essas mantêm-se |

O que a Google diz que CONTA: conteúdo único, não genérico, de primeira mão. O exemplo do próprio
documento contrasta "7 dicas para quem compra casa pela primeira vez" (genérico) com "porque
dispensámos a inspecção e poupámos dinheiro: por dentro da conduta de esgoto" (vivido).

**Tensão a manter à vista, não a resolver por decreto:** a Google rejeita a perseguição de menções
inautênticas, e ao mesmo tempo há estudos de terceiros que medem correlação forte entre menções de
marca e citação em IA (ver `citabilidade.md`). As duas coisas convivem: menções ganhas por
trabalho real contam, menções fabricadas são spam. Nunca recomendar fabricação de menções.

## Teste Quem / Como / Porquê (E-E-A-T operacional)
Fonte: developers.google.com/search/docs/fundamentals/creating-helpful-content

- **Quem** criou: assinatura onde o leitor a espera; página de autor obrigatória em YMYL.
- **Como** foi criado: sobretudo em conteúdo assistido por IA, revelar o processo onde o leitor
  razoavelmente perguntaria.
- **Porquê** existe: para ajudar pessoas, não para apanhar cliques de pesquisa.

YMYL (dinheiro, saúde, segurança) pesa mais, e desde Setembro de 2025 inclui temas políticos e
sociais. Sinais de alarme que a própria Google lista para auto-auditoria: escrever para um número
de palavras alvo (não existe número), entrar em nichos sem competência só por tráfego, falsificar
frescura de datas, e produzir conteúdo em massa para fingir actualização.

## Conteúdo gerado por IA
Fonte: developers.google.com/search/blog/2023/02/google-search-and-ai-content
Conteúdo gerado por IA é aceitável se cumprir as Search Essentials. Torna-se spam quando serve
para escalar páginas de baixo valor. Isto valida o nosso ghost-check: não é preciosismo estético,
é a fronteira declarada entre conteúdo aceitável e abuso de escala.

## Ferramentas de terceiros (documento companheiro, 2026-06-05)
Fonte: developers.google.com/search/docs/fundamentals/third-party-seo
Nenhuma ferramenta garante posições; ferramentas de terceiros não têm acesso aos dados internos de
ranking da Google; a Search Console é a fonte autoritativa de primeira parte.

Consequência directa para o Eco: qualquer pontuação que produzamos é heurística nossa, nunca sinal
interno da Google, e diz-se isso no relatório. Isto reforça a Regra Absoluta 5 (sem promessas de
ranking) e dá-lhe fonte externa em vez de ser só política da casa.

---
**Versão 1.0 (2026-09-14).** Criado a partir da auditoria do repo `claude-seo`.
