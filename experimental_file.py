the_string = input('Enter ye olde string: ')
splitty = input('What do you want to split on? ')

# the string is empty
if not splitty:
    #    don't put anything into the split argument
    split_string = the_string.split()
else:
    # do put the thing in
    split_string = the_string.split(splitty)

print(split_string)
# join me and together we will rule the universe as... whoever
# separator.join
print("|-|".join(split_string))