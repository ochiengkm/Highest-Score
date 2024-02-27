from random import randint
#Debuging, Finding and Fixing Errors in Your Code:
#1.)Describe Your problem
def my_function():
    for i in range(1, 21):
        if i==20:
            print("You got it")
my_function()

#2.)Reproduce the bug
dice_imgs=["(1)", "(2)", "(3)", "(4)", "(5)", "(6)"]
dice_num= randint(1, 6)
print(dice_imgs[dice_num - 1])

#3.)Play Computer and Evaluate Each Line
year=int(input("What year were you born?: "))
if year>1980 and year<1994:
    print("You are a Millenial!")
elif year>=1994:
    print("You are a Gen Z!")

#4.)Fixing Errors and Watching for Red Underlines
#5.)Squash Bugs With a print() Statement
pages= 0
word_per_page= 0
pages=int(input("Number of pages: "))
print(pages)
words_per_page=int(input("Number of words per page: "))
print(words_per_page)
total_words=pages * words_per_page
print(total_words)

#6.)Bringing Out the Big Gun Using a Debugger
def mutate(a_list):
    b_list=[]
    for item in a_list:
        new_item= item* 2
        b_list.append(new_item)
    print (b_list)
mutate([1, 2, 3, 5, 8, 13])    