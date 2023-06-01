print("To start your quiz firstly,enter your name?")
name=input("What is your name?")
print(f"So your name is {name}")
play=input(f"Do you want to play {name}?")

if play.lower()!="yes":
    print("Thank you for your response!")
    quit()
else :       
    print("Welcome to Quiz Ishan?")   
    score =0
    answer=input("what is the full form of WWW?") 
    if answer=="world wide web":
        score +=1
    else:
       pass
    
    answer=input("What is the fullform of RAM?")
    if answer=="random access memory":
        score +=1
    else:
        pass
        
    answer=input("What is the fullform of ROM?")
    if answer=="read only memory":
        score +=1
    else:
        pass

    if score>0:
        print("Passed!")
        print("Hence, you have successfully correct",str(score),"questions.")
    else:
        print("Fail,you haven't even correct any questions")         
    
  
     
        