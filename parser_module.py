import ply.yacc as yacc
from lexer import tokens

# --- Phase 3.3: Symbol Table & Semantic Analysis ---
# This dictionary tracks your variables.
symbol_table = {}

# --- Phase 3.4: Intermediate Code Generation State ---
# This counter helps create temporary variables like t1, t2, etc.
temp_count = 0

def get_new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

# --- Grammar Rules ---

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    '''statements : statement statements
                  | statement'''
    pass

# Declaration Rule: int x;
def p_declaration(p):
    'statement : INT ID SEMI'
    var_name = p[2]
    if var_name in symbol_table:
        print(f"SEMANTIC ERROR: Variable '{var_name}' already declared.")
    else:
        symbol_table[var_name] = 'int'
        print(f"SYMBOL TABLE: Added '{var_name}'")

# Assignment Rule: x = 10 + 5;
def p_assignment(p):
    'statement : ID EQUALS expression SEMI'
    if p[1] not in symbol_table:
        print(f"SEMANTIC ERROR: Variable '{p[1]}' used before declaration.")
    else:
        # Phase 3.4: Generate Intermediate Code for Assignment
        print(f"INTERMEDIATE CODE: {p[1]} = {p[3]}")

# Expression Rule: Handling Math Operations
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    
    op = p[2]
    new_temp = get_new_temp()
    
    # Phase 3.4: Generate 3AC for operations
    print(f"INTERMEDIATE CODE: {new_temp} = {p[1]} {op} {p[3]}")
    p[0] = new_temp

# Expression Rule: Handling Numbers and Variables
def p_expression_factor(p):
    '''expression : NUMBER
                  | ID'''
    p[0] = p[1]

# Error Handling
def p_error(p):
    if p:
        print(f"SYNTAX ERROR at token {p.type} ('{p.value}')")
    else:
        print("SYNTAX ERROR: Unexpected end of input")

# Build the parser
parser = yacc.yacc()