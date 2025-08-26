# weather_model_stage1.py
import math

# Hard-coded coefficients
a = 1
b = -3
c = 2

print("Weather Model - Quadratic Solution (Hardcoded)")
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots (unstable weather pattern)")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")
