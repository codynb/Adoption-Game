#The author is Cody Brown, Word Game Project

#Adopting a Animal

#------------------------- Code directly copied from example
import time
import random
achieved = []
element = ""

def prt_list(list):
    for j in list:
        print(j, flush=True)
        if len(j) < 70:
            time.sleep(2)
        else:
            time.sleep(3)

def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)
#-------------------------

def adopt_center():
    global element
    element = random.choice(["big dog", "bird", "cat", "gerbil", "horse", "puppy"])
    beginning = [
        "Your family has decided they want to add another member to family,",
        "and it is time to go to the adoption center to find that furry friend!",
        "Before you take everyone, you go alone to see who will be the best for "
        "you all.", f"The worker brings out a {element}.",
        f"To get to know the {element}, you can either play with it or cuddle with it"
    ]
    prt_list(beginning)

def first_interaction_choice():
    choice = [
        "Type play to play with it.",
        "Type cuddle to cuddle with it."
        ]
    prt_list(choice)
    response = str(input("(Type play or cuddle.)\n"))
    return response

def play():
    play_attempt_wL = [
        f"You walk up to the {element} to play with it",
        f"The {element} get's so happy!",
        "It jumps around and plays with you.",
        f"It looks like might want to play some more."
        ]
    play_attempt_wnL = [
        f"You walk up to the {element} to play with it,",
        "but it does not trust you.",
        "It might need to love you first."
        ]
    if "loves" in achieved:
        prt_list(play_attempt_wL)
    else:
        prt_list(play_attempt_wnL)
    play_choice = str(input("Do you want to continue to play (a) or stop playing (b)\n"))
    return play_choice

def play2():
    play_response = play()
    if play_response == "a":
        not_loves = [
            f"The {element} tries to play, but gets tired.",
            "But, it does not trust you enough to sleep next to you.",
            f"The {element} is terrified, and you've ruined any future relationship.",
            f"You cannot adopt the {element}"
            ]
        loves = [
            f"The {element} plays for a little bit longer, and then grows sleepy.",
            f"Because the {element} loves and trusts you, it feels safe to fall asleep.",
            f"This {element} is perfect for your family!"
            ]
        if "loves" in achieved:
            prt_list(loves)
            adopt_another_animal()
        else:
            prt_list(not_loves)
            adopt_another_animal()
    elif play_response == "b":
        prt_single(f"The {element} looks at you, as if wanting something more...", 2)
    else:
        prt_single("What do you want to do?", 2)
        play2()

def cuddle():
    cuddle_once = [
        f"The {element} loves you!",
        "It come right up next to you, and feel safe.",
        "How can you test this bond?"
        ]
    if "loves" in achieved:
            cuddle_twice = [
                f"The {element} feels too cuddled, and starts to panic.",
                "You try to calm it down, but it is too late.",
                f"The {element} misinterpreted your extra cuddles as being trapped.",
                f"The {element} cannot be adopted by you as it no longer trusts you."
                ]
            prt_list(cuddle_twice)
            adopt_another_animal()
    else:
        prt_list(cuddle_once)
        achieved.append("loves")

def game():
    choice = first_interaction_choice()
    if choice == "play":
        play2()
    elif choice == "cuddle":
        cuddle()
    else:
        game()
    game()

def Adoption():
    adopt_center()
    game()
    adopt_another_animal()

def adopt_another_animal():
    global achieved
    prt_single("Would you like to try to adopt another animal?", 2)
    response2 = str(input("Please enter y for yes and n for no.\n").lower())
    if response2 == "y":
        achieved = []
        Adoption()
    elif response2 == "n":
        exit()
    else:
        adopt_another_animal()


Adoption()
