#QUESTION 1

# getting input from the user and assigning it to user

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi = weight/(height**2) 
# ** is the power of operator i.e height*height in this case

print("Your BMI is: {0} and you are: ".format(bmi), end='')

#conditions
if ( bmi < 18.5):
   print("Underweight")

elif ( bmi >= 18.5 and bmi <= 24.9):
   print("Normal Weight")

elif ( bmi >= 25 and bmi <= 29.9):
   print("Overweight")

elif ( bmi >=30):
   print("Obesity")



#QUESTION 2
======

def start():
    print('When prompted you can continue and enter another set of three scores or exit the program')
    decision = 'unknown'
    # user has to type in 'yes' or 'no'
    while decision.lower() != 'yes' and decision.lower() != 'no':
        decision = input('Enter YES to begin program or NO to exit\n')
    while decision.lower() == 'yes':
        processScores()
        # Allow user to continue or exit
        decision = 'unknown'
        while decision.lower() != 'yes' and decision.lower() != 'no':
            decision = input('Enter YES to enter another set of scores or NO to exit\n')
def processScores():
    # Allow user to enter scores
    
    scores = [] #empty list
    
    while (len(scores) < 100): # input 100 scores
        newScore = input('Enter a valid score\n')
        if newScore.isdigit() and int(newScore) >= 1 and int(newScore) <=5 :
            newScore = int(newScore) # cast to integer
            scores.append(newScore) #add to list
        else:
            print('Invalid input. Please try again.')
            continue
        
        # calculate average
        if (len(scores) == 3):
            totalScores = 0 # initialize
            for i in scores: # get each element's value in scores list
                totalScores = totalScores + i #sum up the elements
                average = totalScores / 100
                
                #Score and Respondent
                listscore = scores
                one = listscore.count(1)
                two = listscore.count(2)
                three = listscore.count(3)
                four = listscore.count(4)
                five = listscore.count(5)
                sum_all=0
                sum_all = sum_all+one+two+three+four+five
                
                #print statement
                print('\033[4mScore\033[0m   \033[4mTotal number of respondent\033[0m')
                print("{0:15} {1}".format("1", one))
                print("{0:15} {1}".format("2", two))
                print("{0:15} {1}".format("3", three))
                print("{0:15} {1}".format("4", four))
                print("{0:15} {1}".format("5", five))
                
                print('\nTotal overall respondent : ', sum_all)
                print('Average score result : ', average)
               
def main():
   start()
   print('End of program reached')
main()
