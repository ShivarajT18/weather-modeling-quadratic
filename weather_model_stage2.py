# weather_model_stage2.py
import math

print("Weather Model - Quadratic Solution (Keyboard Input)")
a, b, c = map(float, input("Enter a, b, c separated by spaces: ").split())

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots (unstable weather pattern)")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")

