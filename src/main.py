from lexer import Lexer
from parse import Parse

text_input = """
print(4 + 4 - 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parse()
pg.parse()
parser = pg.get_parse()
parser.parse(tokens).eval()


