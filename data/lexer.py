from data.token import Token, TokenInfo

class Lexer:
    def __init__(self) -> None:
        self.data = ''

    def lexerGenerator(self) -> TokenInfo:
        pos = 0

        while pos < len(self.data):
            for token_id in Token:
                if match := token_id.value.match(self.data, pos):
                    pos = match.end(0)

                    if token_id == Token.WHITESPACE or token_id == Token.COMMENT:
                        break
                    
                    yield TokenInfo(token_id.name, match.group(0))
                    break

            else:
                yield TokenInfo(Token.ILLEGAL, self.data[pos])
                pos += 1
        else:
            yield TokenInfo(Token.EOF, '\x00') 
            yield TokenInfo(Token.EOF, '\x00')

    def set_data(self, data: str) -> None:
        self.data = data
