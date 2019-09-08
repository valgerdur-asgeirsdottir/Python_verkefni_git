
years_str = input("Number of years from now (int): ") #Tekur við árafjölda sem streng
years_int = int(years_str) #Breytir árafjölda í integer  
seconds_int = years_int * 365 * 24 * 3600 #Breytir árafjölda í sekúndufjölda

population_now_int = 307357870 #Fasti með núverandi fólksfjölda

birth_float = seconds_int / 7 #Reiknar fjölda fæðinga á tímabilinu
death_float = seconds_int / 13 #Reiknar fjölda dauðsfalla á tímabilinu
immigrant_float = seconds_int / 35 #Reiknar fjölda nýrra innflytjenda á tímabilinu

new_population_int = int(population_now_int + birth_float - death_float \
                         + immigrant_float) #Reiknar nýjan fólksfjölda með því að
#taka fastann, bæta við nýjum fæðingum og innflytjendum og draga frá dauðsföll

if years_int >= 0 : 
    print( "New population after", years_int ,"years is",\
           new_population_int, "!") #Ef gefinn árafjöldi er stærri eða jafn 0 prentast nýr fólksfjöldi

else :
    print("Invalid input!") #Ef gefinn árafjöldi er minni en 0 

                         

