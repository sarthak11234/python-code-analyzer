# Python Code Analyzer (AST-Based)

A simple Python code analyzer built using Python’s built-in **Abstract Syntax Tree (AST)** module.  
This project demonstrates how Python source code can be parsed and analyzed structurally, with a strong focus on learning and understanding the process rather than building a production-ready tool.

---

## Objective

The objective of this project is to:
- Parse a Python source file
- Count the number of:
  - Function definitions
  - Import statements
- Display the analysis result as **JSON output in the terminal**

This project prioritizes clarity, learning, and correct understanding over optimization or advanced features.

---

## Tech Stack

- **Language:** Python 3
- **Core Module:** `ast` (built-in)
- **Output Format:** JSON (printed in terminal)

No external dependencies are required.

---

## Project Structure

```
.
├── analyzer.py   # AST-based analyzer script
├── sample.py     # Sample Python file for analysis
└── README.md
```

---

## How to Run

Make sure Python 3 is installed, then run the analyzer:

```bash
python analyzer.py
```

---

## Sample Input (`sample.py`)

```python
import os
import sys

def foo():
    pass

def bar():
    print("Hello World")
```

---

## Terminal Output

```json
{
  "functions": 2,
  "imports": 2
}
```

---

## Approach

1. Read the Python source file
2. Parse the code into an **Abstract Syntax Tree (AST)**
3. Traverse the AST using `ast.NodeVisitor`
4. Count specific node types:
   - `FunctionDef` → function definitions
   - `Import` and `ImportFrom` → import statements
5. Print the results in JSON format

---

## What I Learned

- How Python internally represents code using AST
- How AST traversal works using `NodeVisitor`
- Why AST-based analysis is more reliable than regex-based parsing
- How structured JSON output can be generated from static code analysis

---

## Challenges Faced

- Understanding different AST node types initially
- Learning how recursive traversal works with `generic_visit`
- Mapping Python syntax to the correct AST nodes

Exploring and printing node types during traversal helped clarify these concepts.

---

## Future Improvements

- Detect unused variables
- Analyze function length or complexity
- Support analysis of multiple files
- Export results to a file instead of terminal output

---

## Note

This project is intentionally kept **simple** to emphasize:
- Learning process
- Clear understanding
- Working output

Not completeness or optimization.
