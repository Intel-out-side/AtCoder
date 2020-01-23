#include "mint.cpp"

struct combination {
  vector<mint> frac, ifrac;
  combination(int n):fact(n+1), ifact(n+1) {
    fact[0] = 1;
    for (int i = 1; i < n; ++i) {
      fact[i] = fact[i - 1] * i;
    }
    ifact[n] = fact[i].inv();
  }

};
