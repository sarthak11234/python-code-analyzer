import ast
import json
import sys

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"functions": [], "imports": []}
        self.tree = []
        self.indent = 0

    def visit_FunctionDef(self, node):
        self.stats["functions"].append(node.name)
        self.tree.append("  " * self.indent + f"└── [FUNC] {node.name}")
        self.indent += 1
        self.generic_visit(node)
        self.indent -= 1

    def visit_ClassDef(self, node):
        self.tree.append("  " * self.indent + f"└── [CLASS] {node.name}")
        self.indent += 1
        self.generic_visit(node)
        self.indent -= 1

    def visit_Import(self, node):
        for name in node.names:
            self.stats["imports"].append(name.name)
            self.tree.append("  " * self.indent + f"└── [IMPORT] {name.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module or "?"
        for name in node.names:
            full_name = f"{module}.{name.name}"
            self.stats["imports"].append(full_name)
            self.tree.append("  " * self.indent + f"└── [IMPORT] {full_name}")
        self.generic_visit(node)

def analyze_code(file_path):
    try:
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
    except Exception as e:
        print(f"Error: {e}")
        return

    analyzer = CodeAnalyzer()
    analyzer.visit(tree)

    print(f"\n� File: {file_path}\n")
    print("AST Structure:")
    for line in analyzer.tree:
        print(line)

    print("\nStats:")
    print(json.dumps(analyzer.stats, indent=2))

if __name__ == "__main__":
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    
    target = sys.argv[1] if len(sys.argv) > 1 else "sample.py"
    analyze_code(target)
