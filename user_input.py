while (true):    
 try:
    num1=int(input("Enter the first number"))
    num2=int(input("enter the second number"))
    sum=num1/num2

 except ZeroDivisionError as e:
    print(e)      
    print("Any number doesnot divide by 0")  
    
 except ValueError as e:
    print(e)      
    print("please enter the numbers")      

    
 except Exception as e:
    print(e)      
    print("Error is occured")
 
else:
     print("Sum of the number is",sum)    
    

