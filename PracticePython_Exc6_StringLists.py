string = raw_input("What is your string? ")

lst = []
for letter in string:
    print "one letter: " + letter
    lst.append(letter)

print lst[0:len(lst)]

#second list adds letters from last to first index.
palindrome = []
index = len(lst)
for x in lst:
    index = index -1
    if index >= 0:
        print lst[index]
        palindrome.append(lst[index])


print palindrome

#combine all letter strings into one line.
print ''.join(palindrome)
