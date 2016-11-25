def DescendingOrder(num):
    myList = []
    for digit in str(num):
        myList.append(int(digit))
    spinList = int(''.join(map(str,(sorted(myList,reverse=True)))))
    print(spinList)
    return spinList

