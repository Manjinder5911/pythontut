


def soldier(path_input,dictionary_file,format):
    import os
    os.chdir(path_input)
    files = os.listdir(path_input)

    i = 1
    f = open(dictionary_file)
    filename = f.read().split("\n")

    for item in files:
        if item not in filename:
            os.rename(item,item.capitalize())
        if os.path.splitext(item)[1] == format:
            os.rename(item, f"{i}{format}")
        i += 1

# path_input = input("enter path name : \n")
# dictionary_file = input("enter file name : \n")
# format = input("enter file format to be renamed : \n")
soldier(r"C:/Users/HP/Desktop/testing",r"C:\Users\HP\PycharmProjects\firstprog\log.txt",".xlsx")
