import pycodestyle


class StyleAgent:
    """
    Checks Python source code for PEP 8 style violations.
    Handles both Unix (LF) and Windows (CRLF) line endings.
    """

    def analyze(self, source: str) -> list:
        issues = []

        # Normalise line endings — pycodestyle chokes on CRLF
        source = source.replace("\r\n", "\n").replace("\r", "\n")

        checker = pycodestyle.Checker(
            lines=source.splitlines(True),
            show_source=False,
            show_pep8=False,
            quiet=True
        )
        checker.check_all()

        for line_number, offset, code, text, _ in checker.results:
            issues.append({
                "type": "PEP8",
                "line": line_number,
                "message": f"{code} — {text}"
            })

        return issues
