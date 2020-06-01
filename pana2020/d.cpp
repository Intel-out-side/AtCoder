#include <bits/stdc++.h>
using namespace std;

bool isSameType(string a, string b) {
  if (a.length() != b.length()) return false;

  bool res = true;
  for (int i = 0; i < a.length(); i++) {
    for (int j = i+1; j < a.length(); j++) {
      //res = res && (!(a[i] == a[j] && b[i] == b[j]) != !(a[i] != a[j] && b[i]!=b[j]));
      if (a[i] == a[j] && b[i] != b[j]) res = false;
      if (a[i] != a[j] && b[i] == b[j]) res = false;
      if ((a[i] == a[j] && b[i] == b[j]) && a[i] != a[j] && b[i] != b[j]) res = false;
    }
  }

  return res;
}

string all_str()

int main() {
  int N;
  cin >> N;

  vector<string> ans;
  string s = "";
  for (int i = 0; i < N; i++) s = s + "a";
  ans.push_back(s);
  all.push_back()

  //cout << isSameType("aa", "bb") << endl;

  vector<string> all;
  int i = N-1;
  while (i >= 0) {
    while (s[i] != 'z') {
      s[i]++;
      all.push_back(s);
    }
    for (int j = N-1; j < )

    i--;
  }

  for (int i = N-1; i >= 0; i--) {
    if (i < N-1) s[i + 1] = 'a';
    for (int j = 1; j < 26; j++) {
      s[i]++;
      bool exist = false;
      for (auto item : ans) {
        exist = isSameType(item, s);
      }
      //cout << s << " " << exist << endl;
      if (exist == false) ans.push_back(s);
    }
  }

  for (auto item : ans) cout << item << endl;
  return 0;
}
