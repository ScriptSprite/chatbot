#initialise message
print('''
Wecome to UniBudyy! Your all-in-one app that makes your freshman journey a bit
easier to navigate!
        Please enter your credentials to get started!: 
    ''')

#Getting and storing user input
name = input("What is your name?: ")
country = input("Where are you from?: ")
age = input("How old are you?: ")
colour = input("What is your favourite colour?: ")

#Use stored input to create personalised respones
print(f"""
Welcome {name}! I see that your favourite colour is {colour}.
I have a few suggestions based on your choice! 
 
""")
print("You are from {}, that's a great place.".format(country))

#Control structures and while loops

age = int(input("How old are you?: "))   
if age < 18:
    print("Wow!You are starting university at a young age!You must be really talented")
elif age > 25 and age < 35:
    print("Hm, you're much older then I expected")   
elif age > 35:
    print("That's fantastic! It's never too late to learn and grow")
else:
    print("{} is a fun age to start university at!".format(age))
    
    
print(f"""
Welcome{name}! I see that your favourite colour is {colour}.
I have a few suggestions based on your choice! 
 
""")

if colour == 'Red':
    print("If you like the colour RED, I have the following for you! Check out:  ")
    print("""
1. Our red colour themed football club.
2. Our red themed art club.
3. Our vampire themed society.    
4. Our twillight themed society.      
""")
    
elif colour == 'Blue':
    print("If you like the colour RED, I have the following for you! Check out:  ")

    print("""
1. Our fighting game club, where you can throw digital hands.
2. Our swimming club which include activites such as : aqua aerobics.
3. Our blue themed art club.
4. Our deep sea exploration club.
5. Our bird watching society.      
""")
    
elif colour == 'Yellow':
    
    print("If you like the colour YELLOW, I have the following for you! Check out:  ")

    print("""
1. Our werewolf society.
2. Our hiking club.
3. Our mountain climbing club.
4. Our dance club.
5. Our suntan society.      
""")
       
else:
    print("I am not sure if that's a colour")
    
    
#FAQ

question = input("Is there anything you would like to ask me? (Type in q to quit)")
    