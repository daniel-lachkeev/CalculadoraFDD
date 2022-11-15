import re


def split_expression(expression):
    temp = re.split('\+|-|\/|\*|\^', expression)
    for i in range(len(temp)):
        temp[i] = temp[i].replace("^", "**") \
            .replace("sqrt(", "") \
            .replace("(", "") \
            .replace(")", "")

    return temp
