#include <stdio.h>
#include <stdlib.h>
long long calc(long long N, long long* X, long long numX) {
  if (0 == N) {
    return 1;
  }
  if (0 < N) {
    long long sol = 0;
    for (long long i = 0; i < numX; i++) {
      if (X[i] <= N) {
        sol += calc(N - X[i], X, numX);
      }
    }
    return sol;
  } else {
    return 0;
  }
}

long long dpcalc(long long N, long long* X, long long numX) {
  long long* dp = malloc((N + 1) * sizeof(long long));

  for (long long i = 0; i < N; i++) {
    dp[i] = 0;
  }
  dp[N] = 1;

  for (long long n = N; n > 0; n--) {
    for (long long i = 0; i < numX; i++) {
      if (0 <= (n - X[i])) {
        dp[n - X[i]] = dp[n - X[i]] + dp[n];
      }
    }
  }
  long long sol = dp[0];
  free(dp);
  return sol;
}

int main() {
  long long N = 3;
  long long X[2] = {1, 2};
  long long numX = 2;

  // printf("Rec: %lld\n", calc(N, X, numX));
  printf("DP: %lld\n", dpcalc(N, X, numX));

  return 0;
}