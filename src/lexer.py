from rply import LexerGenerator


class Lexer():
    """Lexer for the L programming language"""
    def _init_(self):
        self.lexer = LexerGenerator()
    
    def _add_tokens(self):
        # Print statement
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAR', r'\(')
        self.lexer.add('CLOSE_PAR', r'\)')
        # semi-colon
        self.lexer.add('SEMI_COLON', r'\;')