---
name: validar
description: Roda a mesma checagem do CI deste repositório (estrutura dos resumos, links do índice e testes do validador). Use antes de qualquer commit ou PR, e sempre que o CI "Validar documentação" ficar vermelho.
---

# Validar

```bash
python scripts/validate_docs.py
python -m unittest discover -s tests -v
```

## O que cada erro quer dizer

| Mensagem | Correção |
|---|---|
| `resumo ausente no índice` | falta a linha do tema na tabela do `README.md` |
| `link local não encontrado` | o caminho no índice está errado ou a pasta foi renomeada |
| `exatamente um título H1` | há dois `#` fora de bloco de código |
| `a última seção deve ser '## Insights/Aprendizados'` | mova a seção para o fim |
| `falta quebra de linha no final` | termine o arquivo com uma linha em branco |

Se mudar `scripts/validate_docs.py`, escreva primeiro o teste em `tests/test_validate_docs.py` que mostra o problema.

**Pronto quando** os dois comandos terminam sem erro.
