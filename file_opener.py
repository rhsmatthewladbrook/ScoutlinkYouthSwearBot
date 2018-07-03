def get_split_file(file_name):
    file = open(file_name, "r")
    contents = file.read()
    output = contents.split("\n")
    file.close()
    return output

def add_line(file_name, line_to_add):
    file = open(file_name, "r")
    contents = file.read()
    file.close()
    file = open(file_name, "w+")
    file.write("{}\n{}".format(contents, line_to_add))
    file.close()

def remove_line(file_name, line_to_remove):
    contents = get_split_file(file_name)
    contents.remove(line_to_remove)
    file = open(file_name, "w+")
    file.write("\n".join(contents))
    file.close()
