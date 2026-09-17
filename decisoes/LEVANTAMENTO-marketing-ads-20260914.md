# Marketing e análise de anúncios: o que vale a pena ligar
**Data:** 2026-09-14 · **Pedido de José:** alargar o levantamento a repositórios de marketing e de
análise de dados de anúncios.
**Estado:** estrelas, licença e data do último commit CONFIRMADOS POR NÓS com o GitHub
autenticado, não aceites da pesquisa. Preços vêm da pesquisa e estão marcados como tal.

## O critério, antes da lista
Três perguntas, por esta ordem. Quem falha a primeira não chega à terceira.

1. **Lê ou escreve?** Para medir, ferramentas de escrita são risco sem contrapartida.
2. **Duplica alguma coisa que já temos?** Duplicar fluxo é o erro que nenhum rollback desfaz.
3. **O que custa, e o que dá que já não tenhamos?**

## Grupo 1: analítica web alternativa ao GA4
**Veredicto: quase tudo é duplicação.** Plausible, Matomo, Umami e Fathom são substitutos do GA4,
não complementos. Com o GA4 ligado, não acrescentam nada e acrescentam manutenção.

| Repositório | Estrelas | Licença | Último push | Nota |
|---|---|---|---|---|
| `microsoft/clarity-mcp-server` | 116 | MIT | **2026-02-24** | oficial Microsoft, só leitura |
| `motherduckdb/mcp-server-motherduck` | 521 | MIT | 2026-08-19 | oficial, SQL ad-hoc |
| `getsentry/plausible-mcp` | 40 | MIT | 2026-08-31 | duplica GA4 |
| `matomo-org/plugin-McpServer` | 5 | GPL-3.0 | 2026-09-03 | oficial, duplica GA4 |
| `PostHog/mcp` | 151 | MIT | 2026-01-19 | **ARQUIVADO** |
| `cubedevinc/cube-mcp-server` | 13 | **NENHUMA** | 2026-05-14 | fora, sem licença |

**O único que acrescenta mesmo:** o **Clarity** da Microsoft, porque dá mapas de calor e gravações
de sessão, que são qualitativos e o GA4 não tem. É oficial, é MIT, é só leitura, e o produto é
gratuito. **Correcção ao que a pesquisa nos disse:** foi descrito como "bem mantido", e o último
commit é de **24 de Fevereiro**, sete meses atrás. Não é abandono, é estagnação. Muda a leitura de
"ligar já" para "ligar sabendo que pode não acompanhar mudanças da API".

**PostHog está arquivado** no repositório que era o oficial. Foi movido para dentro do monorepo da
empresa, onde continua vivo. De qualquer forma seria duplicação parcial connosco.

**Sobre BI para cruzar CRM com site:** nenhum dos MCP de BI resolve isso de fábrica. Metabase,
Cube e Superset são camadas sobre bases de dados que já teriam de ter o Pipedrive e o GA4
replicados lá dentro, o que é engenharia de dados que não temos montada e que ninguém pediu. Se um
dia for preciso cruzar, o caminho leve é o **MotherDuck/DuckDB**: exportar e cruzar com SQL, sem
infraestrutura para manter. Fica registado como opção, não como recomendação.

## Grupo 2: dados de SEO e de concorrência
Aqui há uma diferença de modelo de negócio que decide quase tudo: **quase todos exigem
mensalidade; um cobra por uso.**

| Repositório | Estrelas | Licença | Último push | Modelo |
|---|---|---|---|---|
| `dataforseo/mcp-server-typescript` | 246 | Apache-2.0 | 2026-09-01 | **pagamento por uso** |
| `serpapi/serpapi-mcp` | 169 | MIT | 2026-09-09 | subscrição |
| `marcopesani/mcp-server-serper` | 168 | MIT | **2025-03-13** | parado há 18 meses |
| `ahrefs/ahrefs-mcp-server` | 101 | **NENHUMA** | 2026-02-19 | **ARQUIVADO** |

