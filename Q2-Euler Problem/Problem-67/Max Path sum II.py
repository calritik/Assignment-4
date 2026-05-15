lines = open('0067_triangle.txt').read().strip().split('\n')
triangle = [list(map(int, row.split())) for row in lines]

# Bottom-up dynamic programming
for i in range(len(triangle)-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])