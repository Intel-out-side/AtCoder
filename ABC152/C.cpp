#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); i++)
using namespace std;
typedef long long li;

int main() {
  int N;
  int sum = 0;
  cin >> N;
  vector<int> p(N);
  rep(i, N) { cin >> p[i]; }

  tmpMin = 1e9;

  rep(i, N) {
    if (tmpMin > p[i]) {
      tmpMin = p[i];
    }

    if (tmpMin == p[i]) {
      sum += 1;
    }
  }

  cout << sum << endl;
  return 0;
}

/*
全探索するとO(N^2)になって間に合わないので，O(N)で行けるような
解法を探すことが大切
*/
