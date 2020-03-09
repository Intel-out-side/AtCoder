#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  long long Q;
  cin >> Q;

  deque<char> dq;

  for (int i = 0; i < s.length(); i++) dq.push_back(s[i]);

  bool isReversed = false;
  for (long long i = 0; i < Q; i++) {
    int Ti, Fi; char Ci;
    cin >> Ti;

    if (Ti == 1) {
      isReversed = !isReversed;
    }
    else if (Ti == 2) {
      cin >> Fi >> Ci;

      //反転されてない
      if (!isReversed) {
        if (Fi == 1) dq.push_front(Ci);
        if (Fi == 2) dq.push_back(Ci);
      }
      else {
        if (Fi == 1) dq.push_back(Ci);
        if (Fi == 2) dq.push_front(Ci);
      }

    }
  }

  if (!isReversed) {
    for (auto item : dq) cout << item;
  }
  else {
    reverse(dq.begin(), dq.end());
    for (auto item : dq) cout << item;
  }
  cout << endl;
  return 0;
}
