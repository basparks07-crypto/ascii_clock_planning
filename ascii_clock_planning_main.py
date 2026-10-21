# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:  Tyler Haidaczuk
# Jai Joshi
# Benjamin Sparks
# NA
# Section: 571
# Assignment: Lab Topic 8 Team
# Date: 20 October 2026
#
# Takes input and breaks it down into usable variabqles for the clock. It also checks if the character is permitted and if the time is in 12 Hr or 24 Hr format.
time = input("Enter the time: ")
clock_type = int(input("Choose the clock type (12 or 24): "))
char = input("Enter your preferred character: ")
while char not in "abcdeghkmnopqrsuvwxyz@$&*= ":
    char = input("Character not permitted! Try again: ")
print()
hour=int(int(time[0:2].strip(":")))
hour_10=hour//10
hour_1=hour%10
minutes_10=int(time[-2])
minutes_1=int(time[-1])
# If in 12 Hr mode, convert the hour to 12 Hr format and set the morning variable to either AM or PM
if clock_type==12:
    if hour>12:
        morning=11
        hour=hour-12
        hour_10=hour//10
        hour_1=hour%10
    elif hour==12:
        morning=11
    elif hour==0:
        hour=hour+12
        morning=12
        hour_10=hour//10
        hour_1=hour%10
    else:
        morning=12
# Begins Printing out the clock in 12 Hr mode        
if clock_type==12:
    if char=="": # Dictionary for if user doesnt input a character, it will default to the number being printed out
        Line_one={0: f"000", 1: f" 1 ", 2: f"222", 3: f"333", 4: f"4 4", 5: f"555", 6: f"666", 7: f"777", 8: f"888", 9: f"999", 12: " A ", 11: f"PPP"}
        Line_two={0: f"0 0", 1: f"11 ", 2: f"  2", 3: f"  3", 4: f"4 4", 5: f"5  ", 6: f"6  ", 7: f"  7", 8: f"8 8", 9: f"9 9", 12: f"A A", 11: f"P P"}
        Line_three={0: f"0 0", 1: f" 1 ", 2: f"222", 3: f"333", 4: f"444", 5: f"555", 6: f"666", 7: f"  7",	8: f"888",	9: f"999",	12:	f"AAA",	11:	f"PPP"}
        Line_four={0: f"0 0", 1: f" 1 ", 2: f"2  ", 3: f"  3", 4: f"  4", 5: f"  5", 6: f"6 6", 7: f"  7", 8: f"8 8", 9: f"  9", 12: f"A A", 11: f"P  "}
        Line_five={0: f"000", 1: f"111", 2: f"222", 3: f"333", 4: f"  4", 5: f"555", 6: f"666", 7: f"   7", 8: f"888", 9: f"999", 12: f"A A", 11: f"P  "}
        if hour_10==1: # If the hour is 10, 11, or 12, it will print out the first digit of the hour as well as the second digit of the hour
            print(Line_one[hour_10]+" "+Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1]+" "+Line_one[morning]+" M   M")
            print(Line_two[hour_10]+" "+Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1]+" "+Line_two[morning]+" MM MM")
            print(Line_three[hour_10]+" "+Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1]+" "+Line_three[morning]+" M M M")
            print(Line_four[hour_10]+" "+Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1]+" "+Line_four[morning]+" M   M")
            print(Line_five[hour_10]+" "+Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1]+" "+Line_five[morning]+" M   M")
        elif hour_10==0:# If the hour is 1-9, it will only print out the second digit of the hour to avoid printing a leading 0
            print(Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1]+" "+Line_one[morning]+" M   M")
            print(Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1]+" "+Line_two[morning]+" MM MM")
            print(Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1]+" "+Line_three[morning]+" M M M")
            print(Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1]+" "+Line_four[morning]+" M   M")
            print(Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1]+" "+Line_five[morning]+" M   M")
    else: # Dictionary for if user inputs a character, it will print out the character instead of the number
        Line_one={0: f"{char}{char}{char}", 1: f" {char} ", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"{char} {char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"{char}{char}{char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: " A ", 11: f"PPP"}
        Line_two={0: f"{char} {char}", 1: f"{char}{char} ", 2: f"  {char}", 3: f"  {char}", 4: f"{char} {char}", 5: f"{char}  ", 6: f"{char}  ", 7: f"  {char}", 8: f"{char} {char}", 9: f"{char} {char}", 12: f"A A", 11: f"P P"}
        Line_three={0: f"{char} {char}", 1: f" {char} ", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"{char}{char}{char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"  {char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: f"AAA", 11: f"PPP"}
        Line_four={0: f"{char} {char}", 1: f" {char} ", 2: f"{char}  ", 3: f"  { char }", 4: f"  { char }", 5: f"  { char }", 6: f"{ char } { char }", 7: f"  { char }", 8: f"{ char } { char }", 9: f"  {char}", 12: f"A A", 11: f"P  "}
        Line_five={0: f"{char}{char}{char}", 1: f"{char}{char}{char}", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"  {char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"  {char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: f"A A", 11: f"P  "}
        if hour_10==1: # If the hour is 10, 11, or 12, it will print out the first digit of the hour as well as the second digit of the hour
            print(Line_one[hour_10]+" "+Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1]+" "+Line_one[morning]+" M   M")
            print(Line_two[hour_10]+" "+Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1]+" "+Line_two[morning]+" MM MM")
            print(Line_three[hour_10]+" "+Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1]+" "+Line_three[morning]+" M M M")
            print(Line_four[hour_10]+" "+Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1]+" "+Line_four[morning]+" M   M")
            print(Line_five[hour_10]+" "+Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1]+" "+Line_five[morning]+" M   M")
        elif hour_10==0: # If the hour is 1-9, it will only print out the second digit of the hour to avoid printing a leading 0
            print(Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1]+" "+Line_one[morning]+" M   M")
            print(Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1]+" "+Line_two[morning]+" MM MM")
            print(Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1]+" "+Line_three[morning]+" M M M")
            print(Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1]+" "+Line_four[morning]+" M   M")
            print(Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1]+" "+Line_five[morning]+" M   M")
