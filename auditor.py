import argparse
import os
from agents.complexity_agent import ComplexityAgent
from agents.security_agent import SecurityAgent
from agents.style_agent import StyleAgent
from utils.parser import parse_file


def audit_file(filepath):
    print(f"\nAuditing: {filepath}")
    print("-" * 50)
    source = parse_file(filepath)

    agents = [ComplexityAgent(), SecurityAgent(), StyleAgent()]
    issues = []

    for agent in agents:
        found = agent.analyze(source)
        issues.extend(found)
        for issue in found:
            print(f"[{issue['type']}]\tLine {issue['line']}: {issue['message']}")

    print(f"\nSummary: {len(issues)} issue(s) found in {filepath}")
    return issues


def audit_directory(dirpath):
    all_issues = []
    for root, _, files in os.walk(dirpath):
        for f in files:
            if f.endswith(".py"):
                all_issues.extend(audit_file(os.path.join(root, f)))
    print(f"\nTotal issues across codebase: {len(all_issues)}")


def main():
    parser = argparse.ArgumentParser(description="LangChain Code Auditor")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to a single Python file")
    group.add_argument("--dir", help="Path to a directory of Python files")
    args = parser.parse_args()

    if args.file:
        audit_file(args.file)
    elif args.dir:
        audit_directory(args.dir)


if __name__ == "__main__":
    main()
