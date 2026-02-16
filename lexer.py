import ply.lex as lex

# List of tokens required by the project
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'EQUALS', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
    'SEMI', 'INT', 'WHILE', 'IF', 'ELSE'
)

# Regular expressions for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'

# Rule for keywords and identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    reserved = {
        'int': 'INT',
        'while': 'WHILE',
        'if': 'IF',
        'else': 'ELSE'
    }
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Lexical Error: Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()