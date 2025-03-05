import random
ans1 = "It is certain"
ans2 = "It is decidedly so"
ans3 = "Without a doubt"
ans4 = "Fosho"
ans5 = "Mhm"
ans6 = "Yea nigga"
ans7 = "Damn right"
ans8 = "hunnid percent"
ans9 = "YESSIR"
ans10 = "ehhh"
ans11 = "shii i mean prolly"
ans12 = "idk brobro"
ans13 = "Possibly"
ans14 = "Nigga do it look like I can tell the future?"
ans15 = "Concentrate and ask again... yea nigga ik you pissed off this one"
ans16 = "Na nigga"
ans17 = "hell naw"
ans18 = "nope"
ans19 = "ain't looking too good bruhbruh"
ans20 = "NO"

name = input("Wusyaname: ")
input(name + ", and what's ya question for the magical ball")

choice = random.randint(1,20)

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
elif choice == 8:
    answer = ans8
elif choice == 9:
    answer = ans9
elif choice == 10:
    answer = ans10
elif choice == 11:
    answer = ans11
elif choice == 12:
    answer = ans12
elif choice == 13:
    answer = ans13
elif choice == 14:
    answer = ans14
elif choice == 15:
    answer = ans15
elif choice == 16:
    answer = ans16
elif choice == 17:
    answer = ans17
elif choice == 18:
    answer = ans18
elif choice == 19:
    answer = ans19
else:
    answer = ans20

print("Magic 8 ball: ", answer)

            
