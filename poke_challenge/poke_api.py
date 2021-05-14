#!/usr/bin/env python3

# imports always go at the top of your code
import requests

poke_input = input("What pokemon do you want to look up? ").lower()


def main(pokemon):
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon).json()
    poke_img = pokeapi["sprites"]["front_default"]
    game_count = len(pokeapi["game_indices"])

    print(f"Image URL: {poke_img}")
    print(f"{pokemon} has been in {game_count} pokemon games")
    print("Moves: ", [item['move']['name'] for item in pokeapi['moves']])

    print(pokeapi)


main(poke_input)
