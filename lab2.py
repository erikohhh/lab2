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
        
        return 1
    elif bmi <18.5:
        print(str(bmi))
        print("User is under weight")
        return -1
    else:
        print(str(bmi))
        print("User has a normal weight")
        return 0

print(calculate_bmi(weight=57,height=1.73))


#def main():
#    print("ET0735(DevOps for AIoT) - Lab 2 - Introduction to Python")
#    display_main_menu()
 #   num_list = get_user_input()
  #  if _name_=="_main_":
   #     main()

#def display_main_menu():
#   print("Enter some numbers seperated by commas(e.g. 5,67,32)")
#display_main_menu()
    
#def get_user_input():
#    user_i = input()
#    sep_in = user_i.split(",")
#    num_list = []
#    num_list = list(sep_in)
#    print(num_list)
#    return num_list
#get_user_input()

#def calc_average_temperature():
#    user_i= input("Enter the temperature readings seperated by comma (e.g. 30,40,35)")
    

