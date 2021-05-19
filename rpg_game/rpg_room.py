#!/usr/bin/python3

import mycode.rpg_game.rpg_figures as rpf


class Room:
    # A dictionary linking a room to other rooms

    rooms = {
        'Hall': {
            'north': 'Bedroom',
            'south': 'Study Room',
            'east': 'Dining Room',
            'west': 'Trophy Room',
            'item': ['shield', 'sword']
        },
        'Trophy Room': {
            'east': 'Hall',
            'item': ['One Eyed Willy']
        },
        'Study Room': {
            'north': 'Hall',
            'west': 'Library',
            'item': ['g-key', 'JOURNAL']
        },
        'Library': {
            'north': 'Book Case',
            'item': ['ILLUMINATI']
        },
        'Catacombs': {
            'down': 'Pagan Altar',
            'item': []
        },
        'Pagan Altar': {
            'teleport': 'Road',
            'item': ['DEMON']
        },
        'Road': {
            'south': 'Home',
            'item': []
        },
        'Bedroom': {
            'south': 'Hall',
            'item': ['s-key', 'Lady']
        },
        'Kitchen': {
            'east': 'Pantry',
            'item': ['TROLL', 'ham']
        },
        'Pantry': {
            'west': 'Kitchen',
            'item': ['medicine', 'immortality serum']
        },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'north': 'Kitchen',
            'item': ['candle', 'SERVANT']
        },
        'Garden': {
            'north': 'Dining Room',
            'item': ['potion']

        }
    }

    def __init__(self, room_name: str):
        self.all_rooms = self.rooms
        self.this_room = room_name
        self.neighbors_and_Items = self.all_rooms[room_name]
        self.description = ''
        self.items = self.neighbors_and_Items['item']

    def player_in_room(self, in_room):
        self.this_room = in_room
        self.neighbors_and_Items = self.all_rooms[in_room]
        self.items = self.all_rooms[in_room]['item']

    def room_description(self):

        description_string = f'Your standing in a dimly lit {self.this_room}. \n'
        for i in self.neighbors_and_Items:
            if i != 'item':
                description_string += f" To the {i} it looks like a {self.neighbors_and_Items[i]}.\n"
        if len(self.items) != 0:
            items_string = f"You see a {', '.join(self.items)}"
            if self.neighbors_and_Items == 'Pantry':
                rpf.meds_render()
                rpf.serum_render()
            elif self.neighbors_and_Items == "Dining Room":
                rpf.candle_render()
            elif self.neighbors_and_Items == "Dining Room":
                rpf.candle_render()
            elif self.neighbors_and_Items == "Hall":
                rpf.sword_shield_render()
            elif self.neighbors_and_Items == "Bedroom" or self.neighbors_and_Items == "Study Room":
                rpf.key_render()
            elif self.neighbors_and_Items == "Garden":
                rpf.wolf_render()
            print(description_string, items_string)
        else:
            print(description_string, ".")
