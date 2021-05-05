def spiralize(size, n):
    x = n  # starting point and number we are at in spiral
    counter = 0  # variable to keep track how many corners we are at
    i = 2  # increments that get added to starting point
    total = 0  # sum of the corners

    if (size ** 2 < x):
        return n
    
    while ( x <= size ** 2):  # main loop to build spiral up to the size^2
        total += x
        #print('total: ' + str(total))
        x += i  
        #print('x: ' + str(x))
        counter += 1  
        #print('counter: ' + str(counter)) 
        if (counter == 4):  
            i += 2  
            counter = 0 
            #print('***************RESET*******************')
            #print('i= ' + str(i))
        
    total += x

        
    
    if (4 > counter > 0): ## loop to see if a full spiral is needed to complete the total equal to tests
        while (counter < 4):
            total += x 
            #print('looper total: ' + str(total))
            x += i
            #print('looper x: ' + str(x))
            counter += 1 
           # print('looper counter: ' + str(counter)) 
        #total += x 

    return total


#print(spiralize(11,27))