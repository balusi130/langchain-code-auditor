import re


class CorrelatedSubqueryAgent:
    """
    Detects correlated subqueries in SELECT statements that could
    be rewritten as JOINs for better performance.
    """

    def analyze(self, source: str) -> list:
        issues = []
        # Look for SELECT inside WHERE clauses — common correlated subquery pattern
        pattern = re.compile(r"WHERE\s+\w+\s+IN\s*\(\s*SELECT", re.IGNORECASE)
        for i, line in enumerate(source.splitlines(), start=1):
            if pattern.search(line):
                issues.append({
                    "type": "REWRITE",
                    "line": i,
                    "message": (
                        "Correlated subquery detected (WHERE x IN (SELECT ...)). "
                        "Consider rewriting as a JOIN — it is usually faster on large tables."
                    )
                })
        return issues
