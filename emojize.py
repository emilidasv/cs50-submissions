import emoji

def main():

    text =input("Input: ")

    if "," in text:

        text = text.split(",")

        print(text[0] + "," + emo(text[1]))

    else:

        print(emo(text))


def emo(name):

    try:

        tmp=emoji.emojize(name)

    except:

        pass

    else:

        tmp=emoji.emojize(name,language='alias')

    return tmp

main()
