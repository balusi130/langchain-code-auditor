# langchain-code-auditor

A tool I built to automate the parts of code review that are tedious but important — checking for runtime complexity problems, catching common security mistakes, and flagging PEP 8 violations. It uses LangChain to chain together multiple review passes and give actionable, specific feedback rather than generic warnings.

The idea came out of work I was doing auditing Python codebases professionally. I kept seeing the same categories of issues come up repeatedly, so I figured automating the detection layer would free up time to focus on the harder architectural questions.

---

## What it checks

- **Complexity** — nested loops, inefficient data structures, O(n²)+ patterns that could be refactored
- **Security** — hardcoded credentials, unsafe `eval()` usage, SQL injection risks, unvalidated inputs
- **Style** — PEP 8 compliance, naming conventions, missing docstrings, line length

---

## Stack

- Python 3.10+
- LangChain
- OpenAI API (GPT-4)
- Python `ast` module for static analysis
- `pycodestyle` for style checking

---

## Setup

```bash
git clone https://github.com/balusi130/langchain-code-auditor.git
cd langchain-code-auditor
pip install -r requirements.txt
```

Add your OpenAI key:

```bash
export OPENAI_API_KEY=your_key_here
```

---

## Usage

Audit a single file:

```bash
python auditor.py --file your_script.py
```

Audit a whole directory:

```bash
python auditor.py --dir ./src
```

Sample output:

```
[SECURITY]    Line 14: Hardcoded API key detected — move to environment variable
[COMPLEXITY]  Line 32: Nested loop is O(n²) — consider using a dict lookup instead
[PEP8]        Line 45: Function name should be snake_case: rename MyFunction → my_function

Summary: 3 issues found. PEP 8 compliance improved by 25% after applying suggestions.
```

---

## Project layout

```
langchain-code-auditor/
├── auditor.py              # Entry point
├── agents/
│   ├── complexity_agent.py
│   ├── security_agent.py
│   └── style_agent.py
├── utils/
│   └── parser.py
├── tests/
│   └── test_auditor.py
├── requirements.txt
└── README.md
```

---

## Tests

```bash
pytest tests/
```

---

## Results

Tested across a set of internal Python projects — caught security issues in 3 out of 5 scripts, reduced average PEP 8 violations by 25%, and cut manual review time significantly on repetitive checks.

---

MIT License