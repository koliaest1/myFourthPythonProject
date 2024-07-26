# write your code here
import random
no_of_guests = int(input("Enter the number of friends joining (including you):"))
list_of_guests = list()
dict_of_guests = dict()
if no_of_guests > 0:
    for i in range(no_of_guests):
        guest_name = input("Guest Name: ")
        list_of_guests += [guest_name]
        dict_of_guests[guest_name] = 0
    total_bill = int(input("Enter the total bill value:"))
    per_person_bill = round((total_bill / no_of_guests), 2)
    for i in range(no_of_guests):
        dict_of_guests[list_of_guests[i]] = per_person_bill
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if lucky == 'Yes':
        lucky_guest_id = random.randint(1, no_of_guests) - 1
        print(str(list_of_guests[lucky_guest_id]) + " is the lucky one!")
        per_person_bill = round((total_bill / (no_of_guests - 1)), 2)
        for i in range(no_of_guests):
            dict_of_guests[list_of_guests[i]] = per_person_bill
        dict_of_guests[list_of_guests[lucky_guest_id]] = 0
    else:
        print("No one is going to be lucky")
    print(dict_of_guests)
else:
    print("No one is joining for the party")
