import re

class Lexer:
    #* Inicializador del analizador léxico
    def __init__(self, input_string):
        self.tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', input_string)
        self.current_token = None
        self.index = -1
    
    #* Obtención de la siguiente ficha léxica
    def get_next_token(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            return self.current_token
        else:
            return None

class Parser:
    #* Inicializador del analizador sintáctico 
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
    
    #* Analizador de la expresión usando en conjunto el analizador léxico y sintáctico
    def parse(self):
        self.current_token = self.lexer.get_next_token()
        if self.current_token is None:
            print("Error: La expresión está vacía")
            return False
        if not self.expresion():
            return False
        if self.current_token is not None:
            print("Error: Expresión incompleta")
            return False
        return True
    
    #* Función para verificar si el token actual coincide con el token esperado
    def match(self, token):
        if self.current_token == token:
            self.current_token = self.lexer.get_next_token()
            return True
        else:
            return False
    
    #* Analiza la expresión
    def expresion(self):
        if not self.termino():
            return False
        while self.match('+') or self.match('-'):
            if not self.termino():
                return False
        return True
    
    #* Analiza el término
    def termino(self):
        if not self.factor():
            return False
        while self.match('*') or self.match('/'):
            if not self.factor():
                return False
        return True
    
    #* Analiza el factor
    def factor(self):
        if self.match('('):
            if not self.expresion():
                return False
            if not self.match(')'):
                print("Error: Falta un paréntesis de cierre")
                return False
            return True
        elif self.current_token is not None and self.current_token.isdigit():
            return self.match(self.current_token)
        else:
            print("Error: Se esperaba un número o un paréntesis de apertura")
            return False


def main():
    #* Función principal del programa, verificando la validez de una expresión aritmética
    while True:
        expression = input("Ingrese una expresión aritmética (o 'exit' para salir): ")
        if expression.lower() == 'exit':
            break
        lexer = Lexer(expression)
        parser = Parser(lexer)
        if parser.parse():
            print("La expresión es sintácticamente válida.")
        else:
            print("La expresión contiene errores sintácticos.")

if __name__ == "__main__":
    main()
