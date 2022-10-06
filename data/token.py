from enum import Enum
from re import compile


class EQEnum(Enum):
    def __eq__(self, element) -> bool:
        if is_instance(b, str):
            return self.name == element
        else:
            return self.name == element.name
    
    def __hash__(self):
        return id(self.name)


class Token(EQEnum):
    # Specials
    ILLEGAL = 'ILLEGAL'
    EOF = 'EOF'

    # Data types
    STRING = compile("")
    INT = compile("")
    FLOAT = compile("")
    
    # Brackets
    L_ROUND = compile("")
    R_ROUND = compile("")
    L_SQUARE = compile("")
    R_SQUARE = compile("")
    L_CURLY = compile("")
    R_CURLY = compile("")

    # Operators
    PLUS = compile("")
    MINUS = compile("")
    MULT = compile("")
    DIVIDE = compile("")
    DIVIDE_INT = compile("")
    MODULO = compile("")
    POWER = compile("")

    # Logical Operators
    AND = compile("")
    OR = compile("")
    NOT = compile("")

    # Conditionnal Operators
    EQ = compile("")
    NEQ = compile("")
    LOWER = compile("")
    HIGHER = compile("")
    EQLOWER = compile("")
    EQHIGHER = compile("")

    # Keywords
    TRUE = compile("")
    FALSE = compile("")
    NONE = compile("")
    IF = compile("")
    ELSE = compile("")
    FOR = compile("")
    WHILE = compile("")
    DEF = compile("")
    RETURN = compile("")
    PRINT = compile("")

    # Variables
    ID = compile("")

    # Comments
    COMMENT = compile("")

    # Delimiters
    COMMA = compile("")
    WHITESPACE = compile("")


class TokenInfo:
    def __init__(self, token: Token, data: str) -> None:
        self.token = token
        self.data = data

    def get_token(self) -> Token:
        return self.token

    def get_data(self) -> str:
        return self.data
