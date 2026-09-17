# Activação dos MCPs de Google no Eco
**Estado a 2026-09-14:** instalado e ligado. **Falta uma credencial, e só o José a pode criar.**

## O que já está feito
| | Estado |
|---|---|
| `analytics-mcp` (GA4, oficial da Google) | instalado com `uv tool install` |
| `mcp-google-search-console` (`acamolese`) | instalado com `uv tool install` |
| Registo no Claude Code, scope user | feito, ambos aparecem como Connected |
| Ferramentas disponíveis | 9 no GA4, 17 no Search Console, todas de leitura |
| Auditoria de segurança | feita, ver `decisoes/AUDITORIA-mcp-google-20260914.md` |

Ambos os servidores esperam **o mesmo ficheiro de credenciais**, de propósito, para haver uma só
identidade a gerir e a revogar:
`~/.config/brasfone/google-eco-sa.json`

Enquanto esse ficheiro não existir, os servidores arrancam e as chamadas falham na autenticação.
É o estado normal de "instalado à espera de credencial", não é avaria.

## O que falta, e porque não o faço eu
Criar a credencial exige entrar na consola da Google com a conta do José. A regra da casa é clara:
**nunca autenticar nem inserir credenciais em nome dele.** Os passos são estes, e no terminal
pode correr os comandos com `!` à frente para o output cair nesta conversa.

### Passo 1, criar a conta de serviço (consola Google Cloud)
1. `console.cloud.google.com`, escolher ou criar um projecto.
2. Activar duas APIs: **Google Analytics Data API** e **Google Search Console API**.
3. IAM e Administração, Contas de serviço, Criar conta de serviço. Nome sugerido: `eco-medicao`.
   **Não lhe atribuir nenhum papel no projecto.** O acesso aos dados dá-se nos produtos, não aqui.
4. Na conta criada, Chaves, Adicionar chave, Criar nova chave, tipo JSON. Descarrega um ficheiro.
5. Guardar esse ficheiro exactamente em `~/.config/brasfone/google-eco-sa.json` e restringir as
   permissões: `chmod 600 ~/.config/brasfone/google-eco-sa.json`.
6. Copiar o **email** da conta de serviço, que tem a forma
   `eco-medicao@PROJECTO.iam.gserviceaccount.com`.

### Passo 2, dar acesso de leitura no Search Console
Em `search.google.com/search-console`, para **cada** propriedade (inubia.pt e brasfone.pt):
Definições, Utilizadores e permissões, Adicionar utilizador, colar o email da conta de serviço,
permissão **Restrito**, que é a de leitura. Nunca Proprietário.

### Passo 3, dar acesso de leitura no GA4
Em `analytics.google.com`, Administrador, Gestão de acessos à propriedade, adicionar o mesmo
email com o papel **Leitor**. Nunca Editor nem Administrador.

### Passo 4, confirmar
Reiniciar a sessão do Claude Code e pedir ao Eco: `eco superficies`. Ele corre a verificação e
diz o que respondeu e o que não respondeu, por produto.

## Segurança desta montagem
- **Uma identidade só**, de máquina, não a conta pessoal do José. Revoga-se apagando a chave na
  consola, sem mexer em mais nada.
- **Permissão de leitura nos dois produtos.** Mesmo que um servidor tivesse uma ferramenta de
  escrita escondida, falharia: a garantia está na permissão, não na confiança no código.
- **Nenhum âmbito `cloud-platform`.** O README do MCP oficial sugere-o para o fluxo de credenciais
  padrão; por conta de serviço não é preciso, e não lho damos.
- **A chave nunca entra no chat, em memória, ou em qualquer ficheiro do repositório.** Só o
  caminho é que é referido, e o caminho não é segredo.
- Nenhum dos dois servidores tem telemetria. Foi critério de escolha, não acaso.

## Se algo falhar
- "invalid_grant" ou "permission denied": o email da conta de serviço não foi adicionado no
  produto, ou foi adicionado noutra propriedade.
- GA4 pede um ID numérico de propriedade, não o de medição `G-XXXX`. Encontra-se em
  Administrador, Definições da propriedade.
- O Search Console distingue `sc-domain:inubia.pt` de `https://inubia.pt/`. Se a propriedade for
  de domínio, o identificador leva o prefixo `sc-domain:`.

---
**Versão 1.0 (2026-09-14).**
