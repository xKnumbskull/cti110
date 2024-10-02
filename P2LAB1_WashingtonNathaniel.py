# Nathaniel Washington
# 10/2/2024
# P2LAB1
# Using math expressions
import math

#Get radius user
radius = float(input("Enter the radius of the circle: "))

#Calculate the circumference, diameter, and area
circumference = 2 * math.pi * radius
diameter = 2 * radius
area = math.pi * (radius ** 2)

#Displays results
print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"Area: {area:.3f}")
