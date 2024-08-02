#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
//Prompt user for text
string text = get_string("Input Text: ")

// count the number of words, letter, and sentences in the text
int letters = count_letters(text);
int words = count_words(text);
int sentences = count_sentences(text);

// Compute Coleman-Liau formula
// use round function from math.h
// cast as float so decimals arent truncated.
 index = 0.0588 * L - 0.296 * S - 15.8
l = (#letters / words) / 100
s = (#sentences / words / 100)



// Print Grade Level
 printf("");



int count_letters(string text)
{
    //return number of letters in text  strlen - (isalpha - ispunct)
    int letters = 0;
    for (int i = 0, i < strlen(text); i++)
    {
        if (isalpha((text[i])
        {
            letters++;
        }
    }
}

int count_words(string text)
{
    //retrun number of words in text)  (isalpha - isblank) + 1
    int words = 1
    for (int i = 0, i < strlen(text); i++)
    {
        if (isspace((text[1]))
        {
            words++;
        }
    }

}

int count_sentences(string text)
{
    //count number of sentences in text.   ispunct
    int sentences = 0
    for (int i = 0, i < strlen(text); i++)
    if (text[i] = "." || text[i] = "!" || text[i] = "?")
    {
        sentences++;
    }
}
}
