#!/usr/bin/python3
z = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - z)), end="")
    z = 0 if z == ord('a') - ord('A') else ord('a') - ord('A')
