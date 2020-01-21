#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  int N;
  string S, T;
  string newString = "";
  cin >> N;
  cin >> S >> T;

  for (int i = 0; i < N; i++) {
    newString += S[i];
    newString += T[i];
  }

  cout << newString << endl;
  return 0;
}
