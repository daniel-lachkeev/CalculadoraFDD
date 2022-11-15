import math

def generate():
    max_numbers = 100

    for i in range(0, max_numbers + 1):
            filename = str(i)
            result = str(math.sqrt(i))

            with open("../sqrt/" + filename, 'w') as fp:
                fp.write(result)

generate()
