// # This problem was asked by Jane Street.
// # # PROBLEM
// # Suppose you are given a table of currency exchange rates, represented as a
// 2D array. # Determine whether there is a possible arbitrage: that is, whether
// there is some sequence # of trades you can make, starting with some amount A
// of any currency, so that you can end up # with some amount greater than A of
// that currency. # There are no transaction costs and you can trade fractional
// quantities.
// #
// # # SOLUTION
// # kind of looks like a graph search
// #
// # Ok, this can totally be done via graph search.
// # with currencies being nodes in the graph
// # and exchange rates being weights of the edges
// # but instead of path length being the sum of the edge weights
// # the path length is the PRODUCT of the edge weights.
// # And the problem we are essentially solving is:
// # All Pairs Shortest Paths, or in this case, longest paths.
// # And that can be done with a simple modification to Floyd's algorithm.
//

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"

void** malloc_2d_array(size_t size, size_t num_rows, size_t num_cols) {
  void** arr = malloc(sizeof(void*) * num_rows);
  for (size_t i = 0; i < num_rows; i++) {
    arr[i] = malloc(size * num_cols);
  }
  return arr;
}

void free_2d_array(void** arr, size_t num_rows) {
  if (arr == NULL) {
    return;
  }
  for (size_t i = 0; i < num_rows; i++) {
    free(arr[i]);
  }
  free(arr);
}

bool floyd_product(double** w, int n) {
  int i, j, k;
  // TODO remove
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      printf("%2.2f ", w[i][j]);
    }
    puts("");
  }
  puts("");

  double** d = malloc_2d_array(sizeof(double), n, n);

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      d[i][j] = w[i][j];
    }
    // hygienic, because 1 is a neutral element for multiplication
    d[i][i] = 1;
  }

  for (k = 0; k < n; k++) {
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        if (d[i][j] < d[i][k] * d[k][j]) {
          d[i][j] = d[i][k] * d[k][j];
        }
      }
    }
  }

  // TODO remove
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      printf("%2.2f ", d[i][j]);
    }
    puts("");
  }
  puts("");

  bool sol = false;
  for (k = 0; k < n; k++) {
    if (d[k][k] > 1) {
      sol = true;
      break;
    }
  }

  free_2d_array(d, n);
  return sol;
}

void puts_bool(bool flag) { flag ? puts("True") : puts("False"); }
int main() {
  int i, j, n = 3;
  double** w = (double* []){(double[]){1, 0.5, 1},
                            (double[]){1.9, 1, 1},
                            (double[]){2, 1, 1}};

  puts_bool(floyd_product(w, n));
  return 0;
}