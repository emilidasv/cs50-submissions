
# grinning face
# print("\U0001f600")

# grinning squinting face
# print("\U0001F606")

# rolling on the floor laughing
# print("\U0001F923")

def main():
    text = input()
    #print(text)
    text = convert(text)
    print(text)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    text = text.replace(":-)", "\U0001f600")
    return text


main()
