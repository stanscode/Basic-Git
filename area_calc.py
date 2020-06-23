def circle_area(x):
    print ((x**2)*3.14)
    return
   

def rectangle_area(y,z):
    print (y*z)
    return
   

print ("Circle and Rectangle Area")
print ("Which Area do you want to calculate?     *type in lowercase")
choice = input("")

if (choice == "circle"):
    x = int(input("Enter the circle radius: "))
    circle_area(x)
elif (choice == "rectangle"):
    y = int(input("Enter the rectangle length: "))
    z = int(input("Enter the rectangle width: "))
    rectangle_area(y,z)
else:
    print (choice + " is not computable ")
 
