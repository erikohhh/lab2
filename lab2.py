print("ET0735(DevOps for AIoT) - Lab 2 - Introduction to Python")
def funcName(parameter1, parameter2):
    print("this is a dummy function")
    return 10

def calculate_bmi(weight,height):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi = weight/(height*height)
    if bmi>25.0:
        print(str(bmi))
        print("User is over weight")
    elif bmi <18.5:
        print(str(bmi))
        print("User is under weight")
    else:
        print(str(bmi))
        print("User has a normal weight")

    

calculate_bmi(weight=57,height=1.73)