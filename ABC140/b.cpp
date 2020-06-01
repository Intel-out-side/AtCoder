#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  vector<int> A(N+1), B(N+1), C(N);
  for (int i = 1; i <= N; i++) cin >> A[i];
  for (int i = 1; i <= N; i++) cin >> B[i];
  for (int i = 1; i <= N-1; i++) cin >> C[i];

  int sum = 0;
  for (int i = 1; i <= N; i++) {
    sum += B[A[i]];
    if (i > 1) {
      if (A[i] == A[i-1]+1) sum += C[A[i-1]];
    }
    cout << sum << " ";
  }
  cout << endl;

  cout << sum << endl;
  return 0;
}
