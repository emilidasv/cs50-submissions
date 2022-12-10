#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void)
{

string userInputtext = get_string("please give me the text:\n");
int lenoftext1 = strlen(userInputtext);
int asciinumber = 0;
int nextchar = 0;
int numbersofletters = 0;
int numbersofwords = 0;
int numbersofsentences = 0;


    for (int i = 0; i < lenoftext1; i++)
    {
        asciinumber = userInputtext[i];
        nextchar = userInputtext[i + 1];
        if (nextchar == 32 )
        {
            numbersofwords++;
        };

        if (((asciinumber > 64) && (asciinumber < 91)) || ((asciinumber > 96) && (asciinumber < 123)))
        {
            numbersofletters++;

            /*if (!(((nextchar > 64) && (nextchar < 91)) || ((nextchar > 96) && (nextchar < 123))))

            {
                numbersofwords++;
            }*/
        }
        else if ((asciinumber == 46) || (asciinumber == 33) ||( asciinumber == 63))
        {
            numbersofsentences++;
        }


}
numbersofwords++;

/*printf("letter: %i\n", numbersofletters);
printf("word: %i\n", numbersofwords);
printf("sentences: %i\n", numbersofsentences);*/

float avgletters = 0;
float avgsentences = 0;
   /*where L is the average number of letters per 100 words in the text, and
    S is the average number of sentences per 100 words in the text.*/

avgletters = numbersofletters*100.0;
avgletters =avgletters/numbersofwords;
avgsentences = (numbersofsentences*100.0)/numbersofwords;
/*printf("avgletters: %f\n", avgletters);
printf("avgsentences: %f\n", avgsentences);*/

float readingindex = (0.0588 * avgletters) - (0.296 * avgsentences) - 15.8;

/*printf("readingindex: %f\n", round(readingindex));*/
int grade = round(readingindex);

if (grade > 16)
{
    printf("Grade 16+\n");
}
else if (grade < 1)
{
  printf("Before Grade 1\n");
}
else
{
    printf("Grade: %i\n", grade);
}

/*printf("readingindex: %f\n", round(readingindex));*/
}





