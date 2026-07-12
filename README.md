# Resumos - Formação Microsoft Azure (DIO)

[![Validar documentação](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml/badge.svg)](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml)

Repositório de resumos das aulas do bootcamp da DIO sobre Microsoft Azure, organizado por tema para facilitar consultas e futuras atualizações.

## Índice

| # | Tema | Resumo |
|---:|---|---|
| 1 | Microsoft Azure - Localizando Serviços por Categoria | [Acessar resumo](./localizando-servicos/resumo.md) |
| 2 | Criando Máquinas Virtuais na Azure | [Acessar resumo](./maquinas-virtuais/resumo.md) |
| 3 | Tipos de Serviço de Nuvem na Azure | [Acessar resumo](./tipos-de-servico/resumo.md) |
| 4 | Configurando uma Instância de Banco de Dados na Azure | [Acessar resumo](./banco-de-dados/resumo.md) |
| 5 | Construindo Arquiteturas no Azure | [Acessar resumo](./arquiteturas/resumo.md) |

## Como adicionar um novo tema

1. Crie uma pasta com nome descritivo em `kebab-case`.
2. Adicione um arquivo `resumo.md` com título e seções sobre os principais conceitos.
3. Mantenha `Insights/Aprendizados` como a última seção do resumo.
4. Inclua o novo tema na tabela do índice.

## Validação local

Antes de enviar uma alteração, execute:

```bash
python scripts/validate_docs.py
```

O mesmo teste é executado pelo GitHub Actions em pushes para `main` e em pull requests.
