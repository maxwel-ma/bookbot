def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    words = file_contents.split()
    print(len(words))
    x = charcount(file_contents)
    sorted_chars = alphasort(x)
    report(sorted_chars)

def charcount (file_contents):
    characters = {}
    lowered_book = file_contents.lower()
    for i in lowered_book:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def sorton(dict):
    return dict["count"]

def alphasort(dict):
    sortedlist = []
    for i in dict:
        if i.isalpha():
            sortedlist.append({"char": i, "count": dict[i]})
    sortedlist.sort(key=sorton, reverse=True)
    return sortedlist

def report(chars):
    for entry in chars:
        print(f"The '{entry['char']}' character was found {entry['count']} times")
main()