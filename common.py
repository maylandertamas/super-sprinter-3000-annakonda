def get_table_from_file(file_name="stories.csv"):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(table, file_name="stories.csv"):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def ID_generator():
    table = get_table_from_file()
    max_value = ""
    for item in range(len(table)):
        for element in table:
            max_value = max(element)
    print(max_value)
    max_index = my_list.index(max_value)
    return None