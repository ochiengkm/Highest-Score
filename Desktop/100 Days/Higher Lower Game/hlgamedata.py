celebrities = [
    {'name': 'Cristiano Ronaldo',
     'follower_count': 400,
     'profession': 'Footballer',
     'country': 'Portugal'
    },
    {'name': 'Taylor Swift',
     'follower_count': 170,
     'profession': 'Singer',
     'country': 'United States'
    },
    {'name': 'Virat Kohli',
     'follower_count': 150,
     'profession': 'Cricketer',
     'country': 'India'
    },
    {'name': 'Emma Watson',
     'follower_count': 110,
     'profession': 'Actress',
     'country': 'United Kingdom'
    },
    {'name': 'Shakira',
     'follower_count': 70,
     'profession': 'Singer',
     'country': 'Colombia'
    },
    {'name': 'Dwayne Johnson',
     'follower_count': 250,
     'profession': 'Actor',
     'country': 'United States'
    },
    {'name': 'Beyoncé',
     'follower_count': 180,
     'profession': 'Singer',
     'country': 'United States'
    },
    {'name': 'Lionel Messi',
     'follower_count': 280,
     'profession': 'Footballer',
     'country': 'Argentina'
     },

]
import random
def random_person():
    random_celeb= random.choice(celebrities)
    return random_celeb
my_list=[]
score=0
def compare():
    for _ in range(2):
        my_list.append(random_person())
    for data in my_list:
        if my_list[1]== my_list[0]:
            my_list.remove(data)
            my_list.append(random_person())
    print (f"Compare A: {my_list[0]['name']} the {my_list[0]['profession']} from {my_list[0]['country']}")
    print(" ")
    print("                   VERSUS")
    print(" ")
    print (f"Against B: {my_list[1]['name']} the {my_list[1]['profession']} from {my_list[1]['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ")
    if my_list[0]['follower_count']>my_list[1]['follower_count'] and choice=="A":
#         score+=1
#         print(f"You are right! Current score is: {score}")
        return True
    elif my_list[0]['follower_count']<my_list[1]['follower_count'] and choice=="B":
#         score+=1
#         print(f"You are right! Current score is: {score}")
        return True
    else:
        print(f"Wrong your total score is: {score}")
        return False
while compare()==True:
    score+=1
    print(f"You are right! Current score is: {score}")
    my_list.pop(0)
    my_list.append(random_person())
    continue
    























































