
#initialise message
print('''
Wecome to UniBudyy! Your all-in-one app that makes your freshman journey a bit
easier to navigate!
        Please enter your credentials to get started! 
    ''')

#Getting and storing user input
user_name = input("What is your name?: ")
user_age = int((input("How old are you?: ")))
user_colour = input("What is your favourite colour?: ").lower()
user_faculty = input("What faculty are you studying?: ").lower()

#Use stored input to create personalised respones
print(f"""
Welcome {user_name}! I see that your favourite colour is {user_colour}.
I have a few suggestions based on your choice! 
 
""")

if user_faculty == 'math':
    print("That is a very hard but rewarding faculty. Keeping my fingers crossed.")
elif user_faculty == 'psychology':
    print("Human's mind is so interesting. I am sure you'll love it.")
elif user_faculty == 'computer science':
    print("Perfect choice. This is what I studied. Good luck.")
else:
    print("I am not sure we have this faculty.Choose from: math, psychology and computer science.")
    

if user_colour == 'red':
    print("If you like the colour RED, I have the following for you! Check out:  ")
    print("""
1. Our red colour themed football club.
2. Our red themed art club.
3. Our vampire themed society.    
4. Our twillight themed society.      
""")
    
elif user_colour == 'blue':
    print("If you like the colour BLUE, I have the following for you! Check out:  ")

    print("""
1. Our fighting game club, where you can throw digital hands.
2. Our swimming club which include activites such as : aqua aerobics.
3. Our blue themed art club.
4. Our deep sea exploration club.
5. Our bird watching society.      
""")
    
elif user_colour == 'yellow':
    
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
    


#Control structures and while loops


if user_age < 18:
    print("Wow!You are starting university at a young age!You must be really talented")
elif user_age > 25 and user_age < 35:
    print("Hm, you're much older then I expected")   
elif user_age > 35:
    print("That's fantastic! It's never too late to learn and grow")
else:
    print("{} is a fun age to start university at! Good luck".format(user_age))
    
    

    
    
#FAQ ; Frequently used question

question = input("Is there anything you would like to ask me? (Type in q to quit: )")

if question == 'How is your day?':
    print("I exist so my day is going well!")
elif question == 'Who can help me with my curriculum form?':
    print("You can speak to your course advisor or an Orientation Leader.")
elif question == 'What clubs does the university offer?':
    print('The university offers a wide range of clubs')
elif question == 'Is there any good restaurants around campus?':
    print('Yes, my favourite is the Mexican Salsa next to the campus')
else:
    print("I am not sure if have an answer to this question.")
