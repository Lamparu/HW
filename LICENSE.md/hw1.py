import math
import cmath

b = 1e-20 
c = 4.0

D = b**2- 4*c 

def squadrix_viet (b, c): #Используя т. Виета
  
  
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

Dk = 4*c/b**2


def squadrix_taylor (b, c): #Используя разложение корня дискриминанта в ряд Тейлора
  if D >= 0 :
    
    if Dk < 1e-15 : #сравниваю с машинным eps
      x2 = -c/b  
      x1 = c/x2
    
    elif Dk > 1/1e-15 :
      x1 = -c/b 
      x2 = c/x1
  
    else : 
      x1, x2 = squadrix_viet (b, c)
  else :
    x1, x2 = squadrix_viet (b, c)
    
  return x1, x2
    
print (squadrix_viet (b, c)) #решение для Виета
print (squadrix_taylor (b, c))  #решение для Тейлора
