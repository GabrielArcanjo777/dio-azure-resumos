# Decisões

## D-001 — Um tema, uma pasta, um `resumo.md`

**Por quê:** fica fácil achar um tema e fácil para um script conferir tudo.

## D-002 — `Insights/Aprendizados` sempre no fim

**Por quê:** é a parte que eu consulto antes de uma entrevista. Estar sempre no mesmo lugar é o que torna a consulta rápida.

## D-003 — O formato é validado no CI, e o validador tem testes

**Por quê:** regra de formato que depende de memória some na terceira aula. E um validador sem teste pode reprovar o que é válido, como aconteceu com comentários em blocos de código (ver `historico.md`).

## D-004 — Sem `dados/` nem `demandas/`

**Por quê:** o repositório não tem dados nem backlog; criar pastas vazias seria estrutura sem função. Se surgir um pedido grande (por exemplo, um tema novo com laboratório), ele entra em `demandas/<id>/`.
