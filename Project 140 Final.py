
rooms = {
   'Brooklyn': {'south' : 'Dark Lands', 'north' : 'Mushroom Kingdom', 'east' : 'Yoshi Island', 'west' : 'Snow Kingdom', 'item': 'no items here'},
   'Dark Lands': {'north' : 'Brooklyn', 'east' : 'Bowsers Castle', 'item': 'turtle shell'},
   'Snow Kingdom': {'east' : 'Brooklyn', 'item': 'freeze flower' },
   'Jungle Kingdom': {'south' : 'Yoshi Island', 'item' : 'banana' },
   'Mushroom Kingdom': {'south' : 'Brooklyn', 'east': 'Princess Peach Castle', 'item': 'mushroom power-up'},
   'Princess Peach Castle': {'west' : 'Mushroom Kingdom', 'item': 'star power-up'},
   'Yoshi Island': {'west': 'Brooklyn', 'north': 'Jungle Kingdom', 'item': 'Yoshi egg'},
   "Bowsers Castle": {'west': 'Dark Lands', 'item': 'Bowser'}
}

current_room = 'Brooklyn'
inventory = []
item = rooms[current_room]['item']


def startup_menu():
    print("Mario and Luigi's Great Adventure")
    print()
    print('* Collect all 6 items to defeat Bowser and win the game!')
    print('* To move our heroes through the game, type: go South, go North, go East, go West, or exit to end the game')
    print("* To collect items and add to inventory: get 'item'")
    print()
    print('GOOD LUCK! The fate of the world rests in your hands!')

def move_between_rooms():
    current_room = 'Brooklyn'
    while True:
        print()
        print('You are in', current_room)
        print('Inventory:', inventory)
        print('--------------------')
        print('You have found', rooms[current_room]['item'])
    # get the player's input
        command = input('Enter your move:').lower().split()
        print()

    # If the player enters 'go' for the first part of the command

        if command[0] == 'go':
            if command[1] in rooms[current_room].keys():  # if the command is in the key for the current room
                current_room = rooms[current_room][command[1]]  # Change current room to new room connected to command


                if current_room == 'Bowsers Castle' and len(inventory) < 6:
                    print('Bowser has captured you and put you in his dungeon. You lose! Game over!')
                    print("""
                             *       ^       *
                           **     ^ ^^^ ^     **
                           *** 0000^^^^^0000 ***
                           (000(   \****/   )000)
                          (00000000 0oo0 00000000)
                           \ \ ____/0000\____/_/
                            \   V   ||||  V   /
                             \  \          /  /
                              \__^_^_^_^_^ _/  """)
                    exit(0)

                if current_room == 'Bowsers Castle' and len(inventory) == 6:
                    print('Congratulations! You have collected all 6 items and defeated Bowser!')
                    print('\ \ / /                    (_)     | |')
                    print(' \ v //__  _   _  __      ___ _ __ | |')
                    print('  \ // _ \| | | | \ \ /\ / / | |_ \| |')
                    print('  | | (_) | |_| |  \ V  V /| | | | |_|')
                    print('  \_/\___/ \__,_|   \_/\_/ |_|_| |_(_)')
                    print()
                    print('Thanks for playing!')
                    exit(0)
            else:
                print("Wrong way, please try again")

    # If player enters 'get' they can acquire the item

        elif command[0] == 'get':
            if current_room != 'Bowsers Castle' or 'Brooklyn':
                item = rooms[current_room]['item']
                if item not in inventory:
                    print('Item acquired!')
                    inventory.append(item)
                    del item
                else:
                    print('You already collected this item')
        # If player enters 'exit' the game will end

        elif command[0] == 'exit':
            print('Game Over! Thanks for playing!')
            exit(0)

    # If player does not enter the 'go' command first, label as invalid entry

        else:
            print('Invalid entry. Please try again.')


startup_menu()
move_between_rooms()







