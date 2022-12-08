#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int length_of_creditnumber (long int n);
int calc_checksum (long int cnum, int len);
int calc_firstnumber(long int cnum, int len);
int valid_cardandTypeOfCard (int frstnum, int secnum, int len);

int main(void)
{
    /*prompt for input of creit card number*/

    long int creditnumber = get_long("Give me credit number");

    /* calculate lenth of creditcard number*/
    int length = length_of_creditnumber(creditnumber);
    /*p debug rintf("length of creditcard number is %i\n", length);*/


    /* calculate checksum - if valid creditcard number*/
    int checksum = calc_checksum (creditnumber, length);

    /*calculate first and second number on card*/
    int firstnumber = calc_firstnumber(creditnumber, length);
    int seclenght = length - 1;
    int secondnumber =calc_firstnumber (creditnumber, seclenght);

    /*check if card number fullfill requireent for AMEX , Mastercard or VISA
    VISA: starts with 4  - AND -  13 or 16 digits
    Master Card: starts with 51,52,53,54,55  - AND - 16 digits
    American Express: starts with 34 or 37 - AND - 15 digits
    */
    int status1 = valid_cardandTypeOfCard (firstnumber, secondnumber, length);


    /*Print result depending on if it has a valid checksum and is one of the required carr types */
    /* debug: printf("checksum: %i\n", checksum); */
    if ((checksum %10 != 0) || (status1 == 0))
    {
    printf("INVALID\n");
    }
    else
    {
    printf("Number: %li\n", creditnumber);
        if (status1 == 3)
        {
            printf("AMEX\n");
        }
        else if (status1 == 4)
        {
            printf("VISA\n");
        }
        else if (status1 == 5)
        {
            printf("MASTERCARD\n");
        }
    };


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
/* clculate checksum*/
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
/* check starting number of cnum*/
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

int valid_cardandTypeOfCard (int frstnum, int secnum, int len)

{
     /*check if card number fullfill requireent for AMEX , Mastercard or VISA
    VISA: starts with 4  - AND -  13 or 16 digits
    Master Card: starts with 51,52,53,54,55  - AND - 16 digits
    American Express: starts with 34 or 37 - AND - 15 digits
    */
    if ((frstnum == 4)&&((len == 13)||(len==16)))
    {
        /*printf("VISA\n");*/
        return 4;
    }
    else if (((frstnum == 3) && ((secnum == 4) || (secnum == 7) )) && (len == 15))
    {
        /*printf("AMEX\n");*/
        return 3;

    }
    else if (((frstnum == 5) && ((secnum > 0) && (secnum < 6)))&&(len == 16))
    {
        /*printf("MASTERCARD\n");*/
        return 5;

    }
    else
    {
        /*printf("INVALID\n");*/
        return 0;
    };


}

