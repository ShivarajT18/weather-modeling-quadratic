# weather_model_stage2.py
import math

print("Weather Model - Quadratic Solution (Keyboard Input Automated)")

# Default coefficients
a, b, c = 1, -3, 2  

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots (unstable weather pattern)")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")


