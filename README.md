# Resumos - Formação Microsoft Azure (DIO)

[![Validar documentação](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml/badge.svg)](https://github.com/GabrielArcanjo777/dio-azure-resumos/actions/workflows/docs.yml)

Base de conhecimento construída durante a formação Microsoft Azure da DIO. O conteúdo está separado por tema, escrito com foco em decisões práticas de arquitetura e validado automaticamente para evitar links quebrados ou documentos fora do padrão.

## Objetivo

- consolidar fundamentos de cloud em documentação consultável;
- relacionar serviços do Azure a requisitos de disponibilidade, segurança e custo;
- registrar aprendizados com exemplos e limitações explícitas;
- aplicar automação e integração contínua também a projetos de documentação.

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

## Como a validação funciona

O script descobre todos os arquivos `*/resumo.md` e compara esse conjunto com os links do índice. Assim, um novo resumo não fica invisível e um link antigo não continua apontando para um arquivo removido.

```python
discovered = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.glob("*/resumo.md")
}

missing_from_index = discovered - indexed
unknown_in_index = indexed - discovered
```

Cada documento também precisa ter exatamente um título principal, seções de segundo nível e terminar com `Insights/Aprendizados`. Essa regra mantém a leitura consistente sem exigir revisão manual de formatação a cada alteração.

## Validação local

Antes de enviar uma alteração, execute:

```bash
python scripts/validate_docs.py
```

O mesmo teste é executado pelo GitHub Actions em pushes para `main` e em pull requests.

## Escopo

Este repositório registra estudos e experimentos. Ele não substitui a documentação oficial da Microsoft nem representa uma arquitetura pronta para produção. Preços, limites e recursos do Azure devem ser conferidos na documentação oficial antes de uma implementação real.
