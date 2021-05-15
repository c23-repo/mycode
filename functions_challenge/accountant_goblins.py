#!/usr/bin/python3

def main():
    ledger_list = []

    with open('puzzle1.txt', 'r') as ledger_file:
        ledger = ledger_file.read()
        string_ledger = ledger.splitlines()

    for i in string_ledger:
        ledger_list.append(int(i))

    match_num = 2020
    find2_num_sum(ledger_list, match_num)
    find3_num_sum(ledger_list, match_num)


def find2_num_sum(num_list, match_sum):
    for i in range(0, len(num_list)):
        right_index = len(num_list) - 1

        while i < right_index:
            if num_list[i] + num_list[right_index] == match_sum:
                print(f"\n\nThe two numbers that sum up to {match_sum} are: {num_list[i]} and {num_list[right_index]}. "
                      f"Their multiple is {num_list[i] * num_list[right_index]}")
                break
            else:
                right_index -= 1


def find3_num_sum(num_list, match_sum):
    # Sort elements
    num_list.sort()

    for i in range(0, len(num_list) - 2):
        # Set the far left index and far right index
        left_index = i + 1
        right_index = len(num_list) - 1

        while left_index < right_index:
            if num_list[i] + num_list[left_index] + num_list[right_index] == match_sum:
                print(f"\n\nThe three numbers that sum up to {match_sum} are: {num_list[i]}, {num_list[left_index]},"
                      f" {num_list[right_index]}. Their multiple is "
                      f"{num_list[i] * num_list[left_index] * num_list[right_index]}")
                break
            elif num_list[i] + num_list[left_index] + num_list[right_index] < match_sum:
                left_index += 1
            else:
                right_index -= 1


main()

