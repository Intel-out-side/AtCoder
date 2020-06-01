#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  bool isStrong = true;
  int N = S.length();
  for (int i = 0; i < N/2; i++) {
    if (S[i] != S[N-1-i]) isStrong = false;
  }

  string partial = S.substr(0, (N-1)/2);
  int N_par = partial.length();
  for (int i = 0; i < N_par/2; i++) {
    if (partial[i] != partial[N_par-1-i]) isStrong = false;
  }

  string partial2 = S.substr((N+3)/2-1, N);
  int N_par2 = partial2.length();
  for (int i = 0; i < N_par2; i++) {
    if (partial2[i] != partial2[N_par2-1-i]) isStrong = false;
  }

  if (isStrong) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
