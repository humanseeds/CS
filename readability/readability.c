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
    string text = get_string("Input Text: ");

// count the number of words, letter, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

// Compute Coleman-Liau formula
// use round function from math.h
// cast as float so decimals arent truncated.
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade_level = round(index);
// Print Grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
         printf("Grade 16+\n");
    }
else
    {
        printf("Grade %i\n", grade_level);
    }
}


int count_letters(string text)
{
    //return number of letters in text  strlen - (isalpha - ispunct)
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    //retrun number of words in text)  (isalpha - isblank) + 1
    int words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[1]))
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    //count number of sentences in text.   ispunct
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    if (text[i] == "." || text[i] == "!" || text[i] == "?")
    {
        sentences++;
    }
}
    return sentences;
}
