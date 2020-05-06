file_name = 'text.txt'

linelist = []
with open(file_name) as file_object:
#    for line in file_object:
#        print(line.rstrip())

#    print(file_object.read())

#    for line in file_object:
#        linelist.append(line.rstrip())
#print(linelist)

    for line in file_object:
        print(line.replace('python', 'P').rstrip())
