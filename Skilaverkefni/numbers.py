#1	Skoðum allar heilar jákvæðar tölur
#1a Leggjum saman einstaka tölustafi af tölunni sem við erum að skoða
#1b Setjum þessa summu í annað veldi
#1c Ef talan sem við erum með núna er jöfn upphaflegu tölunni prentum við hana í sér línu
#2	Skoðum nú allar jákvæðar heilar tölur sem eru minni en 100
#2a Reynum að deila tölunni með öllum jákvæðum heilum tölum upp að tölunni sjálfri (að henni meðtaldri)
#2b	Ef deilingin gengur upp (enginn afgangur verður) teljum við deilinn
#2c Ef talan hefur nákvæmlega 10 deila prentum við hana í sér línu

for i in range(10, 100):
    dig1 = i // 10
    dig2 = i % 10
    sum_dig = dig1 + dig2
    if sum_dig ** 2 == i:
       print(i)

for t in range(1,100):
    count_div = 0
    for b in range(1,t+1):
        if t % b == 0:
            count_div += 1
    if count_div == 10:
        print(t)