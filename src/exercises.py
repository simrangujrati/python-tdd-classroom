def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    l=[]

    for i in range(len(input_list)-1,-1,-1):
    	l.append(input_list[i])
    return l

def count_digits(number):
    """
    Return count of digits
    """
    return len(str(number))