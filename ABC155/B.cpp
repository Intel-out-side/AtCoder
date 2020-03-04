#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i=0; i < n; i++) cin >> a[i];

  bool isApproved = true;
  int i = 0;
  while (i < a.size()) {
    if (a[i] % 2 == 0) {
      if (a[i] % 3 != 0 && a[i] % 5 != 0) {
        isApproved = false;
        break;
      }
    }
    i++;
  }

  if (isApproved) {
    cout << "APPROVED" << endl;
  }
  else {
    cout << "DENIED" << endl;
  }

  return 0;
}
