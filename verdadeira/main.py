from math import sqrt
import util
import num_validation

def calc():
    while True:
        print("> ", end='')
        expression = "".join(input().split())  # retira o whitespace inteiro

        if "quit" in expression or "exit" in expression:
            break

        # negative check, adiciona 0 antes dos negativos caso segue a sintaxe correta
        expression = num_validation.negative_check(expression)

        # partir membros da expressão para validação de cada operando
        number_list = util.split_expression(expression)

        # validação dos operandos
        skip = False
        for num in number_list:
            if not num_validation.is_valid_element(num):
                print("Operação Inválida")
                skip = True
                break

        if skip:
            continue

        # transforma percentagens em quantidades reais caso segue a sintaxe correta
        expression = num_validation.percentage_check(expression, number_list)

        # ^ não é um operador válido com eval, é equivalente ao '**'
        formatted_expression = expression.replace("^", "**")
        try:
            print(eval(formatted_expression))
        except SyntaxError:
            print("Erro de sintaxe")
        except ZeroDivisionError:
            print("Divisão por zero")
        except ValueError:
            print("Indefinido")
        except:
            print("Erro genérico")


def intro():
    print("CalculadoraFDD (a verdadeira)")
    print("Operadores: + - / ^ sqrt(x) x%")
    print("Nota: Percentagens só funcionam com 2 números, ex: 100 + 10%")
    print("Escreva 'quit' ou 'exit' para sair")


if __name__ == '__main__':
    intro()
    calc()
