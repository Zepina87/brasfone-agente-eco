# Citabilidade: a forma que faz uma passagem ser citada
**Estado:** critérios e pesos extraídos de `AgriciDaniel/claude-seo` (MIT). Os números de estudos
(SE Ranking, Ahrefs) NÃO foram verificados por nós nas fontes originais: servem para desenhar como
escrevemos, não entram em peça de cliente sem verificação e nunca com promessa de resultado.
Os números do Aggarwal et al. (KDD 2024) já vinham da doutrina do Eco e mantêm-se.

## AVISO QUE VEM PRIMEIRO: há evidência publicada CONTRA as tácticas deste ficheiro
**Acrescentado 2026-09-14, verificado por nós.** O C-SEO Bench (NeurIPS 2025, Datasets and
Benchmarks Track; arXiv 2506.11097; código em `parameterlab/c-seo-bench`) testou 9 métodos de
optimização para motores conversacionais em 6 domínios e concluiu que **a maioria é largamente
inefectiva, e que vários têm impacto NEGATIVO no posicionamento do documento**, o contrário do
que prometem. Mediu ainda que a linha de base de SEO tradicional foi cerca de **7,6 vezes mais
efectiva** do que o melhor método conversacional testado no domínio do retalho.

Isto está em tensão directa com o paper fundador (Aggarwal et al., KDD 2024) que dá a base das
tácticas abaixo. **Não se resolve escolhendo o que nos convém.** Como se opera:

1. **As tácticas deste ficheiro são hipóteses a testar, não boas práticas estabelecidas.** Entram
   em trabalho nosso e em recomendação a cliente com essa moldura, nunca como garantia.
2. **Quando houver conflito entre "truque de GEO" e SEO bem feito, ganha o SEO.** Três fontes
   independentes convergem: a Google diz que isto continua a ser SEO (`posicao-google.md`), o
   C-SEO Bench mede que o SEO tradicional bate os métodos conversacionais, e a própria Google
   rejeita explicitamente o fraseado especial para IA.
3. **Isto protege-nos comercialmente.** Quem vender GEO como disciplina nova, com tácticas
   próprias e resultado garantido, está a vender contra a evidência publicada. A nossa posição
   defensável é outra: medimos presença, que ninguém contesta ser mensurável, e trabalhamos
   fundamentos, que a evidência suporta.

## As duas metades do problema
O Eco mede **o que os motores dizem de nós** (share of voice, bateria congelada). Este ficheiro
trata da outra metade: **se a nossa página merece ser citada**. Uma coisa não substitui a outra.
Melhorar a forma sem medir é fé; medir sem melhorar a forma é diagnóstico sem tratamento.

## Cinco dimensões, com peso
| Dimensão | Peso | O que é |
|---|---|---|
| Citabilidade | 25% | a passagem pode ser extraída e citada sem contexto à volta |
| Legibilidade estrutural | 20% | hierarquia de títulos, perguntas como cabeçalhos, tabelas, listas |
| Conteúdo multi-modal | 15% | texto com imagens, vídeo, gráficos, ferramentas interactivas |
| Autoridade e sinais de marca | 20% | autoria, datas, fontes citadas, presença de entidade |
| Acessibilidade técnica | 20% | render no servidor, crawlers permitidos |

A pontuação é heurística nossa, nunca sinal interno de um motor. A própria Google diz que
ferramentas de terceiros não têm acesso aos dados de ranking dela. Diz-se isso no relatório.

## 1. Citabilidade
**Forma da passagem: 134 a 167 palavras**, auto-contida, extraível sem o resto da página.
**Cerca de 44% das citações saem dos primeiros 30% da página** (SE Ranking): a conclusão vai ao
topo, nunca ao fundo. Resposta directa nas primeiras 40 a 60 palavras de cada secção.

