import emoji
text = input("Input:")

output = emoji.emojize(text)
if (emoji.is_emoji(output)):
    print ("Output:", output)
else:
    #print(text)
    if text.count(",") > 0:
        print(text)
        text = text.split(",")
        output =text[0] + "," + emoji.emojize(text[1])
        print(emoji.emojize(text[1]))
        print(output)






