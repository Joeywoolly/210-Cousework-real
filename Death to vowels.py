def vowel_remover(text):
    string = ""
    for l in text:
        if l.lower() != "a" and l.lower() != "e" and l.lower() != "i" and l.lower() != "o" and l.lower() != "u":
            string += l ## identifys all the letters that are going to be removed ## didnt work if that wasnt it lower case
    return string 
print (vowel_remover("Beautiful"))
