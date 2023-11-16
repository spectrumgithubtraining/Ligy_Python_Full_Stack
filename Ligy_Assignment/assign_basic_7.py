a = int(input ("Please, Enter the Lowest  Value: "))  
b = int(input ("Please, Enter the Upper  Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (a, b + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)