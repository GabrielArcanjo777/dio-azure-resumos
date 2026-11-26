"""Valida a estrutura dos resumos e os links locais do índice."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INSIGHTS_HEADING = "Insights/Aprendizados"


def markdown_links(content: str) -> list[str]:
    """Retorna somente destinos de links Markdown locais."""
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)
    return [
        target.split("#", maxsplit=1)[0].removeprefix("./")
        for target in targets
        if target and not target.startswith(("http://", "https://", "mailto:", "#"))
    ]


def validate_summary(path: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(ROOT).as_posix()
    content = path.read_text(encoding="utf-8")
    # Comentários "# ..." dentro de blocos de código não são títulos.
    prose = re.sub(r"^```.*?^```", "", content, flags=re.MULTILINE | re.DOTALL)

    h1_headings = re.findall(r"^#\s+(.+?)\s*$", prose, flags=re.MULTILINE)
    h2_headings = re.findall(r"^##\s+(.+?)\s*$", prose, flags=re.MULTILINE)

    if len(h1_headings) != 1:
        errors.append(f"{relative}: deve conter exatamente um título H1")
    if not h2_headings:
        errors.append(f"{relative}: não contém seções H2")
    elif h2_headings[-1] != INSIGHTS_HEADING:
        errors.append(
            f"{relative}: a última seção deve ser '## {INSIGHTS_HEADING}'"
        )
    if h2_headings.count(INSIGHTS_HEADING) != 1:
        errors.append(
            f"{relative}: deve conter exatamente uma seção '{INSIGHTS_HEADING}'"
        )
    if not content.endswith("\n"):
        errors.append(f"{relative}: falta quebra de linha no final do arquivo")

    return errors


def main() -> int:
    errors: list[str] = []

    if not README.is_file():
        print("ERRO: README.md não encontrado", file=sys.stderr)
        return 1

    readme_content = README.read_text(encoding="utf-8")
    if not readme_content.startswith(
        "# Resumos - Formação Microsoft Azure (DIO)\n"
    ):
        errors.append("README.md: título principal inesperado")

    discovered = {
        path.relative_to(ROOT).as_posix() for path in ROOT.glob("*/resumo.md")
    }
    indexed: set[str] = set()

    for link in markdown_links(readme_content):
        target = (ROOT / link).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"README.md: link aponta para fora do repositório: {link}")
            continue

        if not target.is_file():
            errors.append(f"README.md: link local não encontrado: {link}")
        if link.endswith("resumo.md"):
            indexed.add(Path(link).as_posix())

    missing_from_index = discovered - indexed
    unknown_in_index = indexed - discovered
    for path in sorted(missing_from_index):
        errors.append(f"README.md: resumo ausente no índice: {path}")
    for path in sorted(unknown_in_index):
        errors.append(f"README.md: índice aponta para resumo desconhecido: {path}")

    if not discovered:
        errors.append("Nenhum resumo foi encontrado")
    for relative in sorted(discovered):
        errors.extend(validate_summary(ROOT / relative))

    if errors:
        print("Validação falhou:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validação concluída: {len(discovered)} resumos e "
        f"{len(indexed)} links de índice válidos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
