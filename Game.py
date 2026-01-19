print(r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""` 
""")
print("Welcome to The Treasure Island\n")
print("-------------------------------------------------------------------------------------------\n")
print("In front of you is a Lake\n")
dir=input("Enter the direction you want to go: left(l) or right(r)\n")
if dir == 'l':
    print("You encountered a bear and tried to fight it :D\n")
else :
    print("Good Choice, Now you encounter a snake ssssssss\n")
    d=input("What will you do here: Fight it(f) or RUN(r)\n")
    if d == 'f':
        print("Are you an idiot , obv you will die , RIP XD\n")
    else :
        print("Now you come across a large X on the ground:\n")
        do=input("What will you do: Dig(d) or Ignore(i)")
        if do == 'd':
            print("Yay you WON!!!")
        else :
            print("Are you a dumbo or wht :P")
