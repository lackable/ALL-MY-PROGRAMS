hunger_status = str(input("are you hungry?"))

if  hunger_status == "yes" or hunger_status == "Yes":
    print('Please feed!')

elif hunger_status == "no" or hunger_status == 'No':
    print("your tummy is full :)")

else:
    print("you have entered an invalid value, Please enter 'Yes' or 'No'")
   
    
