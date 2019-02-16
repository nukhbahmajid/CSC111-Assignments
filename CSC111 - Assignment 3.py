# ---------------------------------------------------------------------------
#        Name: Nukhbah Majid (I didn't collaborate with anyone from class
#              on this assignment)
#    Filename: Assignment3.py
#        Date: 09/29/18 
#
# Description: Devise a calculator that allows manipulation user's string
#              inputs in many ways. For example uppercasing and lowercasing
#              the characters, capitalizing initials, repeating vowels, 
#              displaying string backwards etc. 
# ---------------------------------------------------------------------------


def main():
    userstring = str(input("Enter a sentence: "))

    print("0.", userstring)


    print("1a.", userstring.upper())


    print("1b.", userstring.lower())


    print("2.", doublevowels(userstring))


    print("3.", abbrev(userstring))

    
    print("4.", titlize(userstring))


    print("5.", reverse(userstring))




def doublevowels(userstring):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        userstring = userstring.replace(vowel, vowel + vowel)
    return userstring



def abbrev(userstring):
    if len(userstring) < 10:
        return userstring
    else:
        first5 = userstring[0:5]
        last5 = userstring[-5:]
        userstring = (first5 + "..." + last5)
        return userstring



def titlize(userstring):
    spaces = []
    for word in userstring.split():
        spaces.append(word[0].upper() + word[1:])
        
    return " ".join(spaces)



def reverse(userstring):
    if len(userstring) == 0:
        return userstring
    else:
        return reverse(userstring[1:]) + userstring[0]

        
        
main()

#-----------------------------------------------------------------------------

# REFERENCES:
# I got help from our textbook: python programming by john zelle for "for"
# statements, chapter 5.4.2
# I googled how to use a function to make the vowels in a word repeat
# and found out this useful link of a Stackoverflow forum:
# https://stackoverflow.com/questions/7301292/string-replace-vowels-in-python
# I worked on this assignment with CSC111 TA Anastasia for capitalize initials 

