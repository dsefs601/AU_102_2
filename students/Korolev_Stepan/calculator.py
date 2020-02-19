from ply import lex
import ply.yacc as yacc

tokens = (
    'LPAREN',
    'RPAREN',
    'SEPARATOR',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'NUMBER',
    'FACTORIAL',
    'U',
)

t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_FACTORIAL = r'!'
t_SEPARATOR = r','
t_U = r'U'


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('left', 'FACTORIAL'),
    ('nonassoc', 'UMINUS', 'U')
)


def p_add(p):
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]


def p_sub(p):
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]


def p_expr2uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]


def p_mult_div(p):
    '''expr : expr TIMES expr
            | expr DIV expr'''

    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        if p[3] == 0:
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]


def p_expr2NUM(p):
    'expr : NUMBER'
    p[0] = p[1]


def p_factorial(p):
    'expr : FACTORIAL expr'
    x = 1
    for i in range(2, p[2] + 1):
        x *= i
    p[0] = x


def p_u(p):
    'expr : U LPAREN NUMBER SEPARATOR NUMBER RPAREN'
    p[0] = p[3]**p[5]


def p_parens(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc(debug=False, write_tables=False)

res = parser.parse("(1+U(3,5)*7)/5")  # the input
print(res)
