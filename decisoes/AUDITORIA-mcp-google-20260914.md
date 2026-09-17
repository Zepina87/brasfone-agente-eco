# Auditoria dos servidores MCP candidatos, um a um
**Data:** 2026-09-14 · **Âmbito:** ligar o Eco ao Search Console e ao GA4
**Método:** clone em sandbox, leitura de código, `audit-externo.sh` com os achados LIDOS, e
handshake MCP real para confirmar as ferramentas que cada servidor expõe de facto.
**Regra aplicada:** nenhum PASS aceite sem contagem de ficheiros lidos, nenhuma FALHA aceite sem
ler o achado.

## Quadro final

| | GA4 oficial | Search Console `acamolese` | Search Console `surendranb` |
|---|---|---|---|
| Repositório | `googleanalytics/google-analytics-mcp` | `acamolese/google-search-console-mcp` | `surendranb/google-search-console-mcp` |
| Autoria | **Google** | indivíduo | indivíduo |
| Licença | Apache-2.0 | MIT | MIT |
| Estrelas | 3185 | 8 | 38 |
| Último push | 2026-08-07 | 2026-08-22 | 2026-08-22 |
| Âmbito OAuth | `analytics.readonly` | `webmasters.readonly` | `webmasters` (não restrito) |
| Ferramentas de escrita | **nenhuma** | **nenhuma** | `submit_sitemap`, `delete_sitemap` |
| Telemetria | **nenhuma** | **nenhuma** | **PostHog, ligada por omissão** |
| cc-audit | 1 médio, 0 críticos, 19 ficheiros | 4 críticos, 103 ficheiros | 11 críticos, 37 ficheiros |
| gitleaks | limpo | limpo | chave pública PostHog |
| Ferramentas confirmadas | **9** | **17** | 9 |
| **Veredicto** | **ESCOLHIDO** | **ESCOLHIDO** | **REJEITADO** |

## 1. `googleanalytics/google-analytics-mcp` — ESCOLHIDO para GA4

**Porque ganha:** é da própria Google, Apache-2.0, com tracção real, e não tem uma única
ferramenta de escrita. Para quem quer medir e não mexer, é exactamente o perfil certo.

**Ferramentas confirmadas por handshake MCP** (não lidas do README): `run_report`,
`run_realtime_report`, `run_funnel_report`, `run_conversions_report`, `get_account_summaries`,
`get_property_details`, `list_property_annotations`, `get_custom_dimensions_and_metrics`,
`list_google_ads_links`. Nove, todas de leitura.

**Segurança:** `audit-externo.sh` leu 19 ficheiros, zero críticos, zero altos, um médio. Gitleaks
limpo. Zero telemetria. O código tem uma função `prevent_stdio_inheritance`, que é sinal de
cuidado deliberado com o canal stdio.

**O ponto a vigiar, e é o único:** o README manda autenticar com os âmbitos
`analytics.readonly` **e** `cloud-platform`. O segundo é largo: cobre a plataforma Google Cloud
inteira. Verificámos onde aparece: **só nas instruções do README**, nunca no código, que pede
apenas `analytics.readonly`. O `cloud-platform` serve o projecto de quota do fluxo de credenciais
padrão. Como vamos por conta de serviço e não por esse fluxo, **não lhe damos `cloud-platform`.**
Se algo falhar por causa disso, resolve-se no projecto de quota, não alargando permissões.

**Ressalva de estabilidade:** a Google marca-o como experimental e o servidor emite avisos de
funcionalidade experimental no arranque. Significa que a interface pode mudar entre versões, não
que seja inseguro. Fixar a versão instalada e reler o changelog antes de actualizar.

## 2. `acamolese/google-search-console-mcp` — ESCOLHIDO para Search Console

Não existe MCP oficial da Google para o Search Console. Entre os de comunidade, este ganhou por
uma razão que não é popularidade: **é o único cujo desenho recusa escrever.**

**O que o README declara e o código confirma:** "The OAuth scope is `webmasters.readonly` and
nothing else." Procurámos âmbitos em todo o repositório: aparece um só, e é o de leitura.

**Dezassete ferramentas, confirmadas por handshake:** `gsc_sites`, `gsc_site_details`,
`gsc_query`, `gsc_performance_overview`, `gsc_compare_periods`, `gsc_quick_wins`, `gsc_ctr_gaps`,
`gsc_cannibalization`, `gsc_traffic_drops`, `gsc_content_decay`, `gsc_alerts`, `gsc_portfolio`,
`gsc_indexing_issues`, `gsc_inspect_url`, `gsc_sitemaps`, `gsc_doctor`, `gsc_audit`.

