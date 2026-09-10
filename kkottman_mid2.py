#Karl Kottman
#CTC 389
#Midterm Q2

def area_rectangle(b,h):
    area = b*h
    return area

base = float(input("Enter the base of your rectangle:"))
height = float(input("Enter the height of your rectangle:"))

result = area_rectangle(base,height)

print("The area of your rectangle is", result)

