#include <bits/stdc++.h>
using namespace std;
using ll = long long;

//Sieveを使うとTLEする(O(NloglogN))場合があるのでこっちを使うとよい。
//素因数分解して各因数が何乗されているかを返す
/*
  実行時間：O(√n)
  @param n: ｘを素因数分解する関数
  @return : 1を含まない素因数の集合(e.g. 12 -> (2,2), (3,1))
*/
vector<pair<ll, ll>> factorize(ll n) {
  vector<pair<ll, ll>> res;
  //√n までを見れば良いので終了条件がi^2<=nになる
  for (ll i = 2; i * i <= n; i++) {
    if (n%i != 0) continue;
    res.emplace_back(i, 0);//res.push_back(make_pair(i, 0));と同等
    while (n % i == 0) {
      n /= i;
      res.back().second++;
    }
  }
  //最初のn自体が
  if (n != 1) res.emplace_back(n, 1);
  return res;
}

int main() {

}
