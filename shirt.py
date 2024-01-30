import sys
import os
from PIL import Image, ImageOps
def main():

    input_filename = ""
    output_filename = ""

    check_user_input()
    shirtfile ="shirt.png"

    #open the infile
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    try:
        image = Image.open(input_filename)
    except:
        sys.exit("Input does not exist")

    shirtimage = Image.open("shirt.png")
    size =  shirtimage.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirtimage, shirtimage)
    muppet.save(output_filename)

def check_user_input():
    # check command-line argument

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #input file
    filename1 = sys.argv[1]
    input_filename = filename1
    #outputfile
    filename2 = sys.argv[2]
    output_filename = filename2

    try:
        fname1, ftype1 = filename1.split(".")
        fname2, ftype2 = filename2.split(".")

        if ((valid_type_file(ftype1)) and (valid_type_file(ftype2))):

            if ftype1.upper() != ftype2.upper():
                print("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    except:
         sys.exit("Invalid output")

def valid_type_file(filetype):
     #print(filetype)
     if filetype.lower() in ("jpg", "jpeg", "png"):
          return True
     else:
          return False


#def resize_paste_images(file_people, file_shirt, output_file):







if __name__ == "__main__":
    main()


