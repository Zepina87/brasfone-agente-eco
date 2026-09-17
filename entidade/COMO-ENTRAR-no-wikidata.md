# Como entrar no Wikidata, passo a passo
**Data:** 2026-09-16 · **Ordem de José:** "vamos entrar para aí". Este documento é a execução dessa
ordem até ao ponto em que só uma pessoa autenticada pode continuar.
**Estado da janela (verificado 16-09):** a consulta de reforma da notoriedade continua aberta
(última actividade 14 de Julho de 2026, três rondas). Ainda não é regra que a empresa não possa
criar o próprio item, mas a direcção é essa. Entrar antes de fechar, e entrar bem.

## O que está pronto
| Ficheiro | O que é |
|---|---|
| `quickstatements-1-brasfone.txt` | comandos para criar o item da Brasfone, com referências |
| `quickstatements-2-inubia.txt` | comandos para criar o item da Inubia, ligado à Brasfone e ao Pipedrive |
| `PACOTE-wikidata-inubia.md` | a justificação de cada propriedade e os QIDs verificados |

**Todos os QIDs foram verificados na API do Wikidata a 16-09.** Um deles estava errado no pacote
de ontem: Q207431 é Louis van Gaal, não Faro. Faro cidade é Q3344655. Sem verificação, a sede da
Brasfone ficava ligada a um treinador de futebol. Nenhum QID entra sem esta verificação.

## Dados fornecidos por José a 16-09, já nos ficheiros
- **NIF 506079031** em `P3608` como `PT506079031`. Dígito de controlo validado (mod 11), prefixo 5
  = pessoa colectiva. Nota: não está em nenhuma superfície pública nossa (homepage, termos,
  privacidade dos dois sites); um site de empresa sem NIF no rodapé é fraco em sinal de entidade
  e vale a pena corrigir na Fase 1.
- **Sociedade por quotas (Lda.)** em `P1454` = Q115399164, "legal form in Portugal", verificado.
- **A Inubia é marca registada dentro do grupo Brasfone**, sem pessoa jurídica própria: `P31` =
  Q167270 (marca comercial), sem NIF próprio; a ligação ao NIF faz-se pela mãe via `P749`.
- Ano de constituição (`P571`): não fornecido; fica de fora. Acrescenta-se depois se quiser.

**Os dois ficheiros QuickStatements estão completos.** Só falta, no ficheiro 2, substituir o
placeholder do QID da Brasfone pelo QID real depois do passo 1.

## Quem cria
**Não a Brasfone nem a Inubia.** A consulta em curso vai no sentido de proibir a criação pela
própria empresa, e mesmo hoje um item criado pela entidade que descreve é olhado com suspeita e
apagado com mais facilidade. Quem cria:
- uma pessoa com conta Wikidata própria, de preferência com algum histórico de edições (uma conta
  criada hoje só para isto é sinal de conflito de interesse);
- que declare na página de discussão do item, em uma linha, a relação com a empresa, se houver.
  Transparência protege o item; ocultação condena-o.
- Sugestão prática: um parceiro ou consultor externo que conheça a casa e tenha conta.

## Procedimento, em ordem
1. José fornece NIF, forma jurídica e a decisão marca ou empresa para a Inubia. Eu preencho os
   placeholders nos dois ficheiros e verifico o QID da forma jurídica.
2. A pessoa que cria abre `https://quickstatements.toolforge.org/`, entra com a conta Wikidata,
   escolhe "New batch", formato **V1**, cola o conteúdo de `quickstatements-1-brasfone.txt`,
   "Import V1 commands", revê a pré-visualização linha a linha, "Run".
3. Anota o QID devolvido (formato `Q123456789`).
4. Substitui `Q_____QID_DA_BRASFONE_CRIADO_NO_PASSO_1_____` no ficheiro 2 por esse QID.
5. Repete o passo 2 com `quickstatements-2-inubia.txt`.
6. Na página de discussão de cada item, uma linha: "Item criado a partir de fontes públicas
   (site oficial, marketplace Pipedrive, registo comercial). [Relação com a entidade, se houver.]"
7. Envia-me os dois QIDs.

## O que eu faço depois de ter os QIDs
- `python3 scripts/gera_jsonld.py organization inubia --wikidata QID_INUBIA --wikidata-mae QID_BRASFONE`
  gera o JSON-LD com `sameAs` para o Wikidata, que é o sinal de desambiguação mais forte que um
  site pode dar. Vai para a entrega da Fase 1.
- `python3 scripts/audita_entidade.py` tem de passar a Inubia de NOME OCUPADO para TALVEZ NOSSA e
  a Brasfone de AUSENTE para TALVEZ NOSSA. Se não passar, algo ficou mal ligado e vê-se logo.
- Actualizo a Fase 1 da `ESTRATEGIA-GEO.md` como fechada neste ponto.

## O que NÃO fazer
- Não criar a Inubia antes da Brasfone: fica um item órfão com nome ambíguo, o pior dos dois mundos.
- Não inventar o NIF nem "aproximar". Um identificador errado é pior do que nenhum.
- Não pôr o logótipo (`P154`) a menos que esteja carregado no Wikimedia Commons com licença livre.
  Uma imagem com direitos reservados é apagada e arrasta atenção para o item.
- Não editar a descrição das entidades brasileiras para "libertar" o nome. Não é nosso, e é a
  forma mais rápida de sermos bloqueados.
- Não repetir a criação se o primeiro item for apagado: ler o motivo na página de eliminação e
  corrigir. Recriar sem corrigir é o segundo caminho mais rápido para o bloqueio.

## Porque isto importa, em uma frase para quem perguntar
Hoje, quando um modelo de IA procura "Inubia" no grafo de conhecimento, encontra um instrumento
indígena e um município do Brasil; quando procura "Brasfone", não encontra nada. Nenhum
concorrente português está lá. Quem entrar primeiro, ligado ao Pipedrive, fica com a única âncora
de terceiro do mercado.

---
**Versão 1.0 (2026-09-16).**
