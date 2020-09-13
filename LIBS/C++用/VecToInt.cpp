#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
using namespace std;
using ll = long long;

//should give vector<integer type>
template <typename T> T VecToInt(vector<T> v) {
  T result = 0, base = 1;
  while (v.size() != 0) {
    result += v[v.size()-1] * base;
    base *= 10;
    v.pop_back();
  }

  return result;
}
