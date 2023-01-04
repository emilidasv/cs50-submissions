#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int num;
    struct node *next;
}
node;

int main(void)
{
node *table[2];

int myAge = 43;     // Variable declaration
int* ptr = &myAge;  // Pointer declaration
                    // A pointer variable, with the name ptr, that stores the address of myAge


// Output the value of myAge (43)
printf("%d\n", myAge);

// Dereference: Output the value of myAge with the pointer (43)
printf("%d\n", *ptr);

// Output the memory address of myAge (0x7ffe5367e044)
printf("%p\n", &myAge);

// Output the memory address of myAge with the pointer (0x7ffe5367e044)
printf("%p\n", ptr);

// Reference: Output the memory address of myAge with the pointer (0x7ffe5367e044)
printf("%p\n", ptr);

node *newnode = malloc(sizeof(node));
printf("%p\n", newnode);  //mempery adress of new node
printf("%i\n", newnode->num);  //mempery adress of new node

newnode->num = 1;
printf("%i\n", newnode->num);  //mempery adress of new node
table[0]= newnode;
printf("%i\n", table[0]->num);
node *newnode2 = malloc(sizeof(node));
newnode2->num = 2;
newnode2->next = table[0];
printf("%i\n", table[0]->num);
table[0]=newnode2;
printf("%i\n", table[0]->num);
printf("%i\n", newnode2->num);






}