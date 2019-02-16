# ----------------------------------------------------------------------
#        Name: Nukhbah Majid (I did not collaborate with anyone on this
#              assignment) 
#    Filename: Pig Latin Encrypt/Decrypt
#        Date: 10/12/18 
# Description: Pig Latin generator from user input, and decrypt back to
#              original user input.  
# ----------------------------------------------------------------------


def encrypt(user_input):
    word_list = user_input.split()
    vowel = ["A", "E", "I", "O", "U", "Y"]
    newPhrase = []
    for i in range(len(word_list)):
        word_list[i] = word_list[i] + "*"
        for j in range(len(word_list[i])):
            if word_list[i][j] in vowel:
                part_1 = word_list[i][:j]
                part_2 = word_list[i][j:]
                if j == 0:
                    newWord = part_2 + part_1 + "~WAY"
                    newPhrase.append(newWord)
                    break
                else:
                    newWord = part_2 + part_1 + "AY"
                    newPhrase.append(newWord)
                    break

    phrase = (" ").join(newPhrase)
    return phrase
        


    

def decrypt(phrase):
    word_list2 = phrase.split()
    normal_string = []
    for i in word_list2:
        if "~WAY" in i:
            i = i[:-5]
            normalWord = i
        else:
            i = i[:-2]
            location = i.find("*")
            normalWord = i[location + 1:] + i[:location]

        normal_string.append(normalWord)
    normalString = (" ").join(normal_string)
    return normalString


def main():
    user_input = input("Enter a phrase: ")

    user_input = user_input.upper()
    #print(user_input)

    encrypted_msg = encrypt(user_input)

    decrypted_msg = decrypt(encrypted_msg)


    print(encrypted_msg)
    print("")
    print(decrypted_msg)
    



if __name__ == "__main__":
    main()

#------------------------------------------------------------------------
# References: Got help from TAs: Georgina and Anastasia
