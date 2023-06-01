try:
      name=input("please enter your name?")
      if name.lower()=="ishan":
          print("you r ready to vote? beacuse your name is matching! ")
          while True:
           try:
            hello=int(input("Please input your age"))
            if hello>17:
              print("your are ready to vote and age is",hello)
              break
            else:
              print("You are not ready to vote")
              continue
            #If not you enter your age and go to the second loop
             
           except Exception as e:
            print(e)
            print("please enter only numbers")
            continue
            break  #This break is used for while loop
   
           else:
            print("Not validate your name")
           continue
except Exception as e:
            print(e)  
            
          