import math


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius (unrounded)."""
    return math.pi * radius ** 2


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    print(f"Area of the circle: {area:.2f}")