#!/usr/bin/python3
import time

from art import tprint

from mycode.rpg_game.rpg_room import Room
import mycode.rpg_game.rpg_figures as rpf


def show_instructions():
    print('''
    =========================================================================================================
            Commands:
              go [direction]        invite [character]   give [item]
              get [item]            inspect [item]       help commands             
''')


def slow_print(string):
    for char in range(len(string)):
        print(string[char], end="")
        time.sleep(.7 / 10)


class Player:
    def __init__(self, start_room: str):
        self.room = Room(start_room)
        self.inventory = []

    def player_movement(self, movement):
        # check that they are allowed wherever they want to go
        if movement in self.room.neighbors_and_Items:
            future_room = self.room.neighbors_and_Items[movement]
            if future_room == "Study Room" and 's-key' not in self.inventory:
                message = "\n\nYou don't have the necessary items to enter this room.\n\n"
                slow_print(message)
            else:
                # set the current room to the new room
                self.room.player_in_room(future_room)
                # self.room_actor.interact()
        else:
            # there is no door (link) to the new room
            print('You can\'t go that way!')

    def player_inspect(self, inspect_item):
        # check that they are allowed wherever they want to go
        if inspect_item in self.room.items:
            if inspect_item.upper() == 'JOURNAL':
                rpf.journal_render()
                journal_entry = ("""
                    I have found evidence that this mansion was used by the Illuminati to conjure evil. Now I 
                just need to find out where they had the sacrificial altar. There has to be a hidden room somewhere
                in this mansion. I shall find it tomorrow. 
                                                                        -Ebeneezer Holmes 
                                                                            30 October 1929
                """)
                slow_print(journal_entry)
            # trap door, one way passage
            elif inspect_item.upper() == 'ILLUMINATI':
                rpf.book_case_render()
                trap_door = ("This book should help shed some light to what's happening here. What the...ahhhhhh! "
                             "I can't believe I just fell through a trap door.")
                slow_print(trap_door)
                self.room.player_in_room('Catacombs')
        else:
            print('NOT WORKING AHHHH!')

    def player_get(self, new_item):
        # if the room contains an item, and the item is the one they want to get
        if "item" in self.room.neighbors_and_Items and new_item in self.room.items:
            if new_item.upper() == 'JOURNAL' or new_item.upper() == 'ILLUMINATI':
                print("You can't collect this item, but you can inspect it")
            elif new_item.upper() == 'DEMON' or new_item.upper() == 'SERVANT' or \
                    new_item.upper() == 'TROLL':
                print("You can't collect this character.")
            # checking the inventory, player can't have more than 5 items at a time

            elif len(self.inventory) == 5:
                print("Your inventory is full! Do you want to drop an item?")
                drop_item = input('Yes or No: ').lower()
                if drop_item == "yes":
                    for count, item in enumerate(self.inventory, 0):
                        print(f'{count + 1})  {item}')
                    item_dropped = input("please enter the number for the item you want to drop:")
                    # add the dropped item from their inventory to the room item list
                    self.room.items.append(self.inventory[int(item_dropped) - 1])
                    # remove the item to their inventory
                    self.inventory.remove(self.inventory[int(item_dropped) - 1])
                    # add the item to their inventory
                    self.inventory.append(new_item)
                    # remove item from the room items
                    self.room.items.remove(new_item)
                    # display a helpful message
                    print(new_item + ' taken!')
                else:
                    print("You have kept all your items")
            else:
                # add the item to their inventory
                self.inventory.append(new_item)
                # display a helpful message
                print(new_item + ' taken!')
                # delete the item from the room
                self.room.items.remove(new_item)
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + new_item + '! Item is not in the room')

    def interact(self):
        if 'One Eyed Willy' in self.room.items:
            smell = ('The smell of burning tobacco is in the air and you see a man revealed by the bright moonlight '
                     'window. Who are you?')

            slow_print(smell)

            rpf.willy_render()
            willy_convo = ("""

            They call me One Eyed Willy, don't need no more info on me. I'm just going to warn you kid, this wing of
            the mansion has secrets you don't want to reveal, unless you're looking to become immortal. Theres an evil 
            presence here, be careful.

            """)

            slow_print(willy_convo)

        elif 'SERVANT' in self.room.items:
            rpf.bad_man_render()
            servant_convo = (""" 
            There's precious treasures in the pantry beyond the kitchen. Be weary of its guardian, for it will let 
            live only you can answer its question haha hahahaha HAHAHAHA 
            """)

            slow_print(servant_convo)

        elif 'DEMON' in self.room.items:
            rpf.monster_render()

            demon_convo = ("""
            I see my Willy has done well in leading the human sacrifice to find me. I will have to reward him now, after
            I'm done with you. Swish!! Splat!!
            """)
            slow_print(demon_convo)
            rpf.bloody_axe_render()
            tprint('''
              game
              over''', "amcaaa01")
        elif 'TROLL' in self.room.items:
            rpf.troll_render()
            troll_convo = ('I\'m the Bipartisan troll, the keeper of gold. To get the riches that lie beyond, '
                           'answer my '
                           'question in one try, reply incorrectly and your life will be gone')
            slow_print(troll_convo)
            answer = input("The more I lie, the more people trust me. What am I?").lower()
            if answer != "politician":
                print("Sorry that's incorrect, time for a snack ")
                rpf.bloody_sword_render()
                tprint('''
                  game
                  over''', "amcaaa01")
            else:
                passage = "You are worthy of passage."
                slow_print(passage)
        else:
            return

    def player_action(self, possible_action: str):
        possible_action = possible_action.lower().split(' ', 1)
        print(possible_action)
        if possible_action[0] == 'help':
            show_instructions()

        # if they type 'go' first
        elif possible_action[0] == 'go':
            self.player_movement(possible_action[1])
            self.interact()

        # if they type 'inspect' first
        elif possible_action[0] == 'inspect':

            # check that they are allowed wherever they want to go
            self.player_inspect(possible_action[1].upper())


         # if they type 'get' first
        elif possible_action[0] == 'get':

            # if the room contains an item, and the item is the one they want to get
            self.player_get(possible_action[1])

        else:
            print("This action is not supported")
            show_instructions()

    def show_status(self):
        # print the player's current status
        print('---------------------------')
        print('You are in the ' + self.room.this_room)
        # print the current inventory
        print('Inventory : ' + str(self.inventory))
        # print an item if there is one
        if "item" in self.room.this_room:
            print('You see a ' + self.room.items)
        print("---------------------------")
        self.room.room_description()
