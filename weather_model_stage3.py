# weather_model_stage3.py
import math

print("Weather Model - Quadratic Solution (File Input - Single Set)")
with open("input_single.txt", "r") as f:
    line = f.readline().strip()
    a, b, c = map(float, line.split())

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots (unstable weather pattern)")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")
