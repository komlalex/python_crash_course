# A loop is used for iterating over a sequence (that is either a list, a tuple, a set, a dictionary or a string)

people = ["John", "Hall", "Sarah", "Suzzie"]

# Simple for loop
#for person in people:
    #print(f"Current person is {person}")

# Break
#for person in people:
    #if person == "Sarah":
       # break 
    #print(person)

# Continue
for person in people:
    if person == "Hall":
        continue 
    print(person)

# Range
for i in range(len(people)):
    print(f"{people[i].upper()} is number {i + 1}")

for j in range(0, 11):
    print(f"Number: {j}")
#While loops execute a statement as long as a statement is true
count = 0
while count < 10:
    print(f"Count: {count}")
    count+=1 