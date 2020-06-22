def circle_area(x):
    print ((x**2)*3.14)
    return
   

def rectangle_area(y,z):
    print (y*z)
    return
   

print ("Circle and Rectangle Area")
print ("Which Area do you want to calculate?")
choice = input("")

if choice == "circle":
    x = int(input("Enter the circle radii: "))
    circle_area(x)


if choice == "rectangle":
    y = int(input("Enter the rectangle length: "))
    z = int(input("Enter the rectangle width: "))
    rectangle_area(y,z)