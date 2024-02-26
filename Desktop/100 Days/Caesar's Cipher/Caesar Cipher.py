#The Caesar Cipher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift%25
    def caesar(start_text, shift_amount, direction_chosen):
        new_text=""
        for char in text:
            if char in alphabet:
                char_position=alphabet.index(char)
                if direction=="encode":
                    cipher_char=alphabet[char_position + shift_amount]
                    new_text+=cipher_char
                elif direction=="decode":
                    decipher_char=alphabet[char_position - shift_amount]
                    new_text+=decipher_char
                else:
                    new_text="NONE,Error encountered, you did not choose 'encode' or 'decode'"
            else:
                new_text+=char
        print(f"The {direction}d message is: {new_text}")
    caesar(start_text=text, shift_amount=shift, direction_chosen=direction)
    repeat=input("Type 'yes' if you want to run again, otherwise type 'no': ")
    if repeat== "no":
        should_continue=False
        print("Goodbye!")
