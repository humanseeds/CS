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
const unsigned int N = 26;

//create a global vriable to track the number of words loaded
unsigned in (word_count) = 0

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
            if (strcascmp(cursor->word, word) == 0)
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
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
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
    while (fscanf(file, %s, input_word) != EOF)
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
    for (int i = 0, i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor->next;
            free(cursor);
            cursor = temp
        }
    }
    return tru;
}
