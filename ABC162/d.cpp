#include <bits/stdc++.h>
using namespace std;
using ll = long long;

//idk
int main() {
  int N;
  cin >> N;
  string S;
  cin >> S;

  int sum = 0;
  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
      if (S[i] == S[j]) continue;
      for (int k = j + 1; k < N; k++) {
        if (S[j] == S[k]) continue;
        if (j - i == k - j) continue;
        if (S[i] != S[j] && S[j] != S[k] && S[k] != S[i]) sum++;
      }
    }
  }

  cout << sum << endl;
  return 0;
}
