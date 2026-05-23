import pycodestyle
import io


class StyleAgent:
    def analyze(self, source: str) -> list:
        issues = []
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.input_file(
            "temp_check.py",
            lines=source.splitlines(True)
        )
        # pycodestyle writes to stdout; capture via its checker
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
