# O Eco a medir superfícies próprias: análise para decisão
**Data:** 2026-09-14 · **Pedido de José:** avaliar repositórios para o Eco medir as superfícies da
Google e da Meta ligadas por MCP na cloud, e passar de agente de GEO a agente de SEO completo.
**Estado:** parte 1 verificada por nós na fonte primária. Parte 2 (inventário de repositórios)
em baixo, da pesquisa.

## 1. A descoberta que muda o desenho, e que não estava no pedido

**A Google lançou relatórios de desempenho de IA generativa no Search Console.** Anúncio em Junho
de 2026, implementação concluída em todos os sites do mundo a **31 de Agosto de 2026**, ou seja há
duas semanas. Fonte: Search Central Blog, `developers.google.com/search/blog/2026/06/gen-ai-performance-reports`
e a ajuda do produto, `support.google.com/webmasters/answer/16984139`.

Isto importa mais do que qualquer servidor MCP desta análise. O Eco mede hoje presença em IA por
**amostragem estocástica**: 25 perguntas, 3 motores, 2 amostras, e infere share of voice. A Google
passou a dar-nos **impressões reais e contadas** das nossas páginas dentro das funcionalidades de
IA dela. É a diferença entre sondagem e recenseamento, e encaixa na Regra Absoluta 1 do Eco, que
diz que a aritmética não é nossa.

**O que o relatório dá e o que não dá, verificado na ajuda do produto:**
- Dá **só impressões**. Não dá cliques nem posição.
- **Junta AI Overviews e AI Mode numa métrica só.** Não os separa, apesar de citarem URL
  diferentes em cerca de 86% dos casos (ver `kb/superficies-ia.md`).
- Filtra por página, país, dispositivo e data (fuso do Pacífico).
- Limite de 1000 linhas, dados recentes preliminares, exclui experiências do Search Labs.
- Um site que tenha optado por sair das funcionalidades de IA fica de fora do relatório.

## 2. O obstáculo, e é sério

**Estes dados não estão na API do Search Console.** Verificado na referência da API
(`developers.google.com/webmaster-tools/v1/searchanalytics/query`): os valores permitidos no campo
`type` são `web`, `image`, `video`, `news`, `googleNews` e `discover`. Nenhum de IA generativa. A
documentação do relatório novo também não menciona acesso por API.

Consequência directa e desagradável: **um servidor MCP de Search Console, por melhor que seja, não
lê hoje as impressões em IA.** Lê o desempenho normal de pesquisa, que é valioso, mas não a
métrica nova que é a mais interessante para o Eco.

**Ressalva honesta, a testar e não a assumir:** a dimensão `searchAppearance` só revela os valores
disponíveis quando se corre uma consulta agrupada por ela. A documentação não lista nenhum valor
de IA, mas a lista completa não está documentada. **Primeiro teste a fazer no dia em que ligarmos
o Search Console:** consulta agrupada por `searchAppearance` para ver o que lá está mesmo. Até
esse teste, a posição correcta é que não temos acesso programático, não que seja impossível.

## 3. O que isto implica para a arquitectura do Eco

Três camadas de medição, e só a primeira é que o Eco tem hoje:

| Camada | Mede | Fonte | Estado |
|---|---|---|---|
| Eco externo | o que os motores dizem de nós | bateria congelada via OpenRouter | **existe**, é o núcleo |
| Eco próprio | o que a Google conta que nos aconteceu | Search Console (API para pesquisa; interface para IA) | **por ligar** |
| Consequência | o que as visitas fizeram | GA4 | **por ligar** |

A terceira camada é a que responde à pergunta que um cliente faz a seguir, e que hoje não sabemos
responder: "isso traduziu-se em quê?". Sem ela, medimos eco e paramos antes do negócio.

## 4. Nota de âmbito sobre a Meta, a dar a José em vez de a esconder
Ver secção própria em baixo, depois do inventário.

## 5. Inventário de servidores MCP para as superfícies Google
**Estrelas, licença e data do último push CONFIRMADOS POR NÓS** na API do GitHub a 2026-09-14,
não aceites da pesquisa. A licença foi verificada porque decide se podemos usar, e um dos
candidatos caiu exactamente aí.

| Repositório | Oficial? | Licença | Estrelas | Último push |
|---|---|---|---|---|
| `googleanalytics/google-analytics-mcp` | **Google** | Apache-2.0 | 3185 | 2026-08-07 |
| `googleads/google-ads-mcp` | **Google** | Apache-2.0 | 946 | 2026-09-10 |
| `ahonn/mcp-server-gsc` | não | **NENHUMA** | 264 | 2026-09-04 |
| `surendranb/google-analytics-mcp` | não | MIT | 242 | 2026-09-10 |
| `surendranb/google-search-console-mcp` | não | MIT | 38 | 2026-08-22 |
| `acamolese/google-search-console-mcp` | não | MIT | 8 | 2026-08-22 |

