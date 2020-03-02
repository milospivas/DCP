//  This problem was asked by Google.

//  PROBLEM
//  Implement locking in a binary tree. A binary tree node can be locked or
//  unlocked only if all of its descendants or ancestors are not locked. Design
//  a binary tree node class with the following methods:

//  •	is_locked(), which returns whether the node is locked
//  •	lock(), which attempts to lock the node. If it cannot be locked, then it
//  should return false. Otherwise, it should lock it and return true.
//  •	unlock(), which unlocks the node. If it cannot be unlocked, then it
//  should return false. Otherwise, it should unlock it and return true.

//  You may augment the node to add parent pointers or any other property you
//  would like. You may assume the class is used in a single-threaded program,
//  so there is no need for actual locks or mutexes. Each method should run in
//  O(h), where h is the height of the tree.

//  SOLUTION
//  Augment the Node struct with a parent pointer, is_locked flag, and an int
//  representing the number of locked descendants.
//  The is_locked() function just returns the is_locked flag.
//  The lock() and unlock() functions check the number of locked descendants,
//  and search for a locked ancestor using parent pointers.
//  If the node can be locked/unlocked, is_locked flag is set acordingly as well
//  as number of locked descendants of all the ancestral nodes.
#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"

typedef struct Node Node;
struct Node {
  int val;
  Node *left, *right;
  // augmentations: -----------------------------------------------------------
  Node *parent;
  bool is_locked;
  int num_locked_descendants;
  // --------------------------------------------------------------------------
};

// ----------------------------------------------------------------------------
// helper function that goes through ancestors of the node and checks
// if there is a locked ancestor
bool has_locked_ancestor(Node *node) {
  if (node->parent == NULL) {
    return false;
  } else {
    if (node->parent->is_locked) {
      return true;
    } else {
      return has_locked_ancestor(node->parent);
    }
  }
}

// helper function that updates num_locked_descendants field
// of all ancestors to the node
void update_ancestors(Node *node, int num) {
  if (node) {
    node->num_locked_descendants += num;
    update_ancestors(node->parent, num);
  }
}

// ----------------------------------------------------------------------------
// Iterative versions of helper functions:

// iterative version of has_locked_ancestor
bool has_locked_ancestor_iter(Node *node) {
  while (node->parent != NULL) {
    if (node->parent->is_locked) {
      return true;
    } else {
      node = node->parent;
    }
  }
  return false;
}

// iterative version of update_ancestors
void update_ancestors_iter(Node *node, int num) {
  while (node) {
    node->num_locked_descendants += num;
    node = node->parent;
  }
}

// ----------------------------------------------------------------------------
// checks if node is locked
bool is_locked(Node *node) { return node->is_locked; }

// tries to lock the node
bool lock(Node *node) {
  if (!(has_locked_ancestor_iter(node)) &&
      (node->num_locked_descendants == 0)) {
    node->is_locked = true;
    update_ancestors_iter(node->parent, 1);
    return true;
  } else {
    return false;
  }
}

// tries to unlock the node
bool unlock(Node *node) {
  if (!(has_locked_ancestor_iter(node)) &&
      (node->num_locked_descendants == 0)) {
    node->is_locked = false;
    update_ancestors_iter(node->parent, -1);
    return true;
  } else {
    return false;
  }
}

// ----------------------------------------------------------------------------
// helper function that prints a boolean
void puts_bool(bool flag) { flag ? puts("true") : puts("false"); }

int main() {
  Node *root = &(Node){0, NULL, NULL, NULL, false, 0};
  root->left = &(Node){1, NULL, NULL, root, false, 0};
  root->right = &(Node){2, NULL, NULL, root, false, 0};

  root->left->left = &(Node){3, NULL, NULL, root->left, false, 0};
  root->left->right = &(Node){4, NULL, NULL, root->left, false, 0};

  root->right->left = &(Node){5, NULL, NULL, root->right, false, 0};
  root->right->right = &(Node){6, NULL, NULL, root->right, false, 0};

  Node *l = root->left;
  Node *r = root->right;
  Node *ll = root->left->left;
  Node *lr = root->left->right;
  Node *rl = root->right->left;
  Node *rr = root->right->right;

  puts("locking root:");
  puts_bool(lock(root));

  puts("trying to lock other nodes:");
  puts_bool(lock(l));
  puts_bool(lock(r));
  puts_bool(lock(ll));
  puts_bool(lock(lr));
  puts_bool(lock(rl));
  puts_bool(lock(rr));

  puts("unlocking root:");
  puts_bool(unlock(root));

  puts("trying to lock leaf nodes:");
  puts_bool(lock(ll));
  puts_bool(lock(lr));
  puts_bool(lock(rl));
  puts_bool(lock(rr));

  puts("trying to lock mid level nodes:");
  puts_bool(lock(l));
  puts_bool(lock(r));

  puts("unlocking leaf nodes:");
  puts_bool(unlock(ll));
  puts_bool(unlock(lr));
  puts_bool(unlock(rl));
  puts_bool(unlock(rr));

  puts("trying to lock mid level nodes:");
  puts_bool(lock(l));
  puts_bool(lock(r));

  return 0;
}