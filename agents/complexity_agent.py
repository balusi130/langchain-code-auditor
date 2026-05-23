from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import ast


class ComplexityAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)

    def analyze(self, source: str) -> list:
        issues = []
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return issues

        for node in ast.walk(tree):
            # Only flag actual For loops, not comprehensions
            if isinstance(node, ast.For):
                for child in ast.walk(node):
                    if isinstance(child, ast.For) and child is not node:
                        # Skip if inside a comprehension
                        if not isinstance(child, ast.comprehension):
                            issues.append({
                                "type": "COMPLEXITY",
                                "line": node.lineno,
                                "message": (
                                    f"Nested loop at line {node.lineno} — O(n²) complexity. "
                                    "Consider using a dict or set lookup to reduce to O(n)."
                                )
                            })
                        break
        return issues
