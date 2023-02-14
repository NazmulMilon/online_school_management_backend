user_input = input()


def acronym(string):
    phrase = ""
    exclude_words = ["a", 'an', 'the', 'of', '&', 'and', 'for', 'on']

    changed_input = string.split()

    for word in changed_input:
        if word.lower() not in exclude_words:
            phrase += word[0].upper()

    return phrase


print(acronym(user_input))
