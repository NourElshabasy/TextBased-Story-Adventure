import time

# Acceptable answers
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = "\nUse only A, B, or C\n"

# Introduction with beggining choices
def intro():
    print("Your master instructed you to go explore the dungeon that is in the cave. \
He explained how there was a legend that stated that there is a legendary sword hidden \
deep in the dungeon. If you found this sword you would become the new owner of it and it would \
allow you to slay any enemy at your will. You go down the cave with your rusty sword and bronze \
shield and find the dungeon that your master told you about. While exploring the dungeon you \
find a pouch of gold but then you encountered a goblin wanting to steal your gold! You will:")
    time.sleep(1)
    print("""    A. Fight the goblin
    B. Give him the gold
    C. Run away""")
    choice = input(">>> ")
    if choice in answer_A:
        option_fight()
    elif choice in answer_B:
        print("\nYou give the gold to the goblin and he runs off with it leaving you be. \
The gold could have been useful later on to find the legendary sword. You continue forward \
but fall into a spike trap!\n\nYou died!")
    elif choice in answer_C:
        print("\nYou run as fast as you can attempting to loose the goblin but the goblin \
is too fast thanks to him being small and agile on his feet. He ends up catching up \
to you and calls out to his other goblin friends. They take your gold and stab you with \
their daggers!\n\nYou died!")
    else:
        print(required)
        intro()

# Option A : Fight (More choices which change the story a little)
def option_fight():
    print("\nYou decide to fight the goblin! You will:")
    time.sleep(1)
    print("""    A. Strike the goblin with your rusty sword
    B. Block the goblin's incoming attack
    C. Charge and bash the goblin with your shield""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou ended up killing the goblin which allows you to keep the gold that you found! \
Now it is time to explore deeper into the dugeon and find that legendary sword!")
        shop_route()
    elif choice in answer_B:
        print("\nYou successfully blocked the goblin's attack but the goblin gets back on his feet \
and goes in for a backstab!\n\nYou died!")
    elif choice in answer_C:
        print("\nYou charge the goblin with your shield and bash into him. You killed the goblin as \
he did not expect you to do that! Now it is time to explore deeper into the dugeon and find that \
legendary sword!")
        pickaxe_route()
    else:
        print(required)
        option_fight()

# Option A : Strike the goblin with your rusty sword (Opens up the shop route due to keeping the money)
def shop_route():
    print("\nAs you go deeper into the dungeon you find an old man who is the owner of a shop. \
You decide to see what you can spend your gold on. You see that he is selling a key that could be \
useful in the dungeon. You purchase the key with your gold and continue on your exploration.")
    print("\nAfter a bit of exploring you find a chest which conveniently has a key hole that is \
perfect for the key you purchased! You open the chest and obtained ... another key?! You continue \
going deeper hoping that the key will have a use. You eventually find a door that is locked. Do you use \
the key on the door? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        print("\nYou open the door and find that there is a opening with a small cave and in the middle \
there was a light beaming down on the legendary sword that was in a rock! You pull on the sword with \
all your might untill you get it out of the rock. The sword is now yours! You slay every enemy in your \
path and make back to the surface to show your master!\n\nWell done!")
    if choice in no:
        print("\nYou decide not to open the door and end up exploring for so long that you die \
of bordem!")


# Option C : Charge and bash the goblin with your shield (Opens up the pickaxe route)
def pickaxe_route():
    print("\nWhile exploring you find a pickaxe on the ground. Will you pick it up? Y/N")
    time.sleep(1)
    choice = input(">>> ")
    if choice in yes:
        print("\nYou grab the pickaxe and decide to start mining through this unusual rock that \
you found. You break the rock and find that there is a opening with a small cave and in the middle \
there was a light beaming down on the legendary sword that was in a rock! You pull on the sword with \
all your might untill you get it out of the rock. The sword is now yours! You slay every enemy in your \
path and make back to the surface to show your master!\n\nWell done!")
    if choice in no:
        print("\nYou decide not to pick up the pickaxe and end up explorin-g for so long that you die \
of bordem!")

# Intro function called which starts the whole story
intro()