**DataForSEO é a escolha, e por uma razão estrutural, não de funcionalidades.** É o único com
pagamento por uso a sério: depósito mínimo de cerca de 50 dólares, e consultas na ordem dos
cêntimos (preços da pesquisa, a confirmar na fonte antes de comprar). Cobre SERP, palavras-chave,
backlinks e análise de domínio. Para consultoria, isto importa mais do que parece: **o custo passa
a ser variável e imputável a um cliente concreto**, em vez de uma mensalidade fixa que temos de
amortizar tenhamos trabalho ou não.

Ahrefs (desde cerca de 129 dólares por mês), Semrush (o MCP só a partir de cerca de 199) e
Similarweb (sem preço público) são mensalidade obrigatória. Só se justificam com carteira de
clientes de SEO a pagar por isso, e não é o caso hoje.

O repositório público da Ahrefs está arquivado e sem licença; o MCP real deles é remoto e fechado,
atrás da subscrição.

## Grupo 3: monitorização paga de visibilidade em IA
**Veredicto: não comprar.** E esta é a conclusão de que tenho mais certeza de todo o levantamento.

Profound (99 a 399 dólares por mês), Otterly (MCP só a partir de 189), Peec AI (desde cerca de
95), Scrunch (MCP só a partir de 500), Evertune (800), Brandlight (sem preço público). Preços da
pesquisa.

Nós já temos motor próprio: 25 perguntas fixas, três motores, duas amostras, contagem por regex
determinístico, a custo de cêntimos por corrida. **O que estas ferramentas dão a mais é real e
vale a pena nomear com honestidade:** vêem os motores como o utilizador os vê, por navegador, o
que inclui as AI Overviews e o Copilot, superfícies que a nossa via por API não reproduz
fielmente. E trazem painéis prontos a mostrar a um cliente.

Nenhuma dessas duas coisas justifica a mensalidade **para medir a nossa própria marca**. O sinal
direccional que precisamos já o temos.

**A única porta que fica aberta, e é comercial e não técnica:** se algum dia decidirmos vender
monitorização de GEO como serviço a clientes, a conta muda, porque a mensalidade passa a ser custo
de produto com receita do outro lado. Nesse cenário o ponto de entrada mais barato com MCP nativo
é o Peec AI. Isso é decisão de oferta, do José, e não se antecipa aqui.

## Grupo 4: plataformas de anúncios

| Repositório | Estrelas | Licença | Último push | Escreve? |
|---|---|---|---|---|
| `googleads/google-ads-mcp` (oficial) | 946 | Apache-2.0 | 2026-09-10 | **não** |
| `gomarble-ai/google-ads-mcp-server` | 143 | MIT | 2026-08-05 | leitura hoje |
| `AdsMCP/tiktok-ads-mcp-server` | 49 | MIT | 2026-07-04 | **não** |
| `danielpopamd/linkedin-ads-mcp` | 33 | MIT | 2026-09-02 | **sim, 25 ferramentas** |
| `windsor-ai/windsor_mcp` | 5 | MIT | 2026-08-19 | **sim, ao vivo** |
| `CDataSoftware/linkedin-ads-mcp-server-by-cdata` | 2 | MIT | **2025-10-18** | não |
| `radiateb2b/mcp-linkedin-ads` | 1 | **NENHUMA** | 2025-06-12 | fora |

### Google Ads: correcção a uma afirmação minha anterior
Na análise da manhã escrevi que o MCP oficial de Google Ads "escreve além de ler" e "gere
campanhas", e rejeitei-o com esse fundamento. **Está errado.** Verifiquei o código: a pasta
`ads_mcp/tools/` tem exactamente três ficheiros, `search.py`, `get_resource_metadata.py` e
`core.py`, e o repositório inteiro não contém uma única ocorrência de `mutate`, que é o mecanismo
pelo qual a API do Google Ads faz todas as escritas sem excepção. **É só leitura.**

