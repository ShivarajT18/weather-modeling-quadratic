# weather_model_stage4.py
import math

print("Weather Model - Quadratic Solution (File Input - Multiple Sets)")
with open("input_multiple.txt", "r") as f:
    for line in f:
        a, b, c = map(float, line.strip().split())
        discriminant = b**2 - 4*a*c
        print(f"\nEquation: {a}x² + {b}x + {c} = 0")

        if discriminant < 0:
            print("  No real roots (unstable weather pattern)")
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"  Roots: {root1}, {root2}")
