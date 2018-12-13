def find_hypotenuse(x,y):
 import math
 if x > 0 and y > 0:
   h = math.sqrt(x * x + y * y)
   print(f"The hypotenuse of this right triangle is {h}")
 else:
  print(f"This shape is not a triangle")
  
 
