def filterList(n):
    """
    Create a new list called filtered_list that contains only the integers from the list n.
    
    :param n: a list of any type
    :return: [1, 3, 7]
    """
    filtered_list = [var for var in n if type(var) is int] #filter out strings to only print int
    return filtered_list

myList = [1, 3, "cat", 7, "dog"]
print(filterList(myList))