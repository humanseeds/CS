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

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
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
    // TODO
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
        if (new_node == NULL)
        {
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
    }
    fclose(file)
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
