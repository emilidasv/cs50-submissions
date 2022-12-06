#include <stdio.h>
/* needed to be able to use get_string function */
#include <cs50.h>

int main(void)
{
/* Ask for the users name*
"?\n means new line/
    string name = get_string("Hello. What  is your name?\n");


/* Say hello to user  %s is place holder for string name*/
    printf("Hello %s\n", name);
}

