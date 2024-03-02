from rply import ParserGenerator
from Abstact_syntax_tree import *

class Parse():
    """Parser for i"""
    def __init__(self) -> None:
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSED_PAREN', 'SEMI_COLON',
             'COMMENTS', 'ADD', 'SUB', 'MUL']
        )
    
    def parse(self):
        @self.pg.production('output : PRINT OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def output(p):
            return Print[p[2]]
        
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'ADD':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
        
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
        
        @self.pg.production('comment : COMMENTS comment')
        def comment(p):
            return Comment()
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
    
    def get_parse(self):
        return self.pg.build()
