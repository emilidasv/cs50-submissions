import sys
import os
from PIL import Image, ImageOps
def main():

    check_user_input()
    shirt1 = Image.open("before1.jpg")
    shirt2 = Image.open("cs50_Tshirt.png")
    shirt1.save("before1.png")

    size1 = shirt1.size
    #print(size1)

    #size2 = shirt2.size
    #print(size2)
    #photo.paste(shirt1, shirt2)

def check_user_input():
    # check command-line argument

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #input file
    filename1 = sys.argv[1]
    #outputfile
    filename2 = sys.argv[2]

    try:
        fname1, ftype1 = filename1.split(".")
        fname2, ftype2 = filename2.split(".")

        if (valid_type_file(ftype1) and valid_type_file(ftype2)):

            if ftype1.upper() != ftype2.upper():
                #print("Both files seems to be correct")
            #else:
                print("Input and output have different extensions")
                #sys.exit("Invalid output22")
        else:
            sys.exit("Invalid output")
    except:
         sys.exit("Invalid output")
    file_shirt ="shirt.png"
    #print(file_shirt)  shirt.png
    #print(filename1)   before1.png
    #print(filename2)   after1.png
    #print(ftype1)
    #print(ftype2)
    if (ftype1.lower()!= "png"):
        # open a file in jpg or jpeg and save as temporary png file"
        try:
            pngfile = Image.open(filename1)
            pngfile.save("tmp_filename1.png")
            pngfile.close()
            filename1 = "tmp_filename1.png"
        except:
            sys.exit("Input does not exist")

    resize_paste_images(filename1, file_shirt, filename2)

def resize_paste_images(file_people, file_shirt, output_file):
    try:
        with Image.open(file_shirt) as shirt_picture:

            size1 = shirt_picture.size

            with Image.open(file_people) as im:
                ImageOps.fit(im, size1).save("tmp_resized_person.png")
                Image.open("tmp_resized_person.png")
    except:
        sys.exit("Input does not exist")

    # open the image
    Image1 = Image.open("tmp_resized_person.png")

    # make a copy the image so that the
    # original image does not get affected
    Image1copy = Image1.copy()
    Image2 = Image.open(file_shirt)
    Image2copy = Image2.copy()

    # paste image giving dimensions
    Image1copy.paste(Image2copy, (0, 0), Image2copy)

    # save the image
    Image1copy.save(output_file)
    # close and cleanup tempory files
    Image1.close()
    Image2.close()
    Image1copy.close()
    Image2copy.close()
    os.remove("tmp_resized_person.png")
    os.remove("tmp_filename1.png")



def valid_type_file(filetype):
     #print(filetype)
     if filetype.lower() in ("jpg", "jpeg", "png"):
          return True
     else:
          return False


if __name__ == "__main__":
    main()


