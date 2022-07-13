"""
    It takes a number, converts it to a list of digits, sorts the list in descending order, and then
    converts the list back to a number
    
    :param num: The number to be ranked
    """


def descending_order(num):  #Function to generate largested possible number with largest possibel number

    myList = [int(a) for a in str(num)]
    #sort the list un descending order
    myList.sort(reverse=True)

    n = len(myList)

    #initiliaze num starting element of the list
    num1 = myList[0]

    

    #generate the number
    for i in range(1, n):
        num1 = num1 * 10 + myList[i]
    print(num1)

descending_order(12987654356)
        