# Begins Printing out the clock in 24 Hr mode
elif clock_type==24:
    if char=="": # Dictionary for if user doesnt input a character, it will default to the number being printed out
        Line_one={0: f"000", 1: f" 1 ", 2: f"222", 3: f"333", 4: f"4 4", 5: f"555", 6: f"666", 7: f"777", 8: f"888", 9: f"999", 12: " A ", 11: f"PPP"}
        Line_two={0: f"0 0", 1: f"11 ", 2: f"  2", 3: f"  3", 4: f"4 4", 5: f"5  ", 6: f"6  ", 7: f"  7", 8: f"8 8", 9: f"9 9", 12: f"A A", 11: f"P P"}
        Line_three={0: f"0 0", 1: f" 1 ", 2: f"222", 3: f"333", 4: f"444", 5: f"555", 6: f"666", 7: f"  7", 8: f"888", 9: f"999", 12: f"AAA", 11: f"PPP"}
        Line_four={0: f"0 0", 1: f" 1 ", 2: f"2  ", 3: f"  3", 4: f"  4", 5: f"  5", 6: f"6 6", 7: f"  7", 8: f"8 8", 9: f"  9", 12: f"A A", 11: f"P  "}
        Line_five={0: f"000", 1: f"111", 2: f"222", 3: f"333", 4: f"  4", 5: f"555", 6: f"666", 7: f"   7", 8: f"888", 9: f"999", 12: f"A A", 11: f"P  "}
        if hour_10==1: # If the hour is 10, 11, or 12, it will print out the first digit of the hour as well as the second digit of the hour
            print(Line_one[hour_10]+" "+Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1])
            print(Line_two[hour_10]+" "+Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1])
            print(Line_three[hour_10]+" "+Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1])
            print(Line_four[hour_10]+" "+Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1])
            print(Line_five[hour_10]+" "+Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1])
        elif hour_10==0: # If the hour is 1-9, it will only print out the second digit of the hour to avoid printing a leading 0
            print(Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1])
            print(Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1])
            print(Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1])
            print(Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1])
            print(Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1])
    else:# Dictionary for if user inputs a character, it will print out the character instead of the number
        Line_one={0: f"{char}{char}{char}", 1: f" {char} ", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"{char} {char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"{char}{char}{char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: " A ", 11: f"PPP"}
        Line_two={0: f"{char} {char}", 1: f"{char}{char} ", 2: f"  {char}", 3: f"  {char}", 4: f"{char} {char}", 5: f"{char}  ", 6: f"{char}  ", 7: f"  {char}", 8: f"{char} {char}", 9: f"{char} {char}", 12: f"A A", 11: f"P P"}
        Line_three={0: f"{char} {char}", 1: f" {char} ", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"{char}{char}{char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"  {char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: f"AAA", 11: f"PPP"}
        Line_four={0: f"{char} {char}", 1: f" {char} ", 2: f"{char}  ", 3: f"  { char }", 4: f"  { char }", 5: f"  { char }", 6: f"{ char } { char }", 7: f"  { char }", 8: f"{ char } { char }", 9: f"  {char}", 12: f"A A", 11: f"P  "}
        Line_five={0: f"{char}{char}{char}", 1: f"{char}{char}{char}", 2: f"{char}{char}{char}", 3: f"{char}{char}{char}", 4: f"  {char}", 5: f"{char}{char}{char}", 6: f"{char}{char}{char}", 7: f"  {char}", 8: f"{char}{char}{char}", 9: f"{char}{char}{char}", 12: f"A A", 11: f"P  "}
        if hour_10==1: # If the hour is 10, 11, or 12, it will print out the first digit of the hour as well as the second digit of the hour
            print(Line_one[hour_10]+" "+Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1])
            print(Line_two[hour_10]+" "+Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1])
            print(Line_three[hour_10]+" "+Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1])
            print(Line_four[hour_10]+" "+Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1])
            print(Line_five[hour_10]+" "+Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1])
        elif hour_10==0: # If the hour is 1-9, it will only print out the second digit of the hour to avoid printing a leading 0
            print(Line_one[hour_1]+"   "+Line_one[minutes_10]+" "+Line_one[minutes_1])
            print(Line_two[hour_1]+" "+":"+" "+Line_two[minutes_10]+" "+Line_two[minutes_1])
            print(Line_three[hour_1]+"   "+Line_three[minutes_10]+" "+Line_three[minutes_1])
            print(Line_four[hour_1]+" "+":"+" "+Line_four[minutes_10]+" "+Line_four[minutes_1])
            print(Line_five[hour_1]+"   "+Line_five[minutes_10]+" "+Line_five[minutes_1])
