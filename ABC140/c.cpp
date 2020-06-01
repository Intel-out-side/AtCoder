#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> B(N);
  for (int i = 1; i < N; i++) cin >> B[i];
  vector<int> A(N+1);

  A[1] = A[2] = B[1];
  for (int i = 2; i <= N-1; i++) {
    if (A[i] > B[i]) A[i] = B[i];
    A[i+1] = B[i];
  }

  long long sum = 0;
  for (int i = 1; i <= N; i++) sum += A[i];
  cout << sum << endl;
  return 0;
}
