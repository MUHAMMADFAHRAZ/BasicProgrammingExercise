from turtle import width
# create by fahraz ti22i

def menu():
    print(""" menu :
    1. calculate the area of the triangle
    2. calculate the area of the rectangle
    3. determine odd and even numbers
    4. quit""")
    choose = int(input("choose number : "))
    if choose == 1:
        triangle_area()
    elif choose == 2 :
        rectangle()
    elif choose == 3 :
        determine_number()
    elif choose == 4 :
        print("thanks for using this app")
    else :
        print("invalid input")

def triangle_area():
    while(True):
        m = measure()
        base = int(input("input base of triangle : "))
        height = int(input("input height of triangle : "))
        area_T = 1/2 * base * height
        print("the area of triangle : ", int(area_T), m)
        isbreak = input("want to count again? y for yes, n for no : ")
        if isbreak == "n" :
            break
    
    back()

def rectangle():
    while(True):
        m = measure()
        length = int(input("input length of rectangle :"))
        width = int(input("input width of rectangle : "))
        area = length * width
        print("the area of rectangle : ", area, m)
        isbreak = input("want to count again? y for yes, n for no : ")
        if isbreak == "n" :
            break
    
    back()

def determine_number():
    while(True):
        number = int(input("input the number : "))
        if number % 2 == 0 :
            print("the number is even")
        elif number % 2 == 1:
            print("the number is odd")
        else:
            print("invalid input")

        isbreak = input("want to determine again? y for yes, n for no : ")
        if isbreak == "n" :
            break
    back()

def back():
    back = input("back to menu ? y for yes, n for no : ")
    if back == "y":
        menu()

def measure():
    print(""" unit of measure :
    1. km 
    2. hm 
    3. dam 
    4. m 
    5. dm
    6. cm
    7. mm""")

    measure = int(input("choose number : "))
    if measure == 1:
        measure = "km"
    elif measure == 2 :
        measure = "hm"
    elif measure == 3 :
        measure = "dam"
    elif measure == 4 :
        measure = "m"
    elif measure == 5:
        measure = "dm"
    elif measure == 6:
        measure = "cm"
    elif measure == 7 :
        measure == "mm"
    else :
        print("invalid input")
    
    return measure


menu()