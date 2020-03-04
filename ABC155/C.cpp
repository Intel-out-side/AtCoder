#include <bits/stdc++.h>
using namespace std;
using mp = map<string, long long>;

bool sort2(const pair<string, int> &a,
               const pair<string, int> &b)
{
    return (a.second > b.second);
}

int main() {
  long long N;
  cin >> N;
  vector<string> A(N);
  for (long long i = 0; i < N; i++) cin >> A[i];

  map<string, long long> counter;

  for (long long i = 0; i < N; i++) {
    auto it = counter.find(A[i]);
    if (it == counter.end()) {
      counter[A[i]] = 1;
    }
    else {
      counter[A[i]] += 2;
    }
  }

  vector<pair<string, long long>> vec;
  mp:: iterator it2;
  for (it2 = counter.begin(); it2!=counter.end(); it2++) {
    vec.push_back(make_pair(it2->first, it2->second));
  }

  sort(vec.begin(), vec.end(), sort2);

  vector<string> maxs;

  long long maxCount = vec[0].second;
  long long j = 0;
  while (j < vec.size()) {
    if (maxCount == vec[j].second) {
      maxs.push_back(vec[j].first);
    }
    j++;
  }

  sort(maxs.begin(), maxs.end());

  for (long long k = 0; k < maxs.size(); k++) {
    cout << maxs[k] << endl;
  }

  return 0;
}
