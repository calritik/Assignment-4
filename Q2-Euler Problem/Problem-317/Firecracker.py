import math

h = 100    
v = 20     
g = 9.81   

# The swept region is bounded by a paraboloid of revolution.
# Envelope equation: z = H - (g / 2v^2) * r^2
# where H is the apex height.

H = h + v**2 / (2 * g)

# Volume of a paraboloid = (1/2) * base_area * height
# base radius r_max when z = 0: r_max^2 = 2*v^2*H / g

r_sq = 2 * v**2 * H / g

# Volume of paraboloid = pi * r^2 * H / 2
volume = math.pi * r_sq * H / 2

print(round(volume, 4))