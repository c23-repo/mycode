#!/usr/bin/python3

from rpg_characters import Player
import rpg_figures as rpf
from art import *
import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

s = 'sound'
start_room_int = "Hall"


class Game:
    def __init__(self, start_room: str):
        self.player = Player(start_room)
        self.audio_off = False
        self.game_music = pygame.mixer.music

    def switch_music(self):

        if self.player.room.this_room == "Catacombs" or self.player.room.this_room == "Pagan Altar":
            location_audio = "Sewer-Monsters-Town-Hall-Meeting_Looping.mp3"
            self.game_music.stop()
            self.game_music.unload()
        elif self.player.room.this_room == "Library":
            location_audio = "Closing-In_Looping.mp3"
            self.game_music.stop()
            self.game_music.unload()
        else:
            print("we in the music", self.player.room.this_room)
            location_audio = "City-of-the-Disturbed_Looping.mp3"

        self.game_music.load(os.path.join(s, location_audio))
        self.game_music.set_volume(0.15)
        self.game_music.play(-1)

    def toggle_audio(self):
        if not self.audio_off:
            self.game_music.fadeout(3)
            self.game_music.unload()
            return self.switch_music()
        else:
            return self.game_music.stop()

    def title_screen(self):
        self.game_music.load(os.path.join(s, "Horror-Game-Intro.mp3"))
        self.game_music.set_volume(0.15)
        self.game_music.play(-1)

        # print a main menu and the commands
        rpf.haunted_hill_house_render()
        tprint('''
      the
    haunting''', "amcaaa01")

        user_audio = input('To turn of audio type T + Enter, otherwise press Enter to begin:   ').upper()

        if user_audio == 'T':
            self.audio_off = True
        self.toggle_audio()

    def game_loop_start(self):

        while True:
            self.player.show_status()

            # get the player's next 'move'
            # .split() breaks it up into an list array
            # eg typing 'go east' would give the list:
            # ['go','east']
            move = ''
            while move == '':
                move = input('>>>  ')

            self.player.player_action(move)
            # self.switch_music()

            # Define how a player can win
            if self.player.room.this_room == 'Garden' and 'key' in self.player.inventory and \
                    'potion' in self.player.inventory:
                print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
                break


def main():
    start_game = Game(start_room_int)
    start_game.title_screen()
    start_game.game_loop_start()


if __name__ == '__main__':
    main()
