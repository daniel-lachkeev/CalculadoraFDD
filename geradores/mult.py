def generate():
    max_numbers = 10  # para efeitos de teste no github é até 10
    #idealmente seria 1000 no max até 10000, mas a quantidade de ficheiros a criar seria absurda

    for i in range(0, max_numbers + 1):
        for j in range(0, max_numbers + 1):
            filename = str(i) + "." + str(j)
            result = str(i * j)

            with open("../mult/" + filename, 'w') as fp:
                fp.write(result)

generate()
