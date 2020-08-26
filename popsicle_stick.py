! python3
#this Program randomly chooses a number assigned to a student
#Marc Leon
import random

print('***********************Popsicle Stick Simmulator*************************')
print('=========================================================================')




#TODO: create a class that allows you to put the students name into a dictionary


#class_dict = {}

while True:
    try:
        stud_num = int(input('Enter the number of students in class today: '))
    except ValueError:
        print('Sorry, you must enter an integer with no decimals or letters.  ')
    except NameError:
        print('Sorry, The program only accepts numbers.  ')
        raise
    if stud_num == 0:
        print('The popsicle stick program has terminated')
        break
    else:
        num = (stud_num + 1)
        stick = random.randint (1, num)

        print("                                  *")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                * " + str(stick)  + "*    ")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                *   *")
        print("                                  * ")


        print('Please answer the question ' + 'student number ' + str(stick) + '.  ')
