#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    /*int lenghtofkey = strlen(argv[]);*/
    string charstring = "abcdefghijklmnopqrstuvwxyz";
    int len = 26;
    int keyarray[2][26];

    /*Make sure correct amount of arguments*/
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else
    {
        /*Caluclate lenthf of key */
        string key = argv[1];
        int arglen = strlen(argv[1]);
        if (arglen != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;

        }
        else
        {
            /* Is key valid all alpha characters only once*/

            for (int j = 0; j < 26; j++)
            {
                char tmpkeychar = tolower(argv[1][j]);
                if (!(tmpkeychar> 96) && (tmpkeychar < 123))
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
                else
                {
                    /* Is key valid - characters only once*/
                    for ( int i = j + 1; i < 26; i++)
                    {
                        char nextkeychar = tolower(argv[1][i]);
                        if (tmpkeychar == nextkeychar)
                        {
                            printf("Key must contain 26 characters.\n");
                            return 1;

                        };

                keyarray[0][j] = argv[1][j];
                keyarray[1][j] = charstring[j];

                    }



                }


            }
        string userInputtext = get_string("plaintext:");
        int lenoftext1 = strlen(userInputtext);
        /*  Create the chiffer*/
        char chifferstring[lenoftext1];
        for (int i = 0; i < lenoftext1 ;i++)
        {
            char tmpchar = userInputtext[i];
            if (!((tolower(tmpchar)> 96) && (tolower(tmpchar) < 123)))
            {
                chifferstring[i] = userInputtext[i];
            }
            else
            {
                for (int k = 0; k < 26; k++)
                {
                    if (tolower(tmpchar) == keyarray[1][k])
                    {
                    chifferstring[i] = keyarray[0][k];
                    };

                }

            }






        };


        /*  Print out the chiffer*/
        printf("ciphertext: ");
        for (int i = 0; i < lenoftext1 ;i++)
        {

            printf("%c", chifferstring[i]);




        };
        printf("\n");



        }



    };
}