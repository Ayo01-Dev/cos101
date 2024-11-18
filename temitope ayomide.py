def a():
   input1 = float(input("enter your first digit"))
   input2 = float(input("enter the second digit"))
   calculation = input1-input2
   print(calculation)

def b():
    input1 = float(input("enter your firt digit"))
    input2 = float(input("enter the second digit"))
    calculation = input1+input2
    print(calculation)

def c():
    input1 = float(input("enter your first digit"))
    input2 = float(input("enter the second digit"))
    calculation = input1/input2
    print(calculation)

def d():
    speed = float(input("enter the speed"))
    time = float(input("enter the time taken"))
    Distance = speed/time
    print(Distance)

def e():
    power = float(input("enter the power"))
    time = float(input("enter the time"))
    energy = power * time
    print(energy)

def main():
    user=input("what operation do you want to perform:")
    if user == "a":
        a()
    elif user == "b":
        b()
    elif user == "c":
        c()
    elif user == "d":
        d()
    elif user == "e":
        e()
    else:
        print("invalid input")
if __name__ == '__main__':
    main()
