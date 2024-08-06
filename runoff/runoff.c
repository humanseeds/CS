#include <cs50.h>
#include <stdio.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name); // records voters preferences
void tabulate(void); // counts to votes for all remaining candidates
bool print_winner(void); // determines the winner of the vote
int find_min(void); // find the candidate with the least amount of votes
bool is_tie(int min); // determines if there is a tie between remaining candidates, triggering runoff
void eliminate(int min); // elimnates candidates with the least number of votes

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid, update candidate rank and voter ranking
bool vote(int voter, int rank, string name)
{
    // TODO
    // iterate over the list of candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // compare the candidate list name to the preferences name
        if (strcmp(candidates[i].name, name) == 0)
        {
            // if the candidates name matches the voteres preference name update preferences
            preferences[voter][rank] = i;
            return true;
        }
    }
    // if the voter preferences doesnt match the candidates name return false
    return false;
}

// Tabulate votes for non-eliminated candidates. loop through i + j if not eleminated and add to count
void tabulate(void)
{
    // TODO
    //loop through each voter
    for (int i = 0; i < voter_count; i++)
    {
        // loop through each candidate
        for (int j = 0; j < candidate_count; j++)
        {
            //if the candidate of the voters preference has NOT been elimnated (eleminated = true, not elimnated = false)
            if(candidates[preferences[i][j]].eleminated == false)
            {
                // add a vote to that candidates vote total
                candidates[preferences[i][j]].votes++;
               // break the loop for the voter and go on to the next one
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
    // loop throught each candidate
    for (int i = 0; i < candidate_count; i++)
    {
       // if the candidate has not been eliminated & their votes are greater than half the total votes
        if (!candidates[i].eliminated && candidates[i].votes> voter_count / 2)
        {
            // print the candidates name
            printf("%s/n, candidates[i].name");

            //let program know a winner was found
            return true;
        }
    }
     // continue the program if no winner was found
     return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    // set find_min to the maximum amount of votes
    int find_min = voter_count;
    // loop throught each candidate
    for (i = 0; i < candidate_count; i++)
    {
       // if the candidate has not been eleminated and their votes is less than vote min
        if (!candidates[i].eleminated && candidates[i].votes < find_min)
        {
            find_min = candidates[i].votes;
        }
    }

    return find_min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    //create two ints, one to track if a candidate is eliminated and one to count is votes = min
    int eliminated = 0
    int counter
    // loop through the candidates
    for (int i = 0, i <candidate_count; i ++)
        {
            if (!candidates[i]eliminated)
        }
        }

     return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    // loop throught the candidates
    for ( i = 0; i <candidate_count; i++)
    {
        //if the candidates has the minimum votes they are eleminated
        if (candidates[i].votes == min)
        {
            candidates[i].eleminated == true;
        }
    }
    return;
}
