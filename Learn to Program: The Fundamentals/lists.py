def shift_left(L):
    ''' (list) -> NoneType

    Shift each iten in L one position to the left and shift the first item
    to the last position.

    Precondition: len(L) >= 1

    >>> L = [13, 'love', 12.5]
    >>> shift_left(L)
    >>> L
    ['love', 12.5, 13]
    '''
    #Keeps track of the first item on the list.
    first_item = L[0]
    
    #Shifts characters to the left.
    for i in range(1, len(L)):
        L[i - 1] = L[i]

    #Shifts the last character to the end.
    L[-1] = first_item


def sum_items_while(list1,list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''
    #Keeps track of the list that will be returned
    new_list = []

    #Accumulates the index of the lists
    index = 0

    #Sums the corresponding items and puts the result in new_list
    while index <= len(list1)-1:
        new_list.append(list1[index]+list2[index])
        index = index + 1

    return new_list


def sum_items_for(list1,list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''
    sum_list = []

    for i in range(len(list1)):
         sum_list.append(list1[i] + list2[i])

    return sum_list


def averages(grades):
    ''' (list of list of number) -> list of float

    Return a list in which each item is the average of the numbers in the
    inner list at the corresponding position of grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''
    averages = []

    for grades_list in grades:
        #Calculate the average of grades_list and append it to averages.

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages
    
    
    
