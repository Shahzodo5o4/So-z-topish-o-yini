
from uzwords import words
import random as r

def get_word():
    word = r.choice(words)
    while "-" in word or ' ' in word:
        word = r.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    
    word_letters = set(word)
    
    user_letters = ' '
    print(f"Men {len(word)} harfdan iborat so`z o`yladdim.Topa olasizmi ? ")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(word_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni kiritdingiz.Boshqa harf kiriting. ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to`g`ri. ")
        else:
            print("Bunday harf yo`q. ")
        user_letters += letter
    print(f"Tabriklayman ! {word} so`zini {len(user_letters)} ta urinishda topdingiz. ")
    
        
        