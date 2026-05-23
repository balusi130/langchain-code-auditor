import ast
import re


class SecurityAgent:
    PATTERNS = [
        (r"(api_key|password|secret)\s*=\s*[\"'][^\"']+[\"']", "Hardcoded credential detected — move to environment variable"),
        (r"\beval\s*\(", "Unsafe eval() usage detected"),
        (r"execute\s*\(\s*[\"']\s*SELECT.*%s", "Possible SQL injection risk — use parameterised queries"),
    ]

    def analyze(self, source: str) -> list:
        issues = []
        for i, line in enumerate(source.splitlines(), start=1):
            for pattern, message in self.PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append({"type": "SECURITY", "line": i, "message": message})
        return issues
