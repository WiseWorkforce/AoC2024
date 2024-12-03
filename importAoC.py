import csv
def getInput(folder):
    return_lst = []
    file_to_open = folder + '/test.txt'
    return_lst.append(input_to_list(file_to_open))
    file_to_open = folder + '/input.txt'
    return_lst.append(input_to_list(file_to_open))
    return return_lst

def input_to_list(file_to_open):
    file = open(file_to_open, "r")
    data = list(csv.reader(file))
    file.close()
    return data

def getInputNotSplitted(folder):
    return_lst = []
    file_to_open = folder + '/test.txt'
    return_lst.append(input_not_splitted(file_to_open))
    file_to_open = folder + '/input.txt'
    return_lst.append(input_not_splitted(file_to_open))
    return return_lst

def input_not_splitted(file_to_open):
    file = open(file_to_open, "r")
    data = file.read()
    file.close()
    return data