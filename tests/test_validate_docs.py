"""Testes do validador: garantem que ele aprova o que é válido e acusa o que não é."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_docs.py"
spec = importlib.util.spec_from_file_location("validate_docs", SCRIPT)
validate_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_docs)

TITULO = "# Resumos - Formação Microsoft Azure (DIO)\n"
RESUMO_OK = "# Tema\n\n## Conceito\n\nTexto.\n\n## Insights/Aprendizados\n\n- Item.\n"


class ValidadorTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._original_root = validate_docs.ROOT
        self._original_readme = validate_docs.README
        validate_docs.ROOT = self.root
        validate_docs.README = self.root / "README.md"

    def tearDown(self) -> None:
        validate_docs.ROOT = self._original_root
        validate_docs.README = self._original_readme
        self._tmp.cleanup()

    def _resumo(self, pasta: str, conteudo: str) -> Path:
        caminho = self.root / pasta / "resumo.md"
        caminho.parent.mkdir()
        caminho.write_text(conteudo, encoding="utf-8")
        return caminho

    def _readme(self, *links: str) -> None:
        linhas = "".join(f"- [x](./{link})\n" for link in links)
        (self.root / "README.md").write_text(TITULO + "\n" + linhas, encoding="utf-8")

    def test_repositorio_valido_passa(self) -> None:
        self._resumo("tema", RESUMO_OK)
        self._readme("tema/resumo.md")
        self.assertEqual(validate_docs.main(), 0)

    def test_resumo_fora_do_indice_falha(self) -> None:
        self._resumo("tema", RESUMO_OK)
        self._readme()
        self.assertEqual(validate_docs.main(), 1)

    def test_link_quebrado_falha(self) -> None:
        self._resumo("tema", RESUMO_OK)
        self._readme("tema/resumo.md", "nao-existe/resumo.md")
        self.assertEqual(validate_docs.main(), 1)

    def test_insights_precisa_ser_a_ultima_secao(self) -> None:
        caminho = self._resumo("tema", "# Tema\n\n## Insights/Aprendizados\n\n- a\n\n## Depois\n\nx\n")
        erros = validate_docs.validate_summary(caminho)
        self.assertTrue(any("última seção" in erro for erro in erros))

    def test_comentario_em_bloco_de_codigo_nao_e_titulo(self) -> None:
        # Um resumo com comando de Azure CLI comentado é válido.
        conteudo = (
            "# Tema\n\n## Criando pelo terminal\n\n"
            "```bash\n# cria o grupo de recursos\naz group create -n rg -l brazilsouth\n"
            "## outro comentário\n```\n\n"
            "## Insights/Aprendizados\n\n- Item.\n"
        )
        caminho = self._resumo("tema", conteudo)
        self.assertEqual(validate_docs.validate_summary(caminho), [])


if __name__ == "__main__":
    unittest.main()
