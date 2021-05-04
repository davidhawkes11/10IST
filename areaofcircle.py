# Program to calculate the area of a circle.

"""
Program to calculate the area of a circle.
"""

# import libraries
import math

# define functions
def areaofcircle(r):
    area = math.pi ** r
    print("Returning area to main program.")
    return(area)
    

# main program
radius = float(input("What is the radius of the circle in cm? "))
print("Radius is ", radius, " cm")
print("Area is equal to ", areaofcircle(radius), "cm2")




