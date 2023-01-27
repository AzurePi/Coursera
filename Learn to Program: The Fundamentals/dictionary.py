def invert_dict(d):
    '''(dict) -> dict

    Return a new dictionary where the keys in the new dictionary are the
    values from d, and the values are lists of the keys that are associated
    with those values from d.
    
    Precondition:  d's values are immutable
    
    >>> invert_dictionary({"cherry": "red", "pomegranate": "red"})
   {'red': ['cherry', 'pomegranate']}
   '''
    new_dict = {}
    
    for key in d:
        new_key = d[key]

        #If new_key is not already in the dictionary, add it with its value
        #being a single element: a list consisting of value key.
        if not (new_key in new_dict):
            new_dict[new_key] = [key]

        #If new_key is already in new_dict, append the value key to the list
        #of values associated with new_key.
        else:
            new_dict[new_key].append(key)

    return new_dict

def read_grades(gradefile):
    ''' (file open for reading) -> dict of {float: list of str}

    Reade the grades from gradefile and return a dictionary where each key
    is a grade and each values is the list of ids of studens who earned that
    grade.

    Precondition: gradefile starts with a header that contais no blank lines,
    then has a blank line, and the lines containing a student number and a grade.
    '''
    #Skip over the reader.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    #Read the grades and accumulate them into dict.
    grades_dict = {}
    line = gradefile.readline()
    
    while line != '':
        
        student_id = line[:4]
        grade = float(line[4:].strip())

        if grade not in grades_dict:
            grades_dict[grade] = [student_id]
        else:
            grades_dict[grade].append(student_id)

        line = gradefile.readline()

    return grades_dict
        
            
