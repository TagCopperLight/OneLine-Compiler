from data.token import Token, TokenInfo, ILLEGAL, EOF

class Lexer:
    def __init__(self) -> None:
        self.data = ''

    def lexerGenerator(self) -> TokenInfo:
        pos = 0

        while pos < len(self.data):
            for token in Token:
                if match := token.value.match(self.data, pos):
                    pos = match.end(0)

                    if token == Token.WHITESPACE or token == Token.COMMENT:
                        break
                    
                    yield TokenInfo(token.name, match.group(0))
                    break

            else:
                yield TokenInfo(ILLEGAL, self.data[pos])
                pos += 1
        else:
            yield TokenInfo(EOF, '\x00') 
            yield TokenInfo(EOF, '\x00')

    def set_data(self, data: str) -> None:
        self.data = data
