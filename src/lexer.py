from rply import LexerGenerator


class Lexer():
    """Lexer for the I programming language"""
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
        # quotes
        self.lexer.add('DOUBLE_QUOTES', r'\"')
        self.lexer.add('SINGLE_QUOTES', r'\'')
        # Operations
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('EXP', r'\^')
        # comments
        self.lexer.add('COMMENTS', r'\/\/')
        # ignore whitespaces
        self.lexer.ignore('\s+')
