# Calculadora F_DIDA
# @Daniel Lachkeev

import verdadeira.util as util
import verdadeira.num_validation as valid


def read_result(filename):
    try:
        with open(filename, "r") as f:
            return f.readline()
    except FileNotFoundError:
        return "Este número não está disponível ainda!"


def find_result(num1, num2, op):
    # encontrar ficheiro
    if op == "sqrt":
        return read_result("sqrt/" + str(num1))
    else:
        return read_result(op + "/" + str(num1) + "." + str(num2))
    # retornar o conteudo do ficheiro


def new_version():
    print('''
    - Usar números até 1 milhão!
    - Cálculos com números reais até 3 casas decimais!
    - Contas com percentagens
    - Múltiplas contas ao mesmo tempo e encadeamento!!
    - Melhor performance
    - Números negativos!!!
    ''')


def menu():
    print("Escolha o tipo de conta a fazer:")
    print("Escreva 'about' para descobrir as novas funcionalidades futuras e fantásticas para a versão 2.0")

    while True:
        print('''
            0: Sair do programa
            1: + - / * ^       
            2: Raiz quadrada''')
        option = input("> ")

        try:
            if "quit" in option or "exit" in option:
                break

            if "about" in option:
                new_version()
                continue

            option = int(option)
            if option == 0:
                break
            elif option == 1:
                calc()
            else:
                square_root()
        except ValueError:
            print("Use só opções entre 0 e 2")


def wrong_number(num):
    try:
        temp = int(num)
        if temp < 0 or temp > 10000:
            print("Este número não está disponível ainda!")
            return -1
        else:
            return temp
    except ValueError:
        print("Insira um número inteiro entre 0 e 10000")
        return -1


def square_root():
    print("Escreva 'back' para ir de volta ao menu")
    print("Insira um número para fazer a raíz quadrada")
    print("> ", end='')
    expression = "".join(input().split())  # retira o whitespace inteiro

    if "back" in expression:
        return

    try:
        temp = int(expression)
        print(find_result(temp, None, "sqrt"))
    except ValueError:
        print("Use só números inteiros entre 0 e 10000. Na v2.0 já vai poder usar números decimais.")


def calc():
    print("Escreva 'back' para ir de volta ao menu")
    print("Insira o primeiro número")
    num1 = input("> ")

    if "back" in num1:
        return

    num1 = wrong_number(num1)

    if num1 == -1:
        return

    print("Insira o operador:")
    print("+ - * / ^")
    chars = "+-*/^"

    op = input("> ")

    if len(op) != 1 or op not in chars:
        print("Operador Inválido")
        return

    print("Insira o segundo número")
    num2 = input("> ")
    num2 = wrong_number(num2)

    if num2 == -1:
        return

    try:
        if op == '+':
            print(find_result(num1, num2, "soma"))
        elif op == '-':
            print(find_result(num1, num2, "sub"))
        elif op == '*':
            print(find_result(num1, num2, "mult"))
        elif op == '/':
            print(find_result(num1, num2, "div"))
        else:
            print("Erro desconhecido")
    except ValueError:
        print("Use só números inteiros entre 0 e 10000. Na v2.0 já vai poder usar números decimais.")


if __name__ == '__main__':
    print('''
   _____      _            _           _                 ______ _____  _____  
  / ____|    | |          | |         | |               |  ____|  __ \|  __ \ 
 | |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _| |__  | |  | | |  | |
 | |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |  __| | |  | | |  | |
 | |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | |    | |__| | |__| |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|_|    |_____/|_____/   v1.0
  
  Bem vindo a melhor calculadora do mundo!                                    

    ''')
    menu()
