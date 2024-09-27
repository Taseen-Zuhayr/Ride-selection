x = int(input("Input the ride you want to ride. 1.Airborn or 2.Waterborn : "))

if x == 1:
    a = int(input("What type of car do want? 1.Fighter jet simulator and 2.Casual flight simulator : "))
    if a == 1:
        print("A ride has succesfully been booked for Fighter jet simulator.")
    else:
        print("A ride has succesfully been booked for Casual jet simulator.")
elif x == 2:
    b = int(input("What type of car do want? 1.Fighter ship simulator or 2.Casual ship simulator : "))
    if b == 1:
        print("A ride has succesfully been booked for Fighter ship simulator.")
    elif b == 2:
        print("A ride has succesfully been booked for Casual ship simulator.")
else:
    print("What are you even inputting?")