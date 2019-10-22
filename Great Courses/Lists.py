# Comments out one line
# FirstAmount = 3.50
# SecondAmount = 5.00
# ThirdAmount = 10.00
#
# Average = (FirstAmount + SecondAmount + ThirdAmount)/3
# print(Average)
# year=int(input("Year: "))
# total = 0
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# if year%4==0:
#     days_in_month[1] = 29
# for i in days_in_month:
#     total+= i
# print(total)
# # print(days_in_month)

# summer_months = days_in_month[5:8]
# print(summer_months)
name = ""
names = []
ages = []
while True:
    name = input("Enter name: ")
    if name == 'end':
        break
    age = int(input("Age: "))

    names.append(name)
    ages.append(age)
max_age = 0
i = 0
for i in range(len(ages)):
    if ages[i] > ages[max_age]:
        max_age = i

print (names[max_age],ages[max_age])