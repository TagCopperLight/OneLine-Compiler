from data.lexer import Lexer

def main():
    lexer = Lexer()
    data = """a = 25\nfor a in range(34):\n\tprint("salut)"""
    lexer.set_data(data)

    token_list = [i for i in lexer.lexerGenerator()]

    print(token_list)
    

if __name__ == "__main__":
    main()
