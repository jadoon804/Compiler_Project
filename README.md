# Compiler Construction Project: Symbol Table & Parser

## Description
This project implements a lexical analyzer and parser as part of the Compiler Construction curriculum. It accepts source code input, generates a symbol table, and produces intermediate code (Three-Address Code).

## Features
- **Symbol Table Generation:** Tracks variable declarations.
- **Intermediate Code Generation:** Outputs `t1 = a + b` style logic.
- **Parse Tree:** Validates the grammatical structure of the input.

## How to Run

1. **Compile the project:**
   ```bash
   lex scanner.l
   yacc -d parser.y
   gcc lex.yy.c y.tab.c -o my_compiler