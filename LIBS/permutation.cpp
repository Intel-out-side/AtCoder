#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
using ll = long long;

template <typename T> vector<vector<T>> permutation(vector<T> v) {
  vector<vector<T>> perms;
  do {
    perms.push_back(v);
  } while (next_permutation(v.begin(), v.end()));

  return perms;
}

void vprint(vector<ll> v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i];
  }
  cout << endl;
}

int main() {
  vector<ll> v = {4, 2, 1, 5};
  sort(v.begin(), v.end());

  vector<vector<ll>> result = permutation(v);
  for (int i = 0; i < result.size(); i++) {
    vprint(result[i]);
  }
}
