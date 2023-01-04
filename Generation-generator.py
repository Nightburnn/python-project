#!/usr/bin/python3

print("welcome to Generation generator. We tell you what generation you are from")
print()

year = int(input("what is your birth year: "))
print()

if year <= 1946:
    print("Greetings TRADITIONALIST")
elif year >= 1947 and <= 1964:
    print("your Generation are called BABY BOOMERS")
elif year >= 1965 and <= 1981:
    print("GEN X!!")
elif year >= 1982 and <= 1995:
    print("the age of tech! MILLENIALS")
elif year >= 1996:
    print("it's giving GEN Z")
else:
    print("please pick a year")