**Duas delas encaixam directamente na doutrina que o Eco ganhou esta manhã.** `gsc_content_decay`
mede degradação de conteúdo ao longo do tempo, que é a outra face da frescura que pusemos em
`kb/citabilidade.md` como a alavanca mais barata que temos. E `gsc_compare_periods` dá a forma de
provar que um refrescamento funcionou, em vez de o afirmar.

**Segurança:** `audit-externo.sh` leu 103 ficheiros. Gitleaks limpo. Zero destinos de rede fora dos
domínios da Google e do localhost. Os quatro achados críticos foram lidos e são falsos positivos,
sendo que dois deles são o contrário do que a acusação diz:
- "Transmissão de rede em base64": é `base64.b64encode` a embutir um logótipo como data URI num
  relatório HTML. Não há rede nenhuma envolvida.
- "Intenção de exfiltração": disparou numa função cujo comentário no código é "A Google Fonts
  stylesheet would make the report phone home when opened". O autor desliga fontes externas por
  omissão **para o relatório não telefonar para casa**. O detector acusou de exfiltração o código
  que previne exfiltração.

**O risco honesto:** oito estrelas, um contribuidor, projecto de 2026. Não tem validação de
comunidade. Mitiga-se com o que já fizemos, que é ler o código em vez de contar estrelas, e com o
facto de o âmbito de leitura limitar o estrago possível a zero escrita. Se o projecto morrer,
substitui-se; não há dependência estrutural.

## 3. `surendranb/google-search-console-mcp` — REJEITADO

Era a recomendação inicial da pesquisa, por ter mais tracção. Caiu na leitura do código, por dois
motivos independentes, e qualquer um bastava.

**Escreve.** Expõe `submit_sitemap` e `delete_sitemap`. Um agente com esta ferramenta pode remover
um sitemap de uma propriedade. Para um servidor cujo propósito no nosso caso é ler números, é
capacidade que só traz risco. O âmbito que pede também não é o restrito de leitura.

**Telemetria ligada por omissão, para o PostHog do autor.** Destinos: `gsc.builditwithai.xyz` e um
worker da Cloudflare do autor. O gitleaks apanhou a chave do PostHog no `wrangler.toml`, que é uma
chave pública de projecto e por isso não é fuga, mas confirma para onde os dados vão.

Em abono da verdade, e porque a auditoria tem de ser justa: **a telemetria não exfiltra dados do
Search Console.** O código redige explicitamente os domínios do utilizador, trocando
`sc-domain:exemplo.com` por `<url>`. Isso é cuidado deliberado do autor, e diz-se.

O que envia é impressão digital do ambiente: versão de Python, arquitectura, fuso horário, se está
em contentor ou CI, que ferramentas de IA estão presentes na máquina (Claude Code, Cursor, Gemini,
Windsurf, VS Code) e **os nomes dos processos ancestrais**. Há opt-out por `DISABLE_TELEMETRY`,
`DO_NOT_TRACK` ou `NO_TELEMETRY`, e o opt-out é sério: corta todos os efeitos, incluindo escritas
locais. Mas é opt-out, não opt-in.

**Porque isto chega para rejeitar, quando temos alternativa:** o precedente do Blender MCP, que
instalámos com a telemetria desligada, existiu porque não havia alternativa. Aqui há uma
alternativa sem telemetria nenhuma e sem ferramentas de escrita. Aceitar a pior das duas por ter
mais trinta estrelas seria trocar segurança por popularidade.

O achado "intenção de exfiltração" no `gsc_setup_flow.py` deste repositório é, esse sim, falso
positivo: é o fluxo de configuração a pedir o caminho do ficheiro de credenciais, e o comentário
do próprio código diz "collect a path (not a secret)".

## 4. Os que nem chegaram a auditoria de código
- `ahonn/mcp-server-gsc` (264 estrelas, o mais popular): **não declara licença**. Por omissão,
  todos os direitos reservados. Fora, até publicar uma.
- `googleads/google-ads-mcp` (oficial, Apache-2.0): bom servidor, mas gere campanhas. Não é
  preciso para medir e traz capacidade de gastar dinheiro.
- Google Business Profile: candidatos com duas estrelas e uma aprovação de API da Google que
  demora semanas. Sem dor concreta, não se avança.
- Meta: ver `ANALISE-superficies-medicao-20260914.md`, secção 7. O problema é de direcção, não de
  ferramenta.

---
**Versão 1.0 (2026-09-14).**
