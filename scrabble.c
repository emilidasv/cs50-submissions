#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
/*string charstring[] = {"a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};*/
string charstring ="abcdefghihjklmnopqrstuvwxyz";

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }


}

int compute_score(string word)
{
    // TODO: Compute and return score for string

    string tmpstring = word;
    int len = strlen(word);
    int sumOfPoinst = 0;
    int numberoflettersinalpa = strlen(charstring);

    for (int i = 0, n = strlen(word); i < n; i++)
/*make sure all are lower case*/
    {
        tmpstring[i] = tolower(word[i]);
    }

    for (int j = 0; j < len; j++)
    {
        for (int k = 0; k < numberoflettersinalpa; k++)
        {
            int tmpstringscii = tmpstring[j];
            int tmpcharstringascci = charstring[k];
            if (tmpstring[j] == charstring[k])
            {
                sumOfPoinst = sumOfPoinst + POINTS[k];
            }
        }

    }



        return sumOfPoinst;
}
