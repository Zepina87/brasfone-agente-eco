# O Eco — agente GEO da Brasfone/Inubia

Cópia exacta do agente Eco tal como corre internamente na Brasfone: os 6 modos (auditoria,
monitor, conteúdo, relatório, superfícies próprias, entidade), a bateria de perguntas congelada, o
histórico de medição, as decisões e os scripts.

## Instalar no Claude Code

```bash
git clone https://github.com/Zepina87/brasfone-agente-eco.git
mkdir -p ~/.claude/skills
cp -R brasfone-agente-eco ~/.claude/skills/eco
```

Abre o Claude Code (nesta pasta ou noutra) e escreve `/eco` para confirmar que instalou.

## O que está aqui

| Ficheiro/pasta | O que é |
|---|---|
| `MASTER-PROMPT-ECO.md` | Fonte única de verdade: missão, regras, os 6 modos |
| `ESTRATEGIA-GEO.md` | Estratégia e faseamento |
| `prompts-baseline.json` / `prompts-baseline-v1.1.json` | Bateria de perguntas congelada (Modo 2) |
| `baseline/` | Séries de medição, scripts de corrida e reprocessamento |
| `decisoes/` | Decisões e auditorias que moldaram o agente |
| `entidade/` | Pacote de trabalho sobre a entidade no Wikidata |
| `fase1-diffs/` `fase2-conteudo/` | Correcções técnicas e conteúdo GEO já produzidos |
| `kb/` | Base de conhecimento verificada (crawlers, posição do Google, citabilidade) |
| `scripts/` | Auditoria técnica, auditoria de entidade, gerador de JSON-LD |

## Nota sobre caminhos internos

Este é um clone exacto do agente tal como vive dentro do ecossistema completo da Brasfone. Por
isso, o `MASTER-PROMPT-ECO.md` cita alguns caminhos que só existem lá dentro (`agents/o-cerebro/kb/...`,
`agents/_tools/fact-gate.sh`, o blackboard `agents/o-cerebro/memory/state.md`). Aqui, sozinho,
esses ficheiros não existem — os modos de leitura (auditoria, monitor, entidade) funcionam de
qualquer forma; os que dependem desses gates (conteúdo, relatório) esperam que os recries ou que
peças o agente para te dizer o que precisa, em vez de inventar que passou um portão que não existe.

## Antes de correr por conta própria

Os modos que escrevem para fora (conteúdo, relatório) esperam os gates da casa (`fact-gate`,
`ghost-check`) e a aprovação de quem decide. Os modos de leitura (auditoria, monitor, entidade)
não pedem licença. Ver `MASTER-PROMPT-ECO.md` para o detalhe de cada modo.
