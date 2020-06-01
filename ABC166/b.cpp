#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N, K;
  cin >> N >> K;

  vector<bool> A(N, false);

  for (int i = 0; i < K; i++) {
    int d;
    cin >> d;
    for (int j = 0; j < d; j++) {
      int A_i;
      cin >> A_i;
      A_i--;
      A[A_i] = true;
    }
  }

  int sum = 0;
  for (bool item : A) {
    if (!item) sum++;
  }

  cout << sum << endl;
  return 0;
}
