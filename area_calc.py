#The Area Function
def circle_area(x):
    print ((x**2)*3.14)   

def rectangle_area(y,z):
    print (y*z)

def parallelogram_area(w,v):
    print (w*v)
   
print ("Circle, Rectangle and Parallelogram Calculator")
print ("Which Area do you want to calculate?")
choice = input("")

if (choice == "circle" or choice == "Circle"):
    x = int(input("Enter the circle radius: "))
    circle_area(x)
elif (choice == "rectangle" or choice == "Rectangle"):
    y = int(input("Enter the rectangle length: "))
    z = int(input("Enter the rectangle width: "))
    rectangle_area(y,z)
elif (choice == "parallelogram" or choice == "Parallelogram"):
    w = int(input("Enter the parallelogram base: "))
    v = int(input("Enter the parallelogram height: "))
    parallelogram_area(w,v)    
else:
    print (choice + " is not computable ")
 
