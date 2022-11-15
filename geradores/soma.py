def generate():
    max_numbers = 10  # idealmente seria até 1000, mais que isso seria muito tempo a criar ficheiros
    #max até 10000

    for i in range(0, max_numbers + 1):
        for j in range(0, max_numbers + 1):
            filename = str(i) + "." + str(j)
            result = str(i + j)

            with open("../soma/" + filename, 'w') as fp:
                fp.write(result)

generate()
