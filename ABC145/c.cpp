#include <bits/stdc++.h>
using namespace std;

template <typename T> vector<vector<T>> permutation(vector<T> v) {
  vector<vector<T>> perms;
  do {
    perms.push_back(v);
  } while (next_permutation(v.begin(), v.end()));

  return perms;
}

void vprint(vector<int> v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i];
  }
  cout << endl;
}

int main() {
  int N;
  cin >> N;
  vector<pair<int, int>> x_y(N);

  for (int i = 0; i < N; i++) {
    int x, y;
    cin >> x >> y;
    x_y[i] = make_pair(x, y);
  }

  vector<int> pairs(N);
  for (int i = 0; i < N; i++) pairs[i] = i+1;

  vector<vector<int>> perm = permutation(pairs);

  double sum_dist = 0;
  for (int i = 0; i < perm.size(); i++) {
    for (int j = 0; j < N - 1; j++) {
      int index = perm[i][j] - 1;
      int index_ = perm[i][j+1] - 1;
      sum_dist += sqrt((x_y[index].first - x_y[index_].first)*(x_y[index].first - x_y[index_].first) + (x_y[index].second - x_y[index_].second)*(x_y[index].second - x_y[index_].second));
    }
  }

  double ave = sum_dist / perm.size();
    //cout << fixed << setprecision(6)とすれば10^-6までの精度で出力できる
  cout << fixed << setprecision(7);
  cout << ave << endl;
  return 0;
}
