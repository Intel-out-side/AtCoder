#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

P headsTail(int x) {
  int tail = x % 10;
  int heads = tail;
  while ((x / 10) != 0) {
    x /= 10;
  }
  heads = x;
  P ans(heads, tail);
  return ans;
}

int main() {
  int N;
  cin >> N;
  ll sum = 0;
  map<P, int> freq;
  for (int i = 1; i <= N; i++) {
    P p = headsTail(i);
    // 整数iにおいてのpair = {heads, tail}
    freq[p]++;
    // 例えば(1, 9)みたいなペアがあったら，その集計を1増やす
    // 存在しないキー値にアクセスすると勝手にゼロ値を代入してくれる
  }

  for (int i = 1; i<= N; i++){
    P p = headsTail(i);
    P q(p.second, p.first);
    sum += freq[q];
  }
  cout << sum << endl;
  return 0;
}
