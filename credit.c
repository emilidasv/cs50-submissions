#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int length_of_creditnumber (long int n);
int calc_checksum (long int cnum, int len);
int calc_firstnumber(long int cnum, int len);
int printTypeOfCard (int frstnum, int secnum, int len);

int main(void)
{
    /*prompt for input of creit card number*/

    long int creditnumber = get_long("Give me credit number");
    printf("Number: %li\n", creditnumber);

    /* calculate checksum - if valid creditcard number*/

    int length = length_of_creditnumber(creditnumber);
    /*printf("length of creditcard number is %i\n", length);*/

    int checksum = calc_checksum (creditnumber, length);
    if (checksum %10 != 0)
    {
    printf("Unvalid\n");
    }
    else
    {
    int firstnumber = calc_firstnumber(creditnumber, length);
    int seclenght = length - 1;
    int secondnumber =calc_firstnumber (creditnumber, seclenght);
    int status1 = printTypeOfCard (firstnumber, secondnumber, length);
    }


}

int length_of_creditnumber (long int cnum)
    /* calculate length of creit card number */
{
    long int tmpcnum = cnum;
    int tmplen = 0;

    for (int i = 0; i < 20; i++)
    {

        /*if ((tmpcnum % 10) != 0 && (tmpcum != 0))*/
        if ((tmpcnum != 0))
        {
            tmplen=tmplen + 1;
            tmpcnum = tmpcnum / 10;
        }

    }

return tmplen;

}

int calc_checksum (long int cnum, int len)
{
    int tmpchecksum = 0;
    long int tmpcnum = cnum;
    int sumEveni = 0;
    int sumOddi = 0;

    for (int i = 0; i < len; i++)
    {
        if ((tmpcnum ) != 0)
        {

            int digit = tmpcnum % 10;

            if((i % 2) == 0)

                {sumEveni = sumEveni + digit;}
            else
                {digit = digit * 2;
                /* of only one digit*/
                if (digit / 10 == 0)
                {sumOddi = sumOddi + digit;}
                else
                {sumOddi = sumOddi + (digit % 10) + (digit / 10);};

                };

            tmpcnum = tmpcnum/10;

        }
    }
    int result_checksum = sumEveni + sumOddi;

return result_checksum;

}

int calc_firstnumber(long int cnum, int len)
{
    long int tmpcnum = cnum;
    int tmplen = len;
    int digit = 0;

    for (int i = 0; i < tmplen; i++)
    {
        if (tmpcnum  != 0)
        {

            digit = tmpcnum % 10;
            /*printf("Digit-cal first: %i\n", digit);*/

            tmpcnum = tmpcnum/10;
            /*printf("tmpcnum-cal first: %li\n", tmpcnum);*/
        }
    }

    return digit;
}

int printTypeOfCard (int frstnum, int secnum, int len)
{
    if ((frstnum == 4)&&((len == 13)||(len==16)))
    {
        printf("VISA\n");
    }
    else if (((frstnum == 3) && ((secnum == 4) || (secnum == 7) )) && (len == 15))
    {
        printf("American Express\n");
    }
    else if (((frstnum == 5) && ((secnum > 0) && (secnum < 6)))&&(len == 16))
    {
        printf("Master Card\n");
    }
    else
    {
        printf("Unknown\n");
    };
    /* print type of card*/
    /*
    VISA: starts with 4  - AND -  13 or 16 digits
    Master Card: starts with 51,52,53,54,55  - AND - 16 digits
    American Express: starts with 34 or 37 - AND - 15 digits
    */


     /* check length of number and starting numbers*/

     return 0;

}

