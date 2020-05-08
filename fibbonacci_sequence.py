def fibbonacci_sequence(x):
    """
    This program gets the list of a fibbonacci sequence of zero to any number desired by the user
    
    fibbonacci_sequence(7), gives:
    >>>[0, 1, 1, 2, 3, 5, 8, 13]
    """
    #creating the first and second terms in a fibbonacci sequence 
    prev_num = 0
    next_num = 1
    
    #Creating a list for the sequence and assigning the first and second term to the list
    list_Fibnum = [prev_num, next_num]
    
    #creating a counter
    count = 1
    
    if count < x :
        while count < x:
            nth_num = next_num + prev_num
            list_Fibnum.append(nth_num)
            prev_num = next_num
            next_num = nth_num
            count += 1
        return list_Fibnum
        
    elif x == 1:
        return list_Fibnum
    
    elif x == 0:
        return 0
    
    else: 
        print ('Run the program again, using x as an integer')
            

        