Sinais fortes: frases citáveis com factos e números concretos; blocos de resposta fechados;
afirmações atribuídas a fonte identificada; definições no padrão "X é..." ou "X refere-se a...";
dados próprios que não existem em mais lado nenhum.
Sinais fracos: generalidades; opinião sem prova; conclusões enterradas; zero números.

Isto soma-se às tácticas que o Eco já tinha do Aggarwal et al. (KDD 2024): estatísticas +25,9%,
citações de peritos +27,8%, fontes explícitas +24,9%. Aquilo diz o QUE pôr; isto diz a FORMA.

## 2. Legibilidade estrutural
Hierarquia limpa de h1 para h2 para h3; cabeçalhos em forma de pergunta, porque casam com a
pergunta real do utilizador; parágrafos de 2 a 4 frases; tabelas para comparação; listas para
passos. A parede de texto é o pior formato possível para ser citado.

## 3. Multi-modal
Conteúdo com elementos multi-modais é seleccionado cerca de 156% mais (terceiro, não verificado).
Texto com imagens relevantes, vídeo, infografias, calculadoras.

## 4. Autoridade, e a alavanca que quase ninguém usa
Assinatura com credenciais, data de publicação e de última actualização, fontes primárias
citadas, citações de peritos atribuídas, presença de entidade na Wikipédia e Wikidata.

**A frescura é alavanca de primeira ordem.** Conteúdo com menos de 3 meses é citado cerca de 3
vezes mais; a partir de 6 meses parado, perde elegibilidade de citação (SE Ranking, estudo de 1,3
milhões de citações). Consequência prática: **um programa agendado de refrescamento das páginas
que já temos vale mais do que escrever uma página nova.** É a recomendação de maior alavancagem
deste ficheiro e a que custa menos.

Cuidado com a fronteira: refrescar é actualizar o conteúdo a sério. Mexer na data sem mexer no
conteúdo é falsificar frescura, e a Google lista isso como sinal de alarme.

**Menções de marca correlacionam mais com citação em IA do que backlinks** (Ahrefs, estudo de 75
mil marcas, terceiro não verificado): YouTube cerca de 0,737, Reddit alto, Wikipédia alto,
LinkedIn moderado, Domain Rating cerca de 0,266. Ler com a ressalva do `posicao-google.md`:
menções ganhas contam, menções fabricadas são spam e a Google rejeita-as explicitamente.
Correlação também não é causa, e um estudo de vendedor de ferramenta tem interesse no resultado.

## 5. Acessibilidade técnica
**Os crawlers de IA não executam JavaScript.** Render no servidor é condição, não preferência. Um
site que monta o conteúdo no cliente está invisível para eles, por muito bem escrito que esteja.
Verificação rápida: `scripts/audita_geo.py` assinala a suspeita quando há pouco texto visível para
muito HTML. Confirmação a sério faz-se comparando o HTML em bruto com a página renderizada.

Mais os crawlers permitidos por nome, em `crawlers-ia.md`.

## Vitórias rápidas, por ordem de custo
1. Definição "O que é X?" nas primeiras 60 palavras.
2. Blocos de resposta auto-contidos de 134 a 167 palavras.
3. Cabeçalhos h2 e h3 em forma de pergunta.
4. Estatísticas com fonte à vista.
5. Datas de publicação e de actualização visíveis.
6. Programa agendado de refrescamento do que já existe.
7. Schema `Person` para autores, `Organization` para a entidade.

## O que NÃO fazer, porque a Google rejeita
Cortar conteúdo em pedaços para a IA, reescrever com fraseados especiais, perseguir menções
fabricadas, sobre-investir em dados estruturados só por causa da IA. Ver `posicao-google.md`.

---
**v1.1 (2026-09-14):** acrescentado o aviso do C-SEO Bench, que contradiz parte das tácticas
aqui listadas. Origem: análise de landscape que José mandou avaliar; a afirmação foi verificada
por nós na fonte antes de entrar.
**Versão 1.0 (2026-09-14).**
