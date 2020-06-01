#include <bits/stdc++.h>
using namespace std;

int main() {
  int M, N;
  cin >> N >> M;
  vector<int> A(N);
  long long votes = 0;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
    votes += A[i];
  }

  int selected = 0;
  for (int i = 0; i < N; i++) {
    if (A[i] * 4 * M >= votes) selected++;
  }

  if (selected >= M) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
