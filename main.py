alphabet_dictionary = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,
            "j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,
            "s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}


def main ():
    # ADD YOUR BOOK NAME HERE, REPLACE frankenstein.txt
    with open("./books/frankenstein.txt") as whole_text:
    # -----------------------------
        read_text = whole_text.read()
        text_as_lower_case = read_text.lower()
        split_text = text_as_lower_case.split()
    for word in split_text:
        for letter in word:
            if (letter.isalpha()):
               alphabet_dictionary[letter] += 1
    user_input = input("Do you want to sort the letter from largest to smallest? type Y/N and press enter ")
    
    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"{len(split_text)} words found in the document \n")
    if(user_input == "Y"):
        sorted_dict = dict(sorted(alphabet_dictionary.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_dict:
            print(f"The '{key}' character was found {alphabet_dictionary[key]} times")
    else:
        for key in alphabet_dictionary:
            print(f"The '{key}' character was found {alphabet_dictionary[key]} times")
        

main()
