//  This problem was asked by Facebook.
//  # PROBLEM
//  Given a string of round, curly, and square open and closing brackets, return
//  whether the brackets are balanced (well-formed).
//  For example, given the string "([])[]({})", you should return true.
//  Given the string "([)]" or "((()", you should return false.
//
//  # SOLUTION
//  Use a stack
//  go through the characters of the string
//    if it's an open bracket -> push it on the stack
//    else pop the stack until the matching closing bracket is poped
//      if the stack is empty and the matching closing bracket isn't found:
//        return False
//    if at the end of the string the stack ISN'T empty:
//      retrun False
//    else:
//      return True

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"

typedef struct Node Node;
struct Node {
  char val;
  Node* prev;
};

typedef struct Stack Stack;
struct Stack {
  Node* top;
};

void init(Stack* s) { s->top = NULL; }

void push(Stack* s, char val) {
  Node* aux = malloc(sizeof(Node));
  aux->val = val;
  aux->prev = s->top;
  s->top = aux;
}

char pop(Stack* s) {
  if (!s->top) {
    return 0;
  }
  char val = s->top->val;
  Node* old = s->top;
  s->top = s->top->prev;
  free(old);
  return val;
}

void free_stack(Stack* s) {
  while (s->top) {
    Node* old = s->top;
    s->top = s->top->prev;
    free(old);
  }
}

bool is_regular(char* s) {
  Stack* stack = &(Stack){NULL};
  for (int i = 0; s[i] != '\0'; i++) {
    // if current char is an open bracket
    if ((s[i] == '(') || (s[i] == '[') || (s[i] == '{')) {
      push(stack, s[i]);
    }
    // if current char is a closed bracket
    else {
      bool stop_flag = false;
      while (!stop_flag) {
        if (stack->top == NULL) {
          return false;
        }
        char x = pop(stack);
        if (((x == '(') && (s[i] == ')')) || ((x == '[') && (s[i] == ']')) ||
            ((x == '{') && (s[i] == '}'))) {
          stop_flag = true;
        }
      }
    }
  }
  if (stack->top != NULL) {
    free_stack(stack);
    return false;
  }
  return true;
}

void puts_bool(bool flag) { flag ? puts("true") : puts("false"); }
void test(char* s) {
  puts(s);
  puts_bool(is_regular(s));
}

int main() {
  char* s;
  s = "()";
  test(s);
  s = "[]";
  test(s);
  s = "{}";
  test(s);
  s = "[(])";
  test(s);
  s = "[()]";
  test(s);
  s = "{[()][()][{([])}]}";
  test(s);
  s = "((()";
  test(s);

  return 0;
}