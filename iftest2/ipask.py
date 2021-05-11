#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
elif ipchk: #if any data is provided, this will test true
    print("looks like the IP address was set: " + ipchk + " This is not recommended.")
else: #if data is NOT provided
    print("You did not provide input.")

