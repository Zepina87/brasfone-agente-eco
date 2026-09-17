# Raid do Eco: estado da Inubia e da Brasfone
**Data:** 2026-09-14 · **Ordem de José.** Varredura das superfícies das duas marcas, cruzada com
o estado do projecto no ClickUp.
**Método:** medição determinística com `scripts/audita_geo.py`, DNS e registo de domínio
consultados directamente, tarefas lidas na lista "GEO · Motores de IA (O Eco)".

## 1. O achado que muda a prioridade de tudo o resto

A tarefa ClickUp `86cbb929c`, de José, prioridade alta, prazo 4 de Setembro, diz:

> "o Fabio comprou inubia.com e vai centralizar ai toda a presenca digital, migrando do inubia.pt"

**Medido hoje, e não bate com isso:**

| Verificação | inubia.pt | inubia.com |
|---|---|---|
| Responde em HTTPS | sim, HTTP 200 | **não responde de todo** |
| Registo DNS tipo A | 185.12.116.164 | **vazio** |
| Nameservers | pdns1/2/3.dnscpanel.com | DNS1 a DNS4.HOST-REDIRECT.COM, **não respondem** |
| Data de criação do registo | n/a | **2005-06-21** |
| Registrar | n/a | Register SPA |

Três leituras possíveis, e não tenho como escolher entre elas sem perguntar ao Fábio:
1. O domínio foi mesmo comprado a um terceiro e os nameservers ainda não foram mudados.
2. A compra está em curso e a tarefa antecipou-se ao facto.
3. A informação não está correcta.

O que é facto, e é o que interessa: **hoje o inubia.com não serve nada, não resolve, e aponta
para nameservers de um serviço de redireccionamento que nem responde.** A data de 2005 diz que o
domínio não nasceu connosco, foi comprado a alguém, o que é normal, mas também significa que pode
ter histórico próprio nos motores.

**Porque isto é urgente para o Eco, e não apenas para o marketing:** uma migração de domínio é o
único evento que consegue apagar de uma vez tudo o que se construiu em presença nos motores. Os
modelos e os índices aprenderam `inubia.pt`. Se a mudança acontecer sem redireccionamentos
permanentes página a página, não perdemos posições, perdemos a identidade: as respostas passam a
citar um domínio que já não existe, ou deixam de nos citar.

E há uma consequência directa na nossa medição: **a bateria congelada e os aliases do Eco falam de
`inubia.pt`.** No dia da migração, a série temporal parte ao meio se ninguém tratar disso antes.
Isto não é motivo para mexer na bateria agora, é motivo para decidir com antecedência o que fazer.

**Recomendação, e é a única coisa deste documento que eu faria esta semana:** confirmar com o
Fábio se o domínio já é nosso e qual a data prevista. Enquanto não houver data, não se mexe em
nada. Quando houver, o trabalho do Eco é anterior à migração, não posterior.

## 2. Estado técnico medido, as duas marcas

Bruto em `baseline/raid-2026-09-14.json` e `baseline/raid-inubiacom-2026-09-14.json`.

**Acesso dos motores: sem problema em nenhuma superfície.** Os treze bots estão permitidos nos
dois domínios, citação e treino. Nada nos bloqueia, e isto está agora medido bot a bot, não
afirmado.

| | inubia.pt | www.brasfone.pt |
|---|---|---|
| Título | "Início - Inubia \| Brasfone Grupo" | "BRASFONE \| Soluções tecnológicas \| Portugal" |
| Meta description | **VAZIA** | preenchida |
| JSON-LD | **NENHUM** | LocalBusiness, WebSite |
| h1 / h2 | 1 / 6 | 1 / 4 |
| Palavras visíveis | 1361 | 751 |
| Peso do HTML | 67 KB | **1,76 MB** |
| llms.txt | 404 | 200 (automático do Wix) |

**Três problemas reais, por ordem de custo de arranjar:**

