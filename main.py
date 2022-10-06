from data.lexer import Lexer
import os

os.system('cls')

def main():
    lexer = Lexer()

    with open('data/test.py', 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
        
    lexer.set_data(data)

    token_list = [i for i in lexer.lexerGenerator()]

    print(data)
    print(token_list)
    

if __name__ == "__main__":
    main()
