---
name: novo-resumo
description: Adiciona o resumo de uma nova aula ou tema de Azure neste repositório, no formato que o validador aceita. Use sempre que for criar, renomear ou reorganizar um resumo, mesmo que o pedido seja só "anota essa aula" ou "coloca isso no repo de Azure".
---

# Novo resumo

O valor deste repositório é ser consultável numa entrevista ou na prova da certificação. Por isso todo resumo tem a mesma forma: um título, seções curtas e, no fim, o que ficou de aprendizado.

## Passos

1. Crie `<tema-em-kebab-case>/resumo.md`. O validador só enxerga arquivos nesse padrão (`*/resumo.md`).
2. Estrutura:

```markdown
# Título do tema

## Conceito ou etapa
Texto curto, com o porquê, não só o passo a passo.

## Insights/Aprendizados
- o que você levaria para um projeto real
```

   - Um único `#` (H1). Comentários `#` dentro de bloco de código não contam.
   - `## Insights/Aprendizados` é sempre a última seção, e aparece uma vez só.
3. Adicione uma linha na tabela de índice do `README.md`. Resumo fora do índice reprova o CI.
4. Rode a skill [`validar`](../validar/SKILL.md).

## Cuidado com o conteúdo

Afirmação técnica sobre Azure (preço, limite, comportamento padrão) precisa bater com a documentação da Microsoft. Na dúvida, coloque o link em `docs/referencias.md` em vez de afirmar de memória.
