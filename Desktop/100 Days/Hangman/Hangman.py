#Project Hangman
word_list=["ardvark", "baboon", "camel","cherry","lighthouse","quilt","jungle","blossom","thunder","tiger","guitar","candle","umbrella","harmony","river","whisper","zephyr","piano","sapphire","meadow","lighthouse","breeze","velvet","moonlight","crimson","cobalt","eclipse","daisy","radiant","silhouette","cascade","lagoon","serenade","mystic","caramel","tranquil","crystal","infinity","pebble","wanderlust","cinnamon","vivid","lullaby","saffron","zodiac","quasar","aurora","cerulean","enigma","jubilee","galaxy","dreamscape","cascading","majestic","abyss","gossamer","ephemeral","sculpture","vortex","solitude","ethereal","mosaic","ripple","astrology","infinite","journey","whimsical","nebula","oasis","cascade","lunar","gentle","enchant","meadow","mystical","rhapsody","vibrant","halcyon","luminescent","obsidian","ballet","serendipity","reverie","mellifluous","astral","tranquility","labyrinth","verdant","luminary","paradise","sonnet","cynosure","serene" ]
import random
from hangman_art import stages
display=[]
chosen_word=random.choice(word_list)
lives=6
for ch in chosen_word:
    display+= "_"
while display.count("_")> 0 and lives>0:    
    print (display)

    guess=input("Guess a letter: ").lower()
    if guess in display:
        print(f"You had already guessed {guess}, try again!")
    for letter in range (len(chosen_word)):
        chosen_letter=chosen_word[letter]
        if chosen_letter==guess:
            display[letter]=guess

    if guess not in chosen_word:
        lives-=1
        print(f"Incorrect! You entered {guess}, and lose a life!")
    if lives==0:
        print(f"{' '.join(display)}\nYou lose! The answer was {chosen_word}")
    print (stages[lives])
if "_" not in display:
    print(f"{' '.join(display)}\nYou win!")

        