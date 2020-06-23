#The Area Function
def circle_area(x):
    print ((x**2)*3.14)
    return
   

def rectangle_area(y,z):
    print (y*z)
    return

def parallelogram_area(w,v):
    print (w*v)
    return    
   
print ("Circle, Rectangle and Parallelogram Calculator")
print ("Which Area do you want to calculate?     *type in lowercase")
choice = input("")

if (choice == "circle"):
    x = int(input("Enter the circle radius: "))
    circle_area(x)
elif (choice == "rectangle"):
    y = int(input("Enter the rectangle length: "))
    z = int(input("Enter the rectangle width: "))
    rectangle_area(y,z)
elif (choice == "parallelogram"):
    w = int(input("Enter the parallelogram base: "))
    v = int(input("Enter the parallelogram height: "))
    parallelogram_area(w,v)    
else:
    print (choice + " is not computable ")
 
