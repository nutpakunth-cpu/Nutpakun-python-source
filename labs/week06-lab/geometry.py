def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 1/2 * height * base
    print(f"Tritangle with height {height} and base {base}")
    print(f"Area = {1/2} × {height} × {base} = {area}")
    print()

print("Calculating tritangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)