import emoji
text = input("Input:")

output = emoji.emojize(text)
if (emoji.is_emoji(output)):
    print ("Output:", output)
else:
    #print(text)
    if text.count(",") > 0:
        text = text.split(",")
        i=0
        output =""
        while (i < len(text)) :
            print("text", text[i])
            tmp_output = emoji.emojize(text[i])
            print("tmp", tmp_output)
            if(emoji.is_emoji(tmp_output)):
                output = output + tmp_output
                print("outpit is", output)
            else :
                output = output + text[i]
                print("iutput not", output)
            i = i + 1
        print(output)






