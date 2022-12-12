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



                    }



                }
                keyarray[0][j] = tolower(argv[1][j]);
                keyarray[1][j] = charstring[j];

            }

        /* print key array*/
   /*     for (int j=0;j<26;j++)
        {   printf("keyarray index%i\n",j);


            printf(" argv[1][j]; %c", argv[1][j]);
            printf("charsting:%c", charstring[j]);
            printf("chif: %c", keyarray[0][j]);
            printf("char: %c\n", keyarray[1][j]);
        }*/
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

                    if ((tolower(tmpchar)) == keyarray[1][k])
                    {
                        if (((tmpchar)> 96) && ((tmpchar) < 123))
                        {
                            chifferstring[i] = keyarray[0][k];


                        }
                        else
                        {

                            chifferstring[i] = toupper(keyarray[0][k]);

                        }


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

  /*     for (int l=0;l<27;l++)
        {
            printf("L:%i", l);
            printf("keyarry%c", keyarray[0][l]);
            printf("charsting%c\n", keyarray[1][l]);
        }*/

        }



    };
}