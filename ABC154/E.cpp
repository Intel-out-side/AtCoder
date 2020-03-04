#include <bits/stdc++.h>
#define rep(i, n) for (long long i = 0; i < n; i++)
using namespace std;

int main() {
  long long N;
  cin >> N;
  int K;
  cin >> K;
  long long sum = 0;
  if (K == 1) {
    if (N <= 9) sum = N;

    if (N > 9) {
      sum += 9;
      for (long long index = 10; index <= N; index += 10) {
        sum++;
      }
    }
  }
  else if (K == 2) {
    if (N > 9) {
      sum += 9;
      for (long long index = 10; index <= N; index += 100) {
        sum++;
      }
    }
  }
}
