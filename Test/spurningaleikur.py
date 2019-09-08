true_answers = 0
print("What is the capital of India? a) Mumbai b) New Delhi c) Bangladesh")
svar1 = input("     Answer: ")
if svar1 == "b" or svar1 == "New Dehli" :
    print("          True answer!")
    true_answers = true_answers + 1
else :
    print("          Wrong answer!")
print("What is the capital of Ukraine? a) Kyiv b) Minsk c) Odesa")
svar2 = input("     Answer: ")
if svar2 == "a" or svar2 == "Kyiv" :
    print("          True answer!")
    true_answers = true_answers + 1
else :
    print("          Wrong answer!")

print("What is the capital of Norway? a) Uppsala b) Berlin c) Oslo")
svar3 = input("     Answer: ")
if svar3 == "c" or svar3 == "Oslo" :
    print("          True answer!")
    true_answers = true_answers + 1
else :
    print("          Wrong answer!")


print("You got",true_answers,"/ 3 right")
