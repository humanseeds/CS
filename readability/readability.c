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
s = (#sentences / words0 / 100)



// Print Grade Level
 printf(")

}

int count_letters(string text)
{
    //return number of letters in text  isalpha
}

int count_words(string text)
{
    //retrun number of words in text)  isblank
}

int count_sentences(string text)
{
    //count number of sentences in text.   ispunct
}
