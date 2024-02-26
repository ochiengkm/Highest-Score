import random
test_seed=int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV=input("Type in the names of everyone separated by a comma and space: ")
names=namesAsCSV.split(", ")
people=len(names)
random_number=random.randint(0, people - 1)
output=(names[random_number])
print(f"{output}, bills' on you!")
