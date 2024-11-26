def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
def print_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))
n = 6
triangle = pascal_triangle(n)
print_triangle(triangle)

