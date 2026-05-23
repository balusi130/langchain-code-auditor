def parse_file(filepath: str) -> str:
    """Read and return the source code of a Python file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
