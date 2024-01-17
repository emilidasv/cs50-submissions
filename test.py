import emoji

text =input("Input: ")

if text.count(",")>0:
    text = text.split(",")
    print(text)
    text= text[1].strip()

    if (emoji.is_emoji(text)) : print("is emoji")
    output = emoji.emojize(text)

    if (emoji.is_emoji(output)) : print("output is emoji")


