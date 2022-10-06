from enum import Enum
from re import compile, IGNORECASE
from sre_constants import IN_IGNORE


ILLEGAL = 'ILLEGAL'
EOF = 'EOF'


class EQEnum(Enum):
    def __eq__(self, element: str) -> bool:
        if isinstance(element, str):
            return self.name == element
        else:
            return self.name == element.name
    
    def __hash__(self) -> int:
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

    #Arithmetic Operators
    PLUS = compile(r"\+")
    MINUS = compile(r"\-")
    MULT = compile(r"\*")
    DIVIDE_INT = compile(r"//")
    DIVIDE = compile(r"/")
    MODULO = compile(r"%")
    POWER = compile(r"\^")

    # Conditionnal Operators
    EQ = compile(r"\=\=")
    NEQ = compile(r"!\=")
    EQLOWER = compile(r"<\=")
    EQHIGHER = compile(r">\=")
    LOWER = compile(r"<")
    HIGHER = compile(r">")

    # Logical Operators
    AND = compile(r"&|and", IGNORECASE)
    OR = compile(r"\||or", IGNORECASE)
    NOT = compile(r"!|not", IGNORECASE)

    # Operators
    ASSIGN = compile(r"\=")

    # Keywords
    TRUE = compile(r"True")
    FALSE = compile(r"False")
    NONE = compile(r"None")

    IF = compile(r"if")
    ELSE = compile(r"else")
    ELIF = compile(r"elif")

    FOR = compile(r"for")
    IN = compile(r"in")
    WHILE = compile(r"while")

    DEF = compile(r"def")
    RETURN = compile(r"return")

    PRINT = compile(r"print")
    RANGE = compile(r"range")

    # Variables
    ID = compile(r"[_a-zA-Z][_a-zA-Z0-9]*")

    # Comments
    COMMENT = compile(r"#.*")

    # Delimiters
    COMMA = compile(r",")
    COLON = compile(r":")
    TAB = compile(r"    |\t")
    WHITESPACE = compile(r"(\ )+")
    NEWLINE = compile(r"(\n)+")


class TokenInfo:
    def __init__(self, token: Token, data: str) -> None:
        self.token = token
        self.data = data

    def get_token(self) -> Token:
        return self.token

    def get_data(self) -> str:
        return self.data
    
    def __repr__(self) -> str:
        return self.token
