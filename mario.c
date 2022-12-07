#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int height = 0;

    /* reject if input is not between 0 and 9 */
    while ((height < 1) || (height > 8))
    {
        /* Ask for the user for height */
        height = get_int("Hi, How high should the pyramid be, 1-8 ?\n");
    }
    if ((height > 0) && (height < 9))

    {
        for (int i = 0; i < height; i++)

        {
            int amountofdashes = i + 1;
            for (int k = amountofdashes; k < height; k++)
            {

                printf(" ");

            }
            for (int j = 0; j < amountofdashes; j++)
            {

                printf("#");

            }
            printf("\n");
        }
    }
}


