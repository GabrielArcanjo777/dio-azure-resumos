# AGENTS.md

> Leia antes de alterar qualquer arquivo.

## Contexto

**O que é:** resumos das aulas da formação Microsoft Azure da DIO, um arquivo por tema, com validação automática de estrutura e links.

**O que não é:** documentação oficial nem material de certificação. Afirmação técnica deve ser conferível na documentação da Microsoft.

## Pode

- criar e revisar resumos (skill [`novo-resumo`](.agents/skills/novo-resumo/SKILL.md))
- corrigir o validador, sempre com teste
- atualizar `docs/` e este arquivo

## Não pode

- afrouxar regras do validador para fazer um resumo passar
- copiar trechos longos das aulas ou da documentação da Microsoft (resumo é com palavras próprias)

## Escala para humano quando

- um resumo contradiz a documentação oficial e não está claro qual está certo
- a mudança altera o formato de todos os resumos

## Pronto

`python scripts/validate_docs.py` e `python -m unittest discover -s tests -v` verdes (skill [`validar`](.agents/skills/validar/SKILL.md)), mais uma linha em `docs/historico.md`.

## Onde está cada coisa

| Preciso de | Vá para |
|---|---|
| Índice dos temas | `README.md` |
| O que já foi feito | `docs/historico.md` |
| Por que o formato é esse | `docs/decisoes.md` |
| Documentação da Microsoft por tema | `docs/referencias.md` |
