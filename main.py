from collections import Counter 

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    def count_words():
        print(len(file_contents.split()))
    count_words()

    def count_characters():
        lower = file_contents.lower()
        counts = Counter(lower)

        return counts
    
    def sort_on(dict):
        return dict["num"]

    def print_report():
        dictionary = {}
        lower = file_contents.lower()

        for c in lower:
            if c.isalpha():
                if c in dictionary:
                    dictionary[c] += 1
                else:
                    dictionary[c] = 1
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_characters()} words found in the document")



        for key in sorted(dictionary,key=dictionary.get,reverse=True):
            print(f"The '{key}' character was found {dictionary[key]} times")
        
        print("--- End report ---")

    print_report()
