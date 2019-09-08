
turns = input("How many integers? ")
turns_int = int(turns)
count = 0
slettar_tolur = 0
oddatolur = 0
while count < turns_int :
    count = count +1
    tala = input(":")
    tala_int = int(tala)
    if (tala_int % 2) > 0 :
        oddatolur = oddatolur + tala_int
    else :
        slettar_tolur = slettar_tolur + tala_int

print("Summa slettra talna:", slettar_tolur, ", summa oddatalna:", oddatolur)
        
      
    
        
        


