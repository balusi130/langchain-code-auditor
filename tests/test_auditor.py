import pytest
from agents.security_agent import SecurityAgent
from agents.complexity_agent import ComplexityAgent
from agents.style_agent import StyleAgent


def test_security_detects_hardcoded_key():
    source = 'api_key = "abc123secret"'
    agent = SecurityAgent()
    issues = agent.analyze(source)
    assert any(i["type"] == "SECURITY" for i in issues)


def test_security_detects_eval():
    source = "result = eval(user_input)"
    agent = SecurityAgent()
    issues = agent.analyze(source)
    assert any("eval" in i["message"] for i in issues)


def test_complexity_detects_nested_loops():
    source = """
for i in range(10):
    for j in range(10):
        print(i, j)
"""
    agent = ComplexityAgent()
    issues = agent.analyze(source)
    assert any(i["type"] == "COMPLEXITY" for i in issues)


def test_no_false_positive_on_clean_code():
    source = """
def add(a, b):
    return a + b
"""
    agent = SecurityAgent()
    issues = agent.analyze(source)
    assert len(issues) == 0
