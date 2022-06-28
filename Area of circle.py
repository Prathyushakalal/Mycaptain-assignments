r=float(input("Enter radius of the circle:"))
area=3.146*r*r
print("Radius:",r)
print("Area:",area)


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
