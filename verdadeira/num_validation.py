def is_valid_number(num):
    # inteiro
    if num.isdigit():
        return True
    # decimal
    else:
        try:
            dec = float(num)
            return True
        except ValueError:
            return False


def is_valid_element(elem):
    #operadores a mais
    if elem.strip() == "":
        return False

    chars = "0123456789%"
    # 123
    if is_valid_number(elem):
        return True
    # 12%
    elif is_valid_number(elem[:-1]) and elem[-1] in chars:
        return True
    # sqrt(12)
    elif elem[:5] + elem[-1] == "sqrt()" and is_valid_number(elem[5:-1]):
        return True
    else:
        return False


def negative_check(expression):
    temp = expression
    i = 0
    while i < len(expression):
        if temp[i] == '-':
            if i == 0:
                temp = "0" + temp
                continue
            elif temp[i - 1] is "(":
                temp = temp[:i] + "0" + temp[i:]
                continue

        i = i + 1

    return temp


def percentage_check(expression, number_list):
    if len(number_list) is not 2 or expression[len(expression) - 1] is not '%':
        return expression

    temp = expression

    for i in range(len(expression)):
        if expression[i] in "+-/*":
            num1 = expression[:i]
            op = expression[i]
            num2 = expression[i + 1:-1]

            try:
                percentage_result = (float(num2) / 100) * (float(num1))
                temp = num1 + op + str(percentage_result)
            except:
                break

    return temp