### GA4: decidido, e sem discussão
**`googleanalytics/google-analytics-mcp`**, da própria Google, Apache-2.0, com tracção a sério.
Cobre `run_report`, `run_funnel_report`, `run_realtime_report` e os metadados de conta, tudo
leitura. Autentica por credenciais padrão da aplicação com âmbito `analytics.readonly`, e aceita
conta de serviço. Só funciona localmente por stdio, não tem versão hospedada. A própria Google
marca-o como experimental, o que significa que a interface pode mudar, não que seja inseguro.

### Search Console: não há oficial, e o mais popular está fora
**Não existe MCP oficial da Google para o Search Console.** Entre os de comunidade:

- `ahonn/mcp-server-gsc` é o mais popular e o mais maduro no tempo, **e está fora**. Verificámos
  na API do GitHub: não declara licença nenhuma. Sem licença explícita, o direito de autor por
  omissão reserva todos os direitos, e usar isto numa empresa é assumir risco jurídico por
  conveniência técnica. Só entra se o autor publicar uma licença.
- **`surendranb/google-search-console-mcp` (MIT, 38 estrelas)** passa a ser a escolha. Do mesmo
  autor do MCP de GA4 com 242 estrelas, o que dá consistência de estilo entre os dois.
- `acamolese/google-search-console-mcp` (MIT, 8 estrelas) tem mais funcionalidades no papel, 17
  ferramentas de leitura, incluindo lacunas de CTR e canibalização. É jovem e sem validação de
  comunidade. Candidato a segunda opinião, não a fundação.

**Nenhum destes resolve o problema da secção 2:** o desempenho em IA generativa não está na API,
portanto nenhum MCP o lê.

### Google Business Profile e Google Ads: não, por agora
O Business Profile não tem oficial, os candidatos têm 2 estrelas, e o acesso à API exige aprovação
da Google com fila reportada em semanas. O Ads tem oficial e bom (Apache-2.0, 946 estrelas, suporta
remoto), mas **escreve além de ler**: gere campanhas. Para medir presença não é preciso, e dar a um
agente a capacidade de mexer em campanhas para ler números é trocar risco por nada. Reabre-se se e
quando houver dor concreta.

## 6. "MCP Cloud": é uma categoria, não um produto
Não existe produto com esse nome da Anthropic, da Cloudflare ou de outro fornecedor. O termo
circula em artigos para dizer "MCP hospedado". A escolha real é entre três modelos, e a diferença
entre eles é **quem guarda as nossas credenciais**:

| Modelo | Quem guarda o token | Exemplos |
|---|---|---|
| Conector nativo | o fornecedor (Google, Meta) e a Anthropic | os conectores que já tem no Claude |
| Auto-hospedado | nós | Cloudflare Workers |
| Plataforma gerida | **um terceiro** | Composio, Zapier MCP, Smithery, Pipedream, Klavis |

**A terceira coluna é a que não se usa aqui.** A casa já teve cinco chaves expostas e continua com
rotações por fechar. Pôr tokens de Google Analytics ou do Search Console numa plataforma gerida de
terceiros, por conveniência, é contrariar a única regra de segurança que já nos custou caro.
Para ferramentas de baixo risco sem dados de CRM pode discutir-se; para isto, não.

**Estado técnico, das fontes primárias:** o transporte recomendado é Streamable HTTP; o SSE puro
da versão de 2024-11-05 está depreciado. A especificação de 2026-07-28 tornou o protocolo sem
estado, o que o faz caber em infraestrutura serverless. Na autorização, quando há HTTP, o servidor
de autorização tem de ser OAuth 2.1, o cliente tem de usar PKCE, e os Resource Indicators (RFC
8707) são obrigatórios precisamente para travar o problema do delegado confuso. O reencaminhamento
de tokens é explicitamente proibido pela especificação.

**Riscos catalogados** (OWASP MCP Security Cheat Sheet): delegado confuso, reencaminhamento de
token, envenenamento de ferramentas (instruções escondidas nas descrições e nos valores de
retorno) e mudança de definição depois de aprovada. O último tem mitigação prática que devemos
adoptar se formos por aqui: fixar o hash da definição da ferramenta na descoberta e revalidar
antes de executar. Isto alinha com o bloco de defesa contra injecção que os nossos agentes já têm.

**Nota para quando quisermos tornar remotos os MCPs locais:** a Cloudflare desencorajou o
`McpAgent` para servidores novos desde Agosto de 2026, a favor de `createMcpHandler()`. Não
construir sobre o padrão antigo.

## 7. Meta: existe oficial, e o problema não é a qualidade, é a direcção
**Confirmado por nós na documentação da Meta** (`developers.facebook.com`, secção Ads MCP Server):
existe um servidor MCP oficial em `https://mcp.facebook.com/ads`, hospedado pela Meta, com
autenticação pelo Business Manager. **Cobre criação e edição de anúncios, conjuntos de anúncios e
campanhas**, citação directa: "Create and edit ads, ad sets, and campaigns".