1. **inubia.pt sem meta description e sem JSON-LD nenhum.** É a marca de campanha, aquela por que
   queremos ser encontrados, e é a superfície mais fraca das duas. A meta description é meia hora
   de trabalho. O JSON-LD já está gerado e à espera: `scripts/gera_jsonld.py organization inubia`.
2. **brasfone.pt com 1,76 MB de HTML para 751 palavras visíveis.** É o Wix a fazer o que o Wix
   faz. Não é bloqueante para citação, mas é peso morto.
3. **brasfone.pt tem JSON-LD, mas não tem `Organization`.** Tem `LocalBusiness` e `WebSite`, que
   não dizem a um motor o que a entidade é nem a quem se liga. O gerador resolve isto.

**O llms.txt deixou de ser prioridade,** e isto corrige o que estava planeado. A Google declara na
documentação oficial que o ignora, nem ajuda nem prejudica. Há duas tarefas no ClickUp sobre
llms.txt que valem muito menos do que valiam quando foram escritas. A de `brasfone.pt` mantém-se,
mas por outro motivo: o ficheiro automático do Wix afirma "Elite" e "anteriormente Brasfone",
contra a entidade que José fixou. Corrige-se por estar errado à frente de toda a gente.

## 3. Estado do projecto no ClickUp

Lista "GEO · Motores de IA (O Eco)", em INUBIA | Aquisição. **Oito tarefas, oito por iniciar,
todas com prazo de 28 de Agosto.** Dezassete dias de atraso, nenhuma começada.

Quatro são de José:
- Documentar o que foi criado e onde está
- Deploy do job semanal de medição no Trigger.dev
- Pedir reviews a 3 clientes para o perfil Pipedrive
- E, noutra lista, instruir o Eco sobre a migração para inubia.com (prazo 4 de Setembro)

As outras quatro estão com colegas e não são para aqui listadas; o que interessa a José é que
duas delas bloqueiam o agente: a palavra-passe de aplicação do WordPress, sem a qual o Eco não
pode publicar nada no inubia.pt, e a decisão sobre as 14 páginas GEO.

**Uma é urgente e não é do Eco, mas afecta-o:** a tarefa diz que o perfil da Brasfone no
marketplace do Pipedrive está em 404.
**CORRECÇÃO 2026-09-15:** o perfil NÃO está em 404. O slug mudou. `partners/brasfone` dá 404,
mas `https://www.pipedrive.com/en/marketplace/partners/inubia-brasfone-group` responde **200**,
e foi o próprio Sonar que o citou numa resposta de teste. A tarefa ClickUp e a versão de ontem
deste relatório apontavam para o slug antigo. O que continua verdade: não aparecemos na listagem
de parceiros de Portugal, e todos os nossos ficheiros (JSON-LD, llms.txt, estratégia) apontavam
para o URL morto. Corrigido no `fase1-diffs/inubia-jsonld.html`; falta corrigir no `llms-brasfone.txt`
e no que mais o cite.

## 4. O que mudou hoje, e que torna metade disto mais fácil

O agente deixou de depender de auditoria manual. O que antes era uma tarefa de meia manhã passou a
ser `python3 scripts/audita_geo.py <domínio>`, com os bots nomeados um a um e três estados, porque
uma medição que falha tem de dizer que falhou e não "está tudo bem". Foi assim que o `inubia.com`
apareceu como NÃO VERIFICADO em vez de aparecer como permitido, que é o que a versão anterior
teria dito.

## 5. Ordem sugerida, se me perguntar por onde começar
1. Confirmar com o Fábio o estado real do inubia.com e a data da migração. Tudo o resto depende disto.
2. Meta description e JSON-LD no inubia.pt. Está gerado, falta colar.
3. Corrigir o llms.txt do Wix, por causa do "Elite", não por causa de ranking.
4. Marketplace Pipedrive fora do 404.
5. O job semanal no Trigger.dev, que é o que transforma medições soltas em série temporal.

---
**Estado:** leitura e medição. Zero escrita em superfícies, zero publicação.
**Versão 1.0 (2026-09-14).**
