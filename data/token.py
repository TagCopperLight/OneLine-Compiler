from enum import Enum
from re import compile


ILLEGAL = 'ILLEGAL'
EOF = 'EOF'


class EQEnum(Enum):
    def __eq__(self, element: str) -> bool:
        if isinstance(element, str):
            return self.name == element
        else:
            return self.name == element.name
    
    def __hash__(self):
        return id(self.name)


class Token(EQEnum):
    # Data types
    STRING = compile(r"(\".*\")|(\'.*\')")
    INT = compile(r"\d+")
    FLOAT = compile(r"\d+\.\d+")
    
    # Brackets
    L_ROUND = compile(r"\(")
    R_ROUND = compile(r"\)")
    L_SQUARE = compile(r"\[")
    R_SQUARE = compile(r"\]")
    L_CURLY = compile(r"\{")
    R_CURLY = compile(r"\}")

    # Operators
    ASSIGN = compile(r"\=")
    PLUS = compile(r"")
    MINUS = compile(r"")
    MULT = compile(r"")
    DIVIDE = compile(r"")
    DIVIDE_INT = compile(r"")
    MODULO = compile(r"")
    POWER = compile(r"")

    # Logical Operators
    AND = compile(r"")
    OR = compile(r"")
    NOT = compile(r"")

    # Conditionnal Operators
    EQ = compile(r"")
    NEQ = compile(r"")
    LOWER = compile(r"")
    HIGHER = compile(r"")
    EQLOWER = compile(r"")
    EQHIGHER = compile(r"")

    # Keywords
    TRUE = compile(r"")
    FALSE = compile(r"")
    NONE = compile(r"")
    IF = compile(r"")
    ELSE = compile(r"")
    FOR = compile(r"")
    WHILE = compile(r"")
    DEF = compile(r"")
    RETURN = compile(r"")
    PRINT = compile(r"")

    # Variables
    ID = compile(r"")

    # Comments
    COMMENT = compile(r"")

    # Delimiters
    COMMA = compile(r"")
    WHITESPACE = compile(r"")


class TokenInfo:
    def __init__(self, token: Token, data: str) -> None:
        self.token = token
        self.data = data

    def get_token(self) -> Token:
        return self.token

    def get_data(self) -> str:
        return self.data
