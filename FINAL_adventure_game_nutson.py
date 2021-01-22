import time
import random
nemesis = ['demon king', 'head goblin', 'sorcerer', 'dark elf']
nemesis_chosen = random.choice(nemesis)


def print_pause(message, seconds=2):
    print(message)
    time.sleep(seconds)


def print_sleep(message, seconds=5):
    print(message)
    time.sleep(seconds)


def start_game():
    start = input("Want to play a game? (yes/no)\n").lower()
    while True:
        if "yes" in start:
            print_sleep("Awesome!\n Starting the game...")
            intro()
            break
        elif "no" in start:
            print_pause("Dont be lame! You wont make any friends that way.")
            print_pause("If you really want to leave enter quit")
            print_sleep("Sooooooo...")
            start_game()
            break
        elif "quit" in start:
            print_pause("Bye Bye!")
            quit()
        else:
            start = input("Please enter a 'yes' or 'no'.\n")
            start_game()


def play_again():
    again = input("New Game? (yes/no)\n").lower()
    while True:
        if "yes" in again:
            print_sleep("Awesome!\n Restarting the game...")
            intro()
            break
        elif "no" in again:
            print_pause("You aren't getting away that easy!")
            print_pause("If you really want to run from your duty, type quit.")
            print_sleep("Sooooooo...")
            play_again()
            break
        elif "quit" in again:
            print_pause("Bye Bye!")
            quit()
        else:
            again = input("Please enter a 'yes' or 'no'.\n")


def intro():
    print('\n\n\n')
    print(' ' * 20 + '\u2694' * 60)
    print(' ' * 20 + '\u2694'"{:^56}"'\u2694'.format('Adventure Game: Slayer'))
    print(' ' * 20 + '\u2694'"{:^56}"'\u2694'.format('Developed by: '
          'Jonshea Nutson'))
    print(' ' * 20 + '\u2694'"{:^56}"'\u2694"'.format('For: Udacity IPND'))
    print(' ' * 20 + '\u2694' * 60)
    print_sleep("You find yourself standing in an secluded forrest.")
    print_sleep("...")
    print_pause("Your surrounded by cherry blossom trees and sakura flowers.")
    print_sleep("You aren't the most confident but you want to help your "
                "village anyway you can; so you decide to go on the hunt.")
    print_sleep(f"Rumor has it that a wicked {nemesis_chosen} "
                "lurks in the nearby "
                "cottage and has been abducting "
                "women from the village.")
    print_sleep("...")
    print_pause("You have to do something or else all the women could "
                "disappear.")
    print_pause("To your right is a wooden cottage that looks rundown, yet "
                "well kept.")
    print_pause("To you left is a large crater with a visibly carved walkway.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "kunai.")


def wooden_cottage(items):
    print_pause("You approach the cottage wielding your weapon tightly.")
    print_sleep("As you approach, the stairs creek one by one on your way to "
                "the door.")
    print_pause("As you reach the door you get a tightness in your chest.")
    print_pause("You peak through the hole in the "
                "rotten door when it suddenly flies open. "
                f"Out steps a {nemesis_chosen}.")
    print_pause(f"WTF! This is a {nemesis_chosen}'s house!")
    decision = input("Would you like to (1) fight or (2) run away?\n")
    while True:
        if decision == "1":
            if "katana" in items:
                print_pause(f"As the {nemesis_chosen} moves to attack, you "
                            "unsheath your Uchikatana and you "
                            "prepare for the worst.")
                print_pause("The Uchikatana's black blade engulfs the "
                            "darkness creating shadow in your "
                            "possession as you brace yourself for the "
                            f"attack.\nBut the {nemesis_chosen} takes "
                            "one look at your mind bending dark blade and "
                            "runs away!", 3)
                print_pause("You have rid the village of this evil presence. "
                            "GAME OVER!")
                play_again()
                break
            else:
                print_pause(f"The {nemesis_chosen} attacks you! You feel "
                            "a bit under-prepared for this, what "
                            "with only having a kunai knife.", 2.5)
                print_pause(f"You do your best...but your kunai breaks "
                            f"under stress against the {nemesis_chosen}.")
                print_pause(f"The {nemesis_chosen} engulfs you and "
                            "takes a human form.")
                print_sleep("He goes back to the village in your form "
                            "taking women every night.")
                print_pause("YOU DIED!")
                play_again()
                break
        elif decision == "2":
            print_sleep("You ran like a coward.")
            print_pause("You run as fast as you can back into the field.")
            print_pause("You trip over a piece of wood on your way "
                        f"out, the {nemesis_chosen} almost grabs your arm.")
            print_pause("You stand up and run as fast as you can "
                        "back into the forrest. How lucky can you be?"
                        "You don't seem to have been followed.", 2.5)
            print_pause("After a few moments, you find yourself back at the "
                        "crosspath.")
            print_pause("You remember you have to do something or all the "
                        "women will be at risk.")
            forrest(items)
            break
        else:
            decision = input("Would you like to (1) fight or (2) run away?\n")


def crater(items):
    print_pause("You head towards the crater.")
    print_sleep("It's extremely dark but you have a lighter to light the way.")
    print_pause("You reach a dead end but your dim lighter is reflected in "
                "front of you as if something metal caught its shine.")
    print_sleep("You feel around the wall.\n...")
    print_pause("You find a katana!")
    print_pause("It has the Japanese letters for Uchikatana enscribed.")
    print_pause("You discard your silly kunai and take "
                "the sword with you.\nYou walk back out "
                "to the forrest.", 3)
    items.append("katana")
    forrest(items)


def forrest(items):
    print_pause("After a few moments, you find yourself back at the "
                "crosspath.")
    print_pause("You remember you have to do something or all the women "
                "will be at risk.")
    choice = input("Enter 1 to knock on the door of the cottage.\n"
                   "Enter 2 to peer into the crater.\n"
                   "Please enter 1 or 2.\n")
    while True:
        if choice == "1":
            wooden_cottage(items)
            break
        elif choice == "2":
            crater(items)
            break
        else:
            choice = input("Please, enter '1' or '2'.\n")


def play_game():
    items = []
    start_game()
    forrest(items)


if __name__ == '__main__':
    play_game()