A recomendação prática não muda, mas muda o motivo, e o motivo importa: fica de fora porque não
temos campanhas Google Ads a medir, não porque seja perigoso. No dia em que houver campanhas, este
é o candidato óbvio, é oficial e é seguro.

### LinkedIn Ads: o canal que interessa, e o pior servido
É o canal que conta para B2B, e **não existe MCP oficial**, nem do LinkedIn nem da Microsoft, que
é dona da API. Todos os candidatos são de comunidade.

O mais popular, `danielpopamd`, tem 33 estrelas e vinte e cinco ferramentas que criam, editam e
apagam campanhas. Pelo critério que aplicámos o dia inteiro, está fora: para ler números, isso é
risco puro. O único desenhado só para leitura, o da CData, tem duas estrelas e **o último commit é
de Outubro de 2025**, quase um ano parado. E o `radiateb2b` não declara licença.

**Conclusão honesta: para LinkedIn Ads não há hoje boa resposta em MCP.** A escolha real é entre um
servidor com escrita que não queremos, um só-leitura quase abandonado, e um agregador pago. Se for
mesmo preciso medir LinkedIn Ads, a via mais limpa é a mesma que recomendámos para a Meta:
**a garantia vive no token, não no servidor.** Credencial de leitura, e qualquer ferramenta de
escrita falha por falta de permissão.

### Agregadores: convenientes, e todos com a mesma factura
Windsor.ai, Supermetrics, Dataslayer, Porter e Improvado resolvem quatro plataformas num servidor
só. **Todos, sem excepção, guardam ou intermediam as credenciais das nossas contas de anúncios**,
porque é assim que o modelo hospedado funciona. Não é defeito de um fornecedor, é a natureza da
coisa.

Dois têm escrita ao vivo confirmada, e para medir isso é risco sem retorno: **Windsor.ai** (pausar
campanhas, mudar orçamentos, publicar) e **Supermetrics** (criar e modificar campanhas; sem plano
gratuito, cerca de 44 a 177 dólares por mês, preços da pesquisa).

Dois anunciam-se explicitamente como só leitura: **Dataslayer** (29 a 299 euros por mês, MCP a
partir do plano de 99) e **Porter Metrics**, que é o mais claro de todos a dizer que nenhuma
ferramenta modifica, apaga ou exporta para fora do chat, e cobre 32 conectores. O preço do Porter
não foi confirmado e fica assim marcado.

## Recomendação final

**Ligar agora: nada.** O que estava em falta no Eco era a camada de superfícies próprias, e essa
ficou ligada hoje com o GA4 e o Search Console. Deste levantamento, nenhum item é preciso já.

**Ligar quando houver a dor concreta, e só então:**
- **Microsoft Clarity**, se e quando quisermos perceber comportamento na página e não só números.
  É o único gap real face ao GA4. Oficial, gratuito, só leitura, com a ressalva de estar parado
  desde Fevereiro.
- **DataForSEO**, se e quando um cliente de consultoria pagar trabalho que exija backlinks ou
  análise de concorrência. Pagamento por uso, portanto custo imputável ao cliente em vez de
  mensalidade nossa.
- **Google Ads oficial**, se e quando houver campanhas Google Ads para medir.

**Não ligar:** Plausible, Matomo, Umami, Fathom e PostHog, porque duplicam o GA4. Ahrefs, Semrush e
Similarweb, porque são mensalidade sem carteira que a justifique. Windsor.ai e Supermetrics, porque
escrevem. Qualquer repositório sem licença. Nenhuma stack de BI, porque não há dados replicados
para ela consumir.

**A conclusão de que tenho mais certeza:** não comprar monitorização paga de visibilidade em IA.
Entre 95 e 800 dólares por mês para obter, sobre a nossa própria marca, um sinal que o motor
próprio já dá por cêntimos. Só muda se decidirmos vender isso como serviço, e aí é decisão de
oferta, não de ferramenta.

---
**Estado:** levantamento para decisão. Zero instalado neste levantamento. Portões corridos.
**Versão 1.0 (2026-09-14).**
