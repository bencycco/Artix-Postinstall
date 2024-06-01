import time

def run():
    method = input("What form is the grade in? (A-U/9-1) >> ")

    if method == "A-U":
        time.sleep(0.7)
        grade = input("What grade did you recieve? >> ")
        if grade == "A*":
            time.sleep(0.7)
            print("You may have recieved a 9 or an 8")
            time.sleep(10)
        elif grade == "A":
            time.sleep(0.7)
            print("You may have recieved a 8 or a 7")
            time.sleep(10)
        elif grade == "B":
            time.sleep(0.7)
            print("You may have recieved a 6 or a 5")
            time.sleep(10)
        elif grade == "C":
            time.sleep(0.7)
            print("You may have recieved a 5 or a 4")
            time.sleep(10)
        elif grade == "D":
            time.sleep(0.7)
            print("You may have recieved a 3")
            time.sleep(10)
        elif grade == "E":
            time.sleep(0.7)
            print("You may have recieved a 3 or a 2")
            time.sleep(10)
        elif grade == "F":
            time.sleep(0.7)
            print("You may have recieved a 2 or a 1")
            time.sleep(10)
        elif grade == "U":
            time.sleep(0.7)
            print("You may have recieved a U")
            time.sleep(10)

    if method == "9-1":
        time.sleep(0.7)
        grade = input("What grade did you recieve? >> ")
        if grade == "9":
            time.sleep(0.7)
            print("You may have recieved a high A*")
            time.sleep(10)
        elif grade == "8":
            time.sleep(0.7)
            print("You may have recieved a low A* or a high A")
            time.sleep(10)
        elif grade == "7":
            time.sleep(0.7)
            print("You may have recieved a low A")
            time.sleep(10)
        elif grade == "6":
            time.sleep(0.7)
            print("You may have recieved a high B")
            time.sleep(10)
        elif grade == "5":
            time.sleep(0.7)
            print("You may have recieved a low B or a high C")
            time.sleep(10)
        elif grade == "4":
            time.sleep(0.7)
            print("You may have recieved a low C")
            time.sleep(10)
        elif grade == "3":
            time.sleep(0.7)
            print("You may have recieved a D or a high E")
            time.sleep(10)
        elif grade == "8":
            time.sleep(0.7)
            print("You may have recieved a low E or a high F")
            time.sleep(10)
        elif grade == "8":
            time.sleep(0.7)
            print("You may have recieved a low F or a G")
            time.sleep(10)
        elif grade == "U":
            time.sleep(0.7)
            print("You may have recieved a U")
            time.sleep(10)