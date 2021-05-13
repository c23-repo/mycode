#!/usr/bin/env python3

from subprocess import call


call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")


interface = input("Enter an interface, like, ens3: ")
# user to issue ip addr show dev, which will reveal IPv4 and IPv6 details.
call(["ip", "addr", "show", "dev", interface])

# user to issue ip route show dev, which will reveal IPv4 and IPv6 details.
call(["ip", "route", "show", "dev", interface])

