"""
1.Toss to choose for batting or bowling 
2.for user batting the user needs to score the runs without getting the same number from the computer while playing 
3.similarly for bowling the wicket is down if the same digits comes while playing
4. checks who got more points while batting 

"""
import random
runs_user=0
runs_comp=0
#funtions to calculate the runs scored by user and the computer 
def userbowlingandcompbatting():
    global runs_comp
    notwicket=True
    while notwicket:
        bowl_user=int(input("enter a number from (0-6)  for bowling!! :  "))
        bat_comp=random.randint(0,6)
        print("computer chooses                             :",bat_comp)
        if bowl_user!=bat_comp:
            if bat_comp==0:
                runs_comp+=bowl_user
            else:
                runs_comp+=bat_comp
        else:
            print("howzat !!!")
            notwicket=False
        
    return runs_comp

def userbattingandcompbowling():
    global runs_user
    notwicket=True
    while notwicket:
        bat_user=int(input("enter a number from (0-6)  for batting!!:  "))
        bowl_comp=random.randint(0,6)
        print("computer chooses                           :",bowl_comp)
        if bat_user!=bowl_comp:
            if bat_user==0:
                runs_user+=bowl_comp
            else:    
                runs_user+=bat_user
        else:
            print("howzat !!!")
            notwicket=False
    return runs_user
#FOR GETTING THE TOSS RESULT
choose_user=input("Say odd or even :")
loopcondtion=True
while loopcondtion:
    choose_usernum=int(input("enter a number from (0-6)  for the toss:  "))
    choose_comp=random.randint(0,5)
    summ=choose_usernum+choose_comp
    if choose_usernum==choose_comp:
        print(" OOps! same numbers,enter the number again")
    else:
        if choose_user=="odd":
            if summ%2!=0:
                print("user won the toss")
                choose_batballuser=input("choose batting or bowling :")
                if choose_batballuser=="batting" :
                    userbattingandcompbowling()
                    print("you scored ",runs_user,"runs")
                    userbowlingandcompbatting()

                elif choose_batballuser=="bowling" :
                    userbowlingandcompbatting()
                    print("you scored ",runs_comp,"runs")
                    userbattingandcompbowling()
                loopcondtion=False
            else:
                print("computer won the toss")
                choose_batballcomp=random.choice(["batting","bowling"])
                print(f"computer chooses {choose_batballcomp} " )
                if choose_batballcomp=="bowling":
                    userbattingandcompbowling()
                    print("you scored ",runs_user,"runs")
                    userbowlingandcompbatting()
                elif choose_batballcomp=="batting":
                    userbowlingandcompbatting()
                    print("you scored ",runs_comp,"runs")
                    userbattingandcompbowling()
                loopcondtion=False
        elif choose_user=="even":
            if summ%2==0:
                print("user won the toss") 
                choose_batballuser=input("choose batting or bowling :")
                if choose_batballuser=="batting" :
                    userbattingandcompbowling()
                    print("you scored ",runs_user,"runs")
                    userbowlingandcompbatting()

                elif choose_batballuser=="bowling" :
                    userbowlingandcompbatting()
                    print("you scored ",runs_comp,"runs")
                    userbattingandcompbowling()
                loopcondtion=False
            else:
                print("computer won the toss")
                choose_batballcomp=random.choice(["batting","bowling"])
                print(f"computer chooses {choose_batballcomp} ")
                if choose_batballcomp=="bowling":
                    userbattingandcompbowling()
                    print("you scored ",runs_user,"runs")
                    userbowlingandcompbatting()
                elif choose_batballcomp=="batting":
                    userbowlingandcompbatting()
                    print("you scored ",runs_comp,"runs")
                    userbattingandcompbowling()
                loopcondtion=False
        else:
            print("something gone wrong")

print("The score of the computer after batting  is",runs_comp)
print("The Your score  after batting is",runs_user)

if runs_user > runs_comp:
    print("So You Are The Winner!!!!")
elif runs_user < runs_comp:
    print("So You Lose")
else:
    print("Its a draw")