import pharmadata
import time

print("This is Permanganate's Pharmacopeia")
time.sleep(0.2)
print("Note that: Not all drugs are included in here")
time.sleep(0.2)

#Taking input
drug = input('Select a drug to find > ')

if drug in pharmadata.name_drugs:
    pharmadata.run(drug)