**Correcção ao que a pesquisa trouxe:** foi-nos reportado que escreve "sem ecrã de confirmação".
A documentação não diz isso, nem num sentido nem no outro. O que está confirmado é que escreve.
Se formos por aqui, isso verifica-se antes, não se assume.

Não cobre Páginas nem Instagram orgânico, que é precisamente a parte que teria algum interesse
para presença de marca.

Alternativas de comunidade, com licenças confirmadas por nós na API do GitHub:

| Repositório | Estrelas | Licença | Push | Nota |
|---|---|---|---|---|
| `pipeboard-co/meta-ads-mcp` | 1257 | **NOASSERTION** | 2026-08-19 | licença não reconhecida como padrão; lê e escreve |
| `brijr/meta-mcp` | 200 | **NENHUMA** | 2026-05-28 | fora, pelo mesmo motivo do `ahonn` |
| `mikusnuz/meta-ads-mcp` | 78 | MIT | 2026-08-28 | lê e escreve |
| `oliverames/meta-mcp-server` | 34 | MIT | 2026-04-21 | único com Páginas e Instagram; parado há 5 meses; pede permissões de publicação |

**Nenhum destes separa leitura de escrita à nascença.** Todos expõem ferramentas de escrita mesmo
quando o caso de uso só pede leitura.

### A objecção de fundo, que é de âmbito e não de ferramenta
**O Facebook não é motor de resposta.** Ligar a Meta não torna o Eco melhor a medir presença em
IA, porque não há presença em IA a medir no Facebook. Torna-o um agente de relatórios de
marketing, que é coisa legítima e pode ser exactamente o que se quer, mas é uma decisão de âmbito
e não uma melhoria técnica do agente de GEO.

Há um argumento a favor desta leitura, vindo dos próprios dados que extraímos hoje: nas
correlações com citação em IA, o que pesa é YouTube (cerca de 0,737), Reddit e Wikipédia. O
Facebook não aparece na lista. Se o objectivo é aumentar o eco nos motores, a Meta é a rede
errada onde investir atenção.

**A recomendação, se mesmo assim se avançar:** só leitura, com âmbito `ads_read` e **nunca**
`ads_management`. O controlo que interessa está no token, não no servidor MCP: um servidor com
ferramentas de escrita ligado a um token sem permissão de escrita falha a escrita, e essa é a
única garantia que não depende de confiar em código de terceiro.

## 8. Recomendação, em degraus

**Degrau 1, faz o Eco completo em SEO e tem caminho limpo:**
GA4 com o MCP oficial da Google (Apache-2.0, leitura pura) e Search Console com o
`surendranb/google-search-console-mcp` (MIT). Ambos locais, por stdio, credenciais nossas, nada em
servidores de terceiros. É aqui que está quase todo o valor do pedido.

**Degrau 2, o teste que decide a ambição maior:**
No dia em que o Search Console ligar, primeira consulta a fazer: agrupada por `searchAppearance`,
para ver se algum valor de IA generativa aparece. Se aparecer, o Eco passa a cruzar impressões
reais em IA com o share of voice da bateria, e isso é um salto. Se não aparecer, a métrica de IA
fica manual pela interface até a Google a expor, e diz-se isso em vez de se fingir.

**Degrau 3, opcional e fora do âmbito GEO:**
Meta só leitura, com `ads_read`, se o objectivo for relatórios de marketing. Não entra como
melhoria do agente de GEO.

**Não fazer:** plataformas geridas de MCP com os nossos tokens; Google Ads (escreve, e não é
preciso para medir); Google Business Profile (candidatos frágeis e aprovação de API demorada);
qualquer repositório sem licença (`ahonn`, `brijr`) enquanto não tiverem uma.

## 9. A decisão que é de José: por onde corre isto
Não é escolha técnica, é escolha de canal, e a regra da casa diz que se apresenta o trade-off e
quem escolhe é ele.

- **Claude com MCP local:** imediato, interactivo, bom para auditoria a pedido e para diagnóstico
  de cliente. Não produz série temporal: o que não for gravado perde-se quando a sessão fecha.
- **Trigger.dev:** é onde já vive o `bdrAnalyticsWeekly` e para onde o Modo 2 do Eco já estava
  planeado migrar como `geoShareOfVoice`. É o canal certo se a medição for semanal, histórica e
  comparável. Custa trabalho de construção que o MCP não custa.
- **Híbrido, que é o que recomendo:** MCP local para o Eco auditar sob pedido, e job Trigger.dev
  para a recolha recorrente que alimenta a série. Um não substitui o outro e não são duas cópias
  do mesmo fluxo: um é interactivo, o outro é agendado.

**Antes de construir seja o que for:** confirmar que não existe já recolha de Search Console ou
GA4 noutro canal da casa. A verificação feita hoje não encontrou nenhuma, nem em `agents/` nem nos
MCP configurados.

---
**Estado:** análise para decisão. Zero instalado, zero autenticado, zero escrito fora desta pasta.
Aguarda escolha de José nos degraus e no canal.
