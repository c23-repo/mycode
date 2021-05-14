#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def grab_agriculture_f1(index, no_veg=False):
    agriculture = farms[index]['agriculture']
    veggies = ["carrots", "celery"]
    print(agriculture)

    if no_veg is True:
        for veg in veggies:
            if veg not in agriculture:
                continue
            else:
                agriculture.remove(veg)

    print(agriculture)
    string = ", ".join(agriculture)
    return string


def grab_farm_f2_n_f3(farm_num, no_veg):
    if farm_num > 1:
        farm_num -= 1
    print(f"\nThe {farms[farm_num]['name']} agriculture consists of {grab_agriculture_f1(farm_num, no_veg)}")


def main():
    grab_farm_f2_n_f3(0, False)

    picked_farm = input("choose a farm: 1 for NE Farm, 2 for W Farm, 3 for SE Farm:  ")
    print(int(picked_farm))
    grab_farm_f2_n_f3(int(picked_farm), False)

    picked_farm_only_animals = input("choose a farm and only display agriculture: 1 for NE Farm, 2 for W Farm, "
                                     "3 for SE Farm:  ")

    grab_farm_f2_n_f3(int(picked_farm_only_animals), True)


main()

