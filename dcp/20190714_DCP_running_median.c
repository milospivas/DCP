// This problem was asked by Microsoft.
// # PROBLEM
// Compute the running median of a sequence of numbers. That is, given a stream
// of numbers, print out the median of the list so far on each new element.
// Recall that the median of an even-numbered list is the average of the two
// middle numbers. For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your
// algorithm should print out:
// 2
// 1.5
// 2
// 3.5
// 2
// 2
// 2
// # SOLUTION
// Have a max-heap and a min-heap.
// Iterate through the list.
// Keep a middle element, and smaller elements in the max-heap, and bigger
// elements in the min-heap, so that the heaps are the same sizes or at 1
// difference at most. The running median is either the middle element, if the
// heaps are the same size, Or the average of the middle and root.val of the
// bigger heap.

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"

typedef struct heap heap;
struct heap {
  int *a;
  int n;
  int size;
  bool is_max_heap;
};

heap *heap_construct(int size, bool is_max_heap) {
  heap *aux = malloc(sizeof(heap));
  if (!aux) {
    puts("DMAError. Malloc failed.");
    return NULL;
  }
  heap *h = aux;
  aux = malloc(sizeof(int) * size);
  if (!aux) {
    puts("DMAError. Malloc failed.");
    return NULL;
  }
  h->a = aux;
  h->n = 0;
  h->size = size;
  h->is_max_heap = is_max_heap;
  return h;
}

heap *heap_destruct(heap *h) {
  if (!h) {
    return NULL;
  }
  if (h->a) {
    free(h->a);
  }
  free(h);
  return NULL;
}

void swap(int *a, int i, int j) {
  if (!a) {
    puts("Error. Array pointer is null.");
  }
  int x = a[i];
  a[i] = a[j];
  a[j] = x;
}

int cmp_max(int *a, int i, int j) {
  if (!a) {
    puts("Error. Array pointer is null.");
    return -2;
  }
  if (a[i] < a[j]) {
    return -1;
  }
  if (a[i] == a[j]) {
    return 0;
  }
  if (a[i] > a[j]) {
    return 1;
  }
}

int cmp_min(int *a, int i, int j) {
  if (!a) {
    puts("Error. Array pointer is null.");
    return -2;
  }
  if (a[i] < a[j]) {
    return 1;
  }
  if (a[i] == a[j]) {
    return 0;
  }
  if (a[i] > a[j]) {
    return -1;
  }
}

void sift_down(int *a, int n, int idx, bool is_max_heap) {
  if (!a) {
    puts("Error. Array pointer is null.");
    return;
  }
  if (n <= 0) {
    puts("SizeError. Can't sift empty heap.");
    return;
  }
  if ((idx < 0) || (idx >= n)) {
    puts("IndexError. Index out of range.");
    return;
  }
  int (*cmp)(int *, int, int);
  if (is_max_heap) {
    cmp = &cmp_max;
  } else {
    cmp = &cmp_min;
  }

  while (2 * idx + 1 < n) {
    int left = 2 * idx + 1;
    int right = left + 1;

    int largest = idx;
    if ((left < n) && ((*cmp)(a, left, largest) == 1)) {
      largest = left;
    }
    if ((right < n) && ((*cmp)(a, right, largest) == 1)) {
      largest = right;
    }

    if (idx != largest) {
      swap(a, idx, largest);
      idx = largest;
    } else {
      break;
    }
  }
}

void sift_up(int *a, int n, int idx, bool is_max_heap) {
  if (!a) {
    puts("Error. Array pointer is null.");
    return;
  }
  if (n <= 0) {
    puts("SizeError. Can't sift empty heap.");
    return;
  }
  if ((idx < 0) || (idx >= n)) {
    puts("IndexError. Index out of range.");
    return;
  }

  int (*cmp)(int *, int, int);
  if (is_max_heap) {
    cmp = &cmp_max;
  } else {
    cmp = &cmp_min;
  }

  while (idx / 2 >= 0) {
    int parent = idx / 2;

    if ((parent >= 0) && ((*cmp)(a, idx, parent) == 1)) {
      swap(a, idx, parent);
      idx = parent;
    } else {
      break;
    }
  }
}

// insert into heap
heap *heap_insert(heap *h, int val) {
  if (h->n == h->size) {
    int new_size = 2 * h->size;
    int *aux = realloc(h->a, sizeof(int) * new_size);
    if (!aux) {
      puts("DMAError. Expanding realloc failed.");
      puts("Couldn't insert into heap.");
      return NULL;
    } else {
      h->a = aux;
      h->size = new_size;
    }
  }
  h->a[h->n] = val;
  sift_up(h->a, h->n + 1, h->n, h->is_max_heap);
  h->n++;
  return h;
}
// extract
int heap_extract(heap *h) {
  if (h->n <= 0) {
    puts("SizeError. Cannot extract from empty heap.");
    return 0;
  }

  int val = h->a[0];
  swap(h->a, 0, h->n - 1);
  h->n--;
  if (h->n > 1) {
    sift_down(h->a, h->n, 0, h->is_max_heap);
  }

  if (h->n < h->size / 2) {
    int new_size = h->size / 2;
    int *aux = realloc(h->a, sizeof(int) * new_size);
    if (!aux) {
      puts("DMAError. Contracting realloc failed.");
      puts("Memory remains bigger than needed.");
    } else {
      h->a = aux;
      h->size = new_size;
    }
  }
  return val;
}

void heap_print(heap *h) {
  if (!h->a) {
    puts("Error. Heap array is NULL.");
    return;
  }
  for (int i = 0; i < h->n; i++) {
    printf("%d ", h->a[i]);
  }
  puts("");
}

double *running_medians(int *stream, int n) {
  double *medians = malloc(sizeof(double) * n);
  if (!medians) {
    puts("DMAError. malloc failed.");
    return NULL;
  }

  int middle = stream[0];
  medians[0] = (double)middle;
  heap *h_max = heap_construct(n / 2 + 1, true);
  heap *h_min = heap_construct(n / 2 + 1, false);

  for (int i = 1; i < n; i++) {
    int x = stream[i];

    if (x <= middle) {
      heap_insert(h_max, x);
    } else {
      heap_insert(h_min, x);
    }

    if (h_max->n - h_min->n == 2) {
      heap_insert(h_min, middle);
      middle = heap_extract(h_max);
    }
    if (h_max->n - h_min->n == -2) {
      heap_insert(h_max, middle);
      middle = heap_extract(h_min);
    }

    switch (h_max->n - h_min->n) {
      case 1:
        medians[i] = (double)(h_max->a[0] + middle) / 2.0;
        break;
      case 0:
        medians[i] = (double)middle;
        break;
      case -1:
        medians[i] = (double)(middle + h_min->a[0]) / 2.0;
        break;

      default:
        puts("Error. Something bad happened.");
        break;
    }
  }
  heap_destruct(h_max);
  heap_destruct(h_min);
  return medians;
}

int main() {
  int n1 = 10;
  int n2 = 12;
  int stream1[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int stream2[12] = {5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4};

  double *medians1 = running_medians(&stream1, n1);  // includes malloc
  double *medians2 = running_medians(&stream2, n2);  // includes malloc

  puts("Output:");
  for (int i = 0; i < n1; i++) printf("%2.2f\n", medians1[i]);
  puts("");
  puts("");
  for (int i = 0; i < n2; i++) printf("%2.2f\n", medians2[i]);
  puts("");

  free(medians1);
  free(medians2);
  return 0;
}