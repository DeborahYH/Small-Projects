# GETTING READY
# Dictionary: stores information in the form of key-value pairs = can be used to create a morse code chart
# keys = English characters
# values = morse code

import re

morse_dict = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.",
    "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..",
    "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.",
    "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
    "Y":"-.--", "Z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-",
    "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----"
}

#message = "Goats have slit pupils which enhances their field of view"
message = "Hi there"
words = []

# ENCRYPTION 
# 1. Extract each character (if not space) from the string and match it with its corresponding morse code stored in the dictionary
# 2. While encoding in morse code we need to add 1 space between every character and 2 consecutive spaces between every word.
# 2. Store the morse code in a variable that will contain our encoded string and then we add a space to our string that will contain the result.
# 4. If the character is a space then add another space to the variable containing the result. We repeat this process till we traverse the whole string

clean_message = message.upper()
print(clean_message)

# Compares char to each dictionary value
# If they are equal, char receives the dictionary morse value
for char in clean_message:
    # Add 1 space between characters + add 2 spaces between words
    if(char.isspace() is False):
        morse_char = morse_dict[char] + " "
        words.append(morse_char)
    else:
        words.append("  ")
print(words)

# Use join() to store the morse code in a variable with a space at the end
morse_message_sent = "".join(words)
print(morse_message_sent)


# DECRYPTION
# 1. we start by adding a space at the end of the string to be decoded (this will be explained later).
#morse_message_received = morse_message_sent.ljust((len(morse_message_sent)+1), " ")
#print(morse_message_received)

morse_message_received = ".... ..   - .... . .-. . "

# 2. Now we keep extracting characters from the string till we are not getting any space.
final_string = ""
full_char = ""
converted_char = ""
received_letter = ""
space = 0

morse_code = morse_message_received.split(' ')
result_message = ''
 
for code in morse_code:      
    for key, value in morse_dict.items():
        if code == "":
            result_message += " "
            break
        elif code == value:
            result_message += key
            break

while "  " in result_message:
    result_message = result_message.replace("  ", " ")

print("Morse: ", morse_code)
print("Final: ", result_message)

# definir uma função para detectar espaço duplo retornando true/false. Dependendo do numero de espaços, faz uma ação 
    
# 3. As soon as we get a space we look up the corresponding English language character to the extracted sequence of characters (or our morse code) and add it to a variable that will store the result.
# 4. Remember keeping track of the space is the most important part of this decryption process. As soon as we get 2 consecutive spaces we will add another space to our variable containing the decoded string.
# 5. The last space at the end of the string will help us identify the last sequence of morse code characters (since space acts as a check for extracting characters and start decoding them).


# EXTRAS
# Dividir em funções
# Validar mensagem de input (impedir uso de caracteres que não sejam alfanuméricos)
# Adicionar opção de testar o programa usando uma string padrão
