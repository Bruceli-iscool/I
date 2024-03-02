from rply import ParserGenerator
from Abstact_syntax_tree import *


class Parse():
    """Parser for i"""
    def __init__(self) -> None:
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSED_PAREN', 'SEMI_COLON',
             'COMMENTS', 'SUM', 'SUB', 'MUL']
            )
    
    def parse(self):
        @self.pg.production('output : PRINT OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def output(p):
            return Print[p[2]]
        
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]