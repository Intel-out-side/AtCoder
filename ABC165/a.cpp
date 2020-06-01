#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {

  int K, A, B;
  cin >> K >> A >> B;

  int i = A;
  bool result = false;
  while (true) {
    if (i % K == 0) {
      result = true;
      break;
    }
    if (i == B) break;

    i++;
  }

  if (result) cout << "OK" << endl;
  else cout << "NG" << endl;
  return 0;
}
