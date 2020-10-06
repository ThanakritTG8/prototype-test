
def print_factors():
   for x in range(100):
    sums=[]
    count=0
    
    for i in range(1, x + 1):
       
     
       if x % i == 0:
           if i != x:
              count+=i
    if count == x :
       sums.append(i)
    if sums != []:
       print(x,'>>',sums)


print_factors()