#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool check_pal(char *word);

int main() {
    char *text = malloc(5 * sizeof(char));
    printf("Enter word : ");
    scanf("%s", text);
    char *answer = check_pal(text) == true ? "Is a palindrome" : "Is not a palindrome";
    printf("\n%s\n", answer);

    return 0;
}

bool check_pal(char *word) {
    //reverse word
    char *rev_word = malloc((sizeof(word) - 1) * sizeof(char));
    for (int i = 0, j = strlen(word)-1; i < (int)strlen(word) && j >= 0; i++, j--) {
        *(rev_word + i) = *(word + j);
    }

    //compare word and it reverse
    bool result = strcmp(word, rev_word) == 0 ? true : false;
    return result;

    free(rev_word);
}