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
    int hashindex = -1;

    hashindex = hash(word);
    for(node *tmpcursor = table[hashindex]; tmpcursor != NULL; tmpcursor = tmpcursor->next)

    {
        if (strcasecmp(word, tmpcursor->word) == 0)
        {
            return true;
        }
        printf("word:%s", word);
        printf("%lu\n", strlen(word));
        printf("tmpcursor->word:%s", tmpcursor->word);
        printf("%lu\n", strlen(word));
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    int tmplen = strlen(word) - 1;

    //for each character or beginning of the word load the word into the hash table

    int ascii_of_char = 0;

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
    };

    return ascii_of_char;
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

    //fgets reads one line unitl \n
    while (fgets(tmpline, sizeof(tmpline), dictptr))
    {

        //length f word tmpline
        int tmplen = strlen(tmpline);
        int hashindex = -1;
        if (tmplen == 1)
        {
            // this means the word is empty
            return false;

        }
        else
        {
            hashindex = hash(tmpline);
            //debug printf("HAshindex%i\n", hashindex);
            // debug printf("tmpline:%s\n", tmpline);

            // allocate memory for a node for a new word

            node  *newnode = malloc(sizeof(node));

            if(newnode == NULL)
            {
                return false;
            }

            newnode->next = table[hashindex];;
            strcpy(newnode->word, tmpline);

            //debug    printf("memory adress of n %p\n", newnode);
            //debug    printf("memory adress table[hashindex] %p\n", table[hashindex]);
            //printf("*n->word%s\n", newnode->word);
            //debug    printf("*n->next%p\n", newnode->next);


            //debug   printf("*n->word%s\n", newnode->word);
            //debug   printf("*n->next%p\n", newnode->next);
            //debug   printf("*table[hashindex]->word%s\n", table[hashindex]->word);

            //debug  printf("memory adress of n %p\n", newnode);
            //debug  printf("memory adress table[hashindex] %p\n", table[hashindex]);

            table[hashindex] = newnode;
            free(newnode);
            wordcount++;


        }

        //printf("\n");


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
    for (int i = 0 ; i < N; i++)

    {
        node *tmpcursor = table[i];
        while (tmpcursor != NULL)
        {
            node *tmp = tmpcursor;

            tmpcursor = tmpcursor->next;
            free(tmp);
        }
        return true;

    }
return false;
}

