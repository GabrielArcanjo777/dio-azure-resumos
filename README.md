# Resumos - Formação Microsoft Azure (DIO)

[![Validar documentação](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml/badge.svg)](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml)

Resumos das aulas da formação Microsoft Azure da DIO, um por tema, escritos para consulta rápida: cada um termina com o que ficou de aprendizado.

O repositório também é um exemplo pequeno de documentação tratada como código: um script valida a estrutura de cada resumo e os links do índice em todo pull request, e o próprio script tem testes.

## Índice

| # | Tema | Resumo |
|---:|---|---|
| 1 | Microsoft Azure - Localizando Serviços por Categoria | [Acessar resumo](./localizando-servicos/resumo.md) |
| 2 | Criando Máquinas Virtuais na Azure | [Acessar resumo](./maquinas-virtuais/resumo.md) |
| 3 | Tipos de Serviço de Nuvem na Azure | [Acessar resumo](./tipos-de-servico/resumo.md) |
| 4 | Configurando uma Instância de Banco de Dados na Azure | [Acessar resumo](./banco-de-dados/resumo.md) |
| 5 | Construindo Arquiteturas no Azure | [Acessar resumo](./arquiteturas/resumo.md) |

## Como funciona a validação

```text
README.md (índice) ──► scripts/validate_docs.py ──► confere que:
*/resumo.md        ──►   - todo resumo está no índice e todo link do índice existe
                         - cada resumo tem um H1 e termina em "Insights/Aprendizados"
tests/             ──► testes do próprio validador (inclui o caso de "#" em bloco de código)
```

## O que eu aprendi

- **Serviço gerenciado não tira a responsabilidade.** Em IaaS, PaaS ou SaaS, identidade, acesso e dados continuam sendo do cliente.
- **Detalhe de cobrança importa.** Desligar a VM pelo sistema operacional não para a cobrança de computação; só desalocar para.
- **Padrão seguro precisa ser explícito.** Criar um Private Endpoint não desliga o acesso público do banco sozinho.
- **Validador também erra.** O script reprovaria um resumo válido com comando de Azure CLI comentado; um teste mostrou o bug antes de alguém tropeçar nele.

## Como adicionar um novo tema

1. Crie uma pasta com nome descritivo em `kebab-case`.
2. Adicione um arquivo `resumo.md` com título e seções sobre os principais conceitos.
3. Mantenha `Insights/Aprendizados` como a última seção do resumo.
4. Inclua o novo tema na tabela do índice.

## Validação local

Antes de enviar uma alteração, execute:

```bash
python scripts/validate_docs.py
python -m unittest discover -s tests -v
```

O mesmo teste é executado pelo GitHub Actions em pushes para `main` e em pull requests.

## Para quem for mexer

Regras em [`AGENTS.md`](AGENTS.md); passo a passo em [`.agents/skills/`](.agents/skills/novo-resumo/SKILL.md); histórico e decisões em [`docs/`](docs/historico.md).
