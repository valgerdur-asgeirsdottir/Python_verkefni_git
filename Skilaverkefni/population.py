
years_str = input("Years: ") 
years_int = int(years_str)  
seconds_int = years_int * 365 * 24 * 3600 #Changes the given years to seconds

population_now_int = 307357870

birth_float = seconds_int / 7 #Calculates number of births on given time period
death_float = seconds_int / 13 #Calculates number of deaths on given time period
immigrant_float = seconds_int / 35 #Calculates number of new immigrants on
#given time period

new_population_int = int(population_now_int + birth_float - death_float \
                         + immigrant_float) #Calculates new population by detracting
#deaths and adding births and new immigrants to the current population

if years_int >= 0 : 
    print( "New population after", years_int ,"years is",\
           new_population_int) 

else :
    print("Invalid input!") 

                         

