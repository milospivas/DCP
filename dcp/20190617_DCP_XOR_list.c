// This problem was asked by Google.

// PROBLEM
// An XOR linked list is a more memory efficient doubly linked list.
// Instead of each node holding next and prev fields, it holds a field named
// both, which is an XOR of the next node and the previous node.

// Implement an XOR linked list; \
//     it has an add(element) which adds the element to the end,
// and a get(index) which returns the node at index.

// If using a language that has no pointers(such as Python),
// you can assume you have access to get_pointer and dereference_pointer \
//     functions that converts between nodes and memory addresses.

// SOLUTION

// An XOR linked list
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;
struct Node {
  int val;
  node* both;
};

node* node_construct(int element) {
  node* new_node = malloc(sizeof(node));
  if (new_node != NULL) {
    new_node->val = element;
    new_node->both = NULL;
  } else {
    puts("malloc error at 'node_construct'");
  }
  return new_node;
}

typedef struct XOR_list xor_list;
struct XOR_list {
  int len;
  node* head;
  node* tail;
};

xor_list* xor_list_construct() {
  xor_list* list = malloc(sizeof(xor_list));
  if (list != NULL) {
    list->len = 0;
    list->head = NULL;
    list->tail = NULL;
  } else {
    puts("malloc error at 'xor_list_construct");
  }
  return list;
}

xor_list* xor_list_add(xor_list* l, int element) {
  node* new_node = node_construct(element);

  if (0 == l->len) {
    l->head = new_node;
    l->head->both = NULL;
  } else {
    l->tail->both = (uintptr_t)l->tail->both ^ (uintptr_t)new_node;
    new_node->both = l->tail;
  }
  l->tail = new_node;
  l->len++;
  return l;
}

int xor_list_get(xor_list* l, int index) {
  if (index > l) {
    puts("error. index out of range.");
    return 0;
  }
  node* aux0 = NULL;
  node* aux1 = l->head;
  for (int i = 0; i < index; i++) {
    node* next = (uintptr_t)aux0 ^ (uintptr_t)aux1->both;
    aux0 = aux1;
    aux1 = next;
  }
  return aux1->val;
}

void xor_list_delete(xor_list* l) {
  if (NULL != l) {
    node* aux0 = NULL;
    node* aux1 = l->head;

    for (int i = 0; i < l->len; i++) {
      node* next = (uintptr_t)aux0 ^ (uintptr_t)aux1->both;
      node* old = aux0;
      free(old);
      aux0 = aux1;
      aux1 = next;
    }
    free(aux0);
    free(aux1);
    free(l);
  }
}

int main(void) {
  xor_list* l = xor_list_construct();
  int x = 2, y = 3, z = 4;
  xor_list_add(l, x);
  xor_list_add(l, y);
  xor_list_add(l, z);

  // node* aux0 = NULL;
  // node* aux1 = l->head;
  // node* next;
  // printf("%d\n", aux1->val);
  // next = (uintptr_t)aux0 ^ (uintptr_t)aux1->both;
  // aux0 = aux1;
  // aux1 = next;
  // printf("%d\n", aux1->val);
  // next = (uintptr_t)aux0 ^ (uintptr_t)aux1->both;
  // aux0 = aux1;
  // aux1 = next;
  // printf("%d\n", aux1->val);

  printf("%d\n", xor_list_get(l, 0));
  printf("%d\n", xor_list_get(l, 1));
  printf("%d\n", xor_list_get(l, 2));

  xor_list_delete(l);
  return 0;
}