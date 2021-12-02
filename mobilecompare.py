import random
import time
import turtle

''' This program asks users to comapre various specifications of mobiles.
    Then provides their current battery charge(s).
    Further, it prints a countdown and shows an appropriate battery charge of each mobile(s), 5 hours later.
'''

#This defines a countdown by importing the time Library
def countdown(time_min): #SOB32
    while time_min:
        mins, secs = divmod(time_min, 60)
        timeformat = '{:02d}:00'.format(secs, mins)
        print(timeformat, end='\r')
        time.sleep(1)
        time_min -= 1

    print("5 Hours Later...", end= "\n\n\n")

def t():
    win = turtle.Screen()
    win.bgcolor("white")
    win.title("See You Soon...")

    turtle.color('#808080')
    style = ('Arial', 80)
    turtle.write('Goodbye! :)', font=style, align='center')
    turtle.hideturtle()

#This imports the classes from Mobile Library
from devices import * #SOB35

print("| Mobile Specifications And Battery Compare | ", end="\n\n\n")

#Loop starts here
while True:
    #These are the choices 
    mobile1 = Mobile('Samsung', 'S20', '2020','Red', 12, 256,5000, 100, 4 )
    mobile2 = Mobile('Apple', 'iPhone 13', '2021','Grey',8, 128, 4352, 100, 2 )
    mobile3 = Mobile('Apple', 'iPhone 13 Mini', '2021','Blue',4, 128, 2438, 100, 2 )
    mobile4 = Mobile('Xiaomi', 'Mi 10 Ultra', '2020','Black',12, 512, 4500, 100, 4 )      
    mobile5 = Mobile('Oppo', 'Find X3 Pro', '2021','Deep Blue',12, 256, 4500, 100, 4 )    

    #These are the set values for random numbers, by importing Random
    n1 = random.randint(65, 74) #SOB33
    n2 = random.randint(45, 64)
    n3 = random.randint(15, 34)
    n4 = random.randint(50, 64)
    n5 = random.randint(48, 64)

    #Gets inputs From the User
    choice = input("How Many Smartphones do you want to compare? [1-5] ")
    print("") #Blank Line

    #Checks Whether the Choice is True 
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            print("")
            print('Android: ' + mobile1.__str__()) #SOB34
            for i in reversed(range(n1,100)):
                mobile1.reduce()
            countdown(5)
            print('Android: ' + mobile1.__str__())

        elif choice == '2':
            print("")
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            for i in reversed(range(n1,100)):
                mobile1.reduce()
            for i in reversed(range(n2,100)):
                mobile2.reduce()
            countdown(5)
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())

        elif choice == '3':
            print("")
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())
            for i in reversed(range(n1,100)):
                mobile1.reduce()
            for i in reversed(range(n2,100)):
                mobile2.reduce()
            for i in reversed(range(n3,100)):
                mobile3.reduce()
            countdown(5)
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())

        elif choice == '4':
            print("")
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())
            print('Android: ' + mobile4.__str__())
            for i in reversed(range(n1,100)):
                mobile1.reduce()
            for i in reversed(range(n2,100)):
                mobile2.reduce()
            for i in reversed(range(n3,100)):
                mobile3.reduce()
            for i in reversed(range(n4,100)):
                mobile4.reduce()
            countdown(5)
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())
            print('Android: ' + mobile4.__str__())

        elif choice == '5':
            print("")
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())
            print('Android: ' + mobile4.__str__())
            print('Android: ' + mobile5.__str__())
            for i in reversed(range(n1,100)):
                mobile1.reduce()
            for i in reversed(range(n2,100)):
                mobile2.reduce()
            for i in reversed(range(n3,100)):
                mobile3.reduce()
            for i in reversed(range(n4,100)):
                mobile4.reduce()
            for i in reversed(range(n5,100)):
                mobile5.reduce()
            countdown(5)
            print('Android: ' + mobile1.__str__())
            print('iOS: ' + mobile2.__str__())
            print('iOS: ' + mobile3.__str__())
            print('Android: ' + mobile4.__str__())
            print('Android: ' + mobile5.__str__())

        #This is a confirmation message to repeat or break the loop
        confirm = input("Wanna Go Again? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break

    #This is the error message if values are invalid    
    else:
        print("Error, Invalid Input!  o_O  .....!!!!!.....!!!!!.....!!!!!.....!!!!!.....!!!!!.....!!!!!..... ", end='\n\n')
