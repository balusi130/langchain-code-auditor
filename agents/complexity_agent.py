from langchain.chat_models import ChatOpenAI
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
            if isinstance(node, ast.For):
                for child in ast.walk(node):
                    if isinstance(child, ast.For) and child is not node:
                        issues.append({
                            "type": "COMPLEXITY",
                            "line": node.lineno,
                            "message": "Nested loop detected — O(n²) complexity. Consider using a dict lookup."
                        })
                        break
        return issues
