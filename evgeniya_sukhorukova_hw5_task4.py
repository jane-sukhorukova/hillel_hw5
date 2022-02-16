list_of_methods = dir(set)
counter = 0

while counter < len(list_of_methods):
    if '_' in list_of_methods[counter]:
        list_of_methods.pop(counter)
    else:
        counter += 1

print(list_of_methods)

