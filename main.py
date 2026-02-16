from parser_module import parser

# Phase 4: Testing and Validation
# This code contains one valid declaration and one semantic error (y is not declared)
test_code = """
int x;
x = 10 + 5;
y = 20;
"""

print("--- Starting MiniLang Compiler ---")
parser.parse(test_code)
print("--- Compilation Finished ---")