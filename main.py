# Function to calculate the cross product of two 3D vectors
def cross_product(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Function to calculate the magnitude of a vector
def magnitude(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

# Function to calculate the area of a parallelogram using three vectors
def parallelogram_area(v1, v2, v3):
    cross_product_result = cross_product(v1, v2)
    area = magnitude(cross_product_result)
    return area

# Function to calculate the area of a triangle using three vectors
def triangle_area(v1, v2, v3):
    cross_product_result = cross_product(v1, v2)
    area = 0.5 * magnitude(cross_product_result)
    return area

# Example vectors
vector1 = [7, 2, -2]
vector2 = [-1, 6, -3]
vector3 = [-3, 1, 2]

# Calculate areas
parallelogram_area_value = parallelogram_area(vector1, vector2, vector3)
triangle_area_value = triangle_area(vector1, vector2, vector3)

print("Area of Parallelogram:", parallelogram_area_value)
