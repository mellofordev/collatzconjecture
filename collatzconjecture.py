def collatz(i):
  l=[]
  l.append(i)
  while True:
    if i%2!=0:
      i=3*i+1
      l.append(i)
    elif i%2==0:
      
      i=i//2
      l.append(i)
    if i==1:
      break
  return l

#todo graph, tree 
     
    
