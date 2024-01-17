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
            #print("text", text[i])
            tmp_output = emoji.emojize(text[i].strip())
            #print("tmp", tmp_output)
            if(emoji.is_emoji(tmp_output)):
                output = output + ", " +tmp_output
            else :
                # try with alias as well
                tmpput = emoji.emojize(text[i].strip(),language='alias')
                if (emoji.is_emoji(tmpput)):
                    output = output + ", " + tmpput
                else:
                    output = output + text[i]
            i = i + 1
        print(output)
    else:
        output = emoji.emojize(text,language='alias')
        print(output)


# hello, :earth_asia: is not working since this is an alias emojis and a coma in the sentence.
        # This program als assumes that the text comes first and all efter coma is emojies.
        # should probabley redo the order of the code since I am using two things twice. 



