#!/usr/bin/python3
for i in range(0, 99):
    if i != 89 and i / 10 < i % 10:
        print("{:0>2},".format(i), end=" ")
print(89)
