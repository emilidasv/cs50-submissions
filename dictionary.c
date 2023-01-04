// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;
//26 * 26 * 26 = 17576;

// Hash table
node *table[N];

//wordcount
int wordcount = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hashindex = hash(word);
    node *tmpcursor = table[hashindex];

    /*if (tmpcursor != NULL)
    {
        printf("tmpcursor == NULL");
    }
    if (tmpcursor != 0)
    {
        printf("tmpcursor != 0");
    }
    */

    while(tmpcursor != NULL)
    {
        if (strcasecmp(word, tmpcursor->word) == 0)
        {
            return true;
        }
        else
        {
            tmpcursor = tmpcursor->next;
        }
    //printf("row 56%s\n", tmpcursor->word);
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function



    //for each character or beginning of the word load the word into the hash table


    unsigned int ascii_of_char = 0;
    //ascii_of_char = toupper(word[0]) - 65;

    for (int j = 0; j < strlen(word); j++)
    {
        ascii_of_char = ascii_of_char + tolower(word[j]);
    }
    return ascii_of_char % N;
    /*int tmplen = strlen(word) - 1;
    if (tmplen >= 3)
    {
        ascii_of_char = (toupper(word[0]) + toupper(word[1]) + toupper(word[2]) ) - 3 * 65;
    }
    else if (2 == tmplen)
    {
        ascii_of_char = (toupper(word[0]) + toupper(word[1]) ) - 2 * 65;
    }
    else if (1 == tmplen)
    {
         ascii_of_char = toupper(word[0]) - 65;
    }
    else
    //tmplen = 0, something is wrong
    {
        ascii_of_char = -1;
    };*/

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    //initiate the table to only be null
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // first open up the dictonary file and read first word
    //open file
    // debug printf("dict %s\n", dictionary);

    FILE *dictptr = fopen(dictionary, "r");
    if (dictptr == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    //read first line in the dictionary text file

    char tmpline[LENGTH + 1];
    node *newnode;
    //fgets reads one line unitl \n
    while (fscanf(dictptr, "%s", tmpline) != EOF)
    {
        //allocate memeroy for new node
        newnode = malloc(sizeof(node));
        if(newnode == NULL)
            {
                return false;
            }

        strcpy(newnode->word, tmpline);
        unsigned int hashindex =hash(tmpline);

        newnode->next = table[hashindex];
        table[hashindex] = newnode;
        wordcount++;
        //free(newnode);
        //printf("row143:%s\n", newnode->word);

    }


    fclose(dictptr);


    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wordcount;

}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int memoryfreed = 0;
    for (int i = 0 ; i < N; i++)

    {
        node *tmpcursor = table[i];
        while (tmpcursor )
        {
            node *tmp = tmpcursor;

            tmpcursor = tmpcursor->next;
            free(tmp);
            memoryfreed++;
            // debug printf("memoryfreed; %i\n", memoryfreed);
        }



    }
    return true;
}

