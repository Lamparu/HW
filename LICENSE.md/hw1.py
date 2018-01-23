import math
import cmath

def squadrix (b, c):
  
  D = b**2- 4*c
  
  if D >= 0:
    sqD = math.sqrt (D)
    
    
    if b >= 0: #определям подходящий знак b
    
      x1 = (-b - sqD)/2.0
      x2 = c/x1
    
    else:
      
      x1 = (-b + sqD)/2.0
      x2 = c/x1
    
  
  else:
    sqD = cmath.sqrt (D)
    
    x1 = (-b + sqD)/2.0
    x2 =  c/x1
    
  
  return x1, x2

print (squadrix (0.5, 4.0)) #подставить значения b и c
