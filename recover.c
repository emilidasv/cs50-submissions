#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

// Check for invalid usage should only be one argument
    if (!(argc == 2))
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    // OPen the file

    // Remember filenames
    char *infile = argv[1];
    int tmpnum = 0;
    char tmpfilename[10] = "dummy.jpg";


    // Open the input file with all the raw data

    FILE *ifileptr = fopen(infile, "r");
    FILE *imgptr;

    if (ifileptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }
    int blocksize = 512;
    BYTE buffer[blocksize];
    // READ one block from the file
    while (fread(buffer, 1, blocksize, ifileptr) == blocksize)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {

            if (tmpnum == 0)
            {
                // this is the first jpg block
                // create a new filename

                sprintf(tmpfilename, "%03i.jpg", tmpnum);
                imgptr = fopen(tmpfilename, "w");
                fwrite(buffer, 1, blocksize, imgptr);
            }
            else
            {
                // more jpg blocks after the first one, fisrt close old img
                fclose(imgptr);

                // open  new img file
                tmpnum++;
                sprintf(tmpfilename, "%03i.jpg", tmpnum);
                imgptr = fopen(tmpfilename, "w");
                fwrite(buffer, 1, blocksize, imgptr);
            }
        }
        else

            // block is not starting as a jpg
        {
            if (tmpnum > 1)
            {
                fwrite(buffer, 1, blocksize, imgptr);
            }

        }


    }


    // close the input file at the end
    fclose(imgptr);
    fclose(ifileptr);


}