import emoji

def main():

    text =input("Input: ")

    if "," in text:

        text = text.split(",")

        print(text[0] + "," + create_emo(text[1]))

    else:

        print(emo(text))


def create_emo(name):

    try:

        output=emoji.emojize(name)

    except:

        pass

    else:

        output=emoji.emojize(name,language='alias')

    return output

main()
