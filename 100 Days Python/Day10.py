print("TIP CALCULATOR")
print("++++++++++++++")
print()
spend = int(input("How much did you spend?: "))
tip = int(input("What percentage do you want to give tip?: "))
people = int(input("How many people are there in your group?: "))

bill_with_tip = tip / 100 * spend + spend
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

print("Total people number is:",people) 
print("So each person have to give-->>", final_amount)
