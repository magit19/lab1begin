#Собственность MaxCorp
def get_largest_perimiter(L):
  hugest = -1
  for i in range(len(L)-2):
    if (L[i] < 0): return "ERROR"
    
    for j in range(i+1,len(L)-1):
      if (L[j] < 0): return "ERROR"
      
      for k in range(j+1,len(L)):
        if (L[k] < 0): return "ERROR"
        
        if (L[k]+L[i]>L[j] and L[i]+L[j]>L[k] and L[k]+L[j]>L[i]): 
          pretender = L[i]+L[j]+L[k]
          if (pretender > hugest):
            hugest = pretender
            pos_a = i
            dlin_a = L[i]
            pos_b = j
            dlin_b = L[j]
            pos_c = k
            dlin_c = L[k]
          
  if (hugest == -1): return "No treugolnik!"
  return ("Perimetr naibolshego treugolnika: " + str(hugest) + "\nStoroni\nPozition: " + str(pos_a) + " " + str (pos_b) + " "  + str(pos_c) 
          + "\nDlini kajdoy storony: " + str(dlin_a) + " " + str (dlin_b) + " "  + str(dlin_c))
          

L = list(map(int, input().split()))
print(get_largest_perimiter(L))
