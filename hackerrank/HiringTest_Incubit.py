eachLine = input()

iteration_pending = sum([ int(i) for i in eachLine.split(" ")])
# print(iteration_pending)

hierarchy_tracker = ""
property_dict = {}


def process_each_tag_line(eachLine = None, my_elements = None):
    if my_elements == None:
        my_elements = eachLine.split(' ')
    for index, each_element in enumerate(my_elements):
        if each_element == '=':
            property_dict[hierarchy_tracker + "~" + my_elements[index - 1]] = my_elements[index + 1][1:-2]
            #print("For:: ", property_dict)
    #print("Final:: ", property_dict)


for i in range(iteration_pending):
    eachLine = input()
    #print("####", eachLine)
    if eachLine.startswith("</"):
        hierarchy_tracker = ".".join(hierarchy_tracker.split(".")[:-1])
        process_each_tag_line(eachLine = eachLine)
    elif eachLine.startswith("<"):
        my_elements = eachLine.split(' ')
        hierarchy_tracker += "."+my_elements[0][1:]
        process_each_tag_line(my_elements=my_elements)
    else:
        print(property_dict.get("."+eachLine, "Not Found!"))

