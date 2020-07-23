// # This problem was asked by Quora.
// # # PROBLEM
// # Given a string, find the palindrome that can be made by inserting
// # the fewest number of characters as possible anywhere in the word.
// # If there is more than one palindrome of minimum length that can be made,
// # return the lexicographically earliest one (the first one alphabetically).
// #
// # For example, given the string "race", you should return "ecarace",
// # since we can add three letters to it (which is the smallest amount
// # to make a palindrome). There are seven other palindromes that can be made
// # from "race" by adding three letters, but "ecarace" comes first
// alphabetically.
// #
// # As another example, given the string "google", you should return
// "elgoogle".
// #
// # # SOLUTION
// # DP

// this is C so we first need to build the tools for handling strings

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef struct String String;
struct String {
  int len;
  char *str;
};

// appends a character as a prefix and suffix
String *append_left_and_right(String *s, char c) {
  String *s_new = malloc(sizeof(String));
  // +2 for the new characters
  s_new->len = s->len + 2;
  //                                 + 1 for the null terminator
  s_new->str = malloc(sizeof(char) * (s_new->len + 1));

  s_new->str[0] = c;
  strcpy(s_new->str + 1, s->str);
  s_new->str[s_new->len - 1] = c;  // this overwrites the null terminator
  s_new->str[s_new->len] = '\0';   // so we add it at the end

  return s_new;
}

int cmp_strings(String *s1, String *s2) {
  int n1 = s1->len;
  int n2 = s2->len;

  if (n1 < n2) {
    return -1;
  }
  if (n1 > n2) {
    return 1;
  }

  if (n1 == n2) {
    for (int i = 0; i < n1; i++) {
      if (s1->str[i] < s2->str[i]) {
        return -1;
      }
    }
  }
  return 1;
}

void print_d(String ***ptr, int n) {
  String(*d)[n][n] = ptr;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      (*d)[i][j].str != NULL ? printf("%10s_", (*d)[i][j].str) : printf("_ ");
    }
    puts("");
  }
}

char *nearest_string(char *s) {
  int n = strlen(s);
  char *sol;

  String d[n][n];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      d[i][j].len = 0;
      d[i][j].str = malloc(sizeof(char));
      d[i][j].str[0] = '\0';
    }
  }

  for (int i = 0; i < n; i++) {
    // d[i][i] = malloc(sizeof(String));
    if (d[i][i].str != NULL) free(d[i][i].str);
    d[i][i].str = malloc(sizeof(char) * 2);
    d[i][i].str[0] = s[i];
    d[i][i].str[1] = '\0';
    d[i][i].len = 1;
  }

  // print_d(&d, n);
  for (int i = 1; i < n; i++) {
    for (int j = i; j < n; j++) {
      int l = j - i;
      int r = j;

      if (s[l] == s[r]) {
        String *aux = append_left_and_right(&d[l + 1][r - 1], s[l]);
        d[l][r].len = aux->len;
        d[l][r].str = aux->str;
      } else {
        String *s1 = append_left_and_right(&d[l + 1][r], s[l]);
        String *s2 = append_left_and_right(&d[l][r - 1], s[r]);
        if (cmp_strings(s1, s2) == -1) {
          d[l][r].len = s1->len;
          d[l][r].str = s1->str;
          free(s2->str);
        } else {
          d[l][r].len = s2->len;
          d[l][r].str = s2->str;
          free(s1->str);
        }
        free(s1);
        free(s2);
      }
      // print_d(&d, n);
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if ((i == 0) && (j == n - 1)) {
        sol = d[i][j].str;
        continue;
      } else {
        free(d[i][j].str);
      }
    }
  }

  return sol;
}

int main() {
  char *s = (char *)&(char[]){"google"};
  // char *s = "google";
  // printf("%s\n", s + 1);
  // char c = s[1];
  // printf("%c\n", c);
  char *sol = nearest_string(s);
  puts(sol);
  free(sol);
  return 0;
}