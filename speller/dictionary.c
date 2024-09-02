// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <dictionary.h>
#include <string.h>


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 5381;

//create a global vriable to track the number of words loaded
unsigned int word_count = 0

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // use the right index in the hash table for the word
    int index = hash(word);

    //create a pointer to traverse the liniked list
    node *cursor = table[index];

    //traverse the linked list as long as the word is not found
    while (cursor != NULL)
        {

            //case insensitive comparison of the word in the node vs the searched word
            if (strcasecmp(cursor->word, word) == 0)
            {
               //if the word is found, return true
                return true;
            }

            //move the cursor to the next node
            cursor = cursor->next;
        }

    // if the word is not found return false
    return false;
}

// Hashes word to a number
//at 7:35 in the hash tables short video Doug Loyd sayd to not write our own hashfunction
// instead find a hash function online and give credit to the athor.
//the DJB2 hash function is from Daniel J. Bernstein
unsigned int hash(const char *word)
{
    //initialize the hash to a large prime number
    unsigned long hash = 5381;

    //create a variable to store each character of the string'word'
    int c;

    //loop through the string, assign the value of each char to c, and increment to the next char in the string
    while ((c = *word++))
    {

        //convert to lowercase to be case insensitive
        c = tolower(c);

        //hash = hash * 32 + c. the << operator shifts the bits by 5 positions (each bit shift
        //multiples by 2, a 5 position shift is 2^5 or 32)
        hash = ((hash << 5) + hash) + c;
    }
    // return the value of the hashed value modulated by the number of buckets
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open the dictionary file, print error if unable
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Unable to open %s\n", dictionary);
    return false;
    }

    // create a temp variable to hold each word from file
    char input_word[LENGTH +1];

    //read strings from the file
    while (fscanf(file, "%s", input_word) != EOF)
    {
        // create a new node for each word
        node *new_node = malloc(sizeof(node));

        //if the memory cannot be allocated, close the file, and free memory leaks
        if (new_node == NULL)
        {
            fclose(file);
            unload();
            return false;
        }
        // copy the word into the node
    strcpy(new_node->word, input_word);

    //hash word to obtain a hash value
    int index = hash(input_word);

    // insert the new node into the hash function.
    new_node->next = table[index];
    table[index] = new_node;

     //increment the word count
    word_count++;
    }

    //close the dictionary source file
    fclose(file);

    //return true if the function was successful
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //iterate over each bucket of the hash table
    for (int i = 0; i < N; i++)
    {
        //set a pointer to the head of the list
        node *cursor = table[i];

        // run a loop while the pointer is not at tthe end of the linked list
        while (cursor != NULL)
        {
            // create a temporary cursor set to the next node in the list
            node *temp = cursor->next;

            // free the memory for the node at the current pointer
            free(cursor);

            // move the pointer to the next node that the temp pointer is addressing
            cursor = temp;
        }
    }
   //return true to indicate the memory is properly free
    return true;
}
