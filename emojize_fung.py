import emoji

def main():

    text =input("Input: ")

    if "," in text:

        text = text.split(",")

        print(text[0] + "," + create_emo(text[1]))

    else:

        print(create_emo(text))


def create_emo(name):

    try:

        tmp=emoji.emojize(name)


    except:

        pass

    else:

        tmp=emoji.emojize(name,language='alias')

    return tmp

main()
