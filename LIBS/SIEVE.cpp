struct Sieve {
  int n;
  vector<int> f, primes;
  Sieve(int n = 1): n(n), f(n + 1) {
    f[0] = f[1] = -1;
    for (int i = 2; i <= n; i++) {
      if (f[i]) continue; //印がなければ素数扱い
      primes.push_back(i);
      for (int j = i; j <= n; j += i) {
        f[j] = i; //iの倍数のところに印をつけていく
      }
    }
  }

  bool isPrime(int x) { return f[x] == x; }

  //ｘを素因数分解する関数
  // return -> 素因数
  vector<int> factorList(int x) {
    vector<int> res;
    while (x != 1) {
      res.push_back(f[x]);
      x /= f[x];
    }
    return res; //大きい順で素因数がvectorに格納されて出てくる
  }

  //各素因数が何乗されているかをpair typeで返す
  vector<P> factorPower(int x) {
    vector<int> factors = factorList(x);
    if (factors.size() == 0) return {};
    vector<P> res(1, P(factors[0], 0));
    for (int p : factors) {
      if (res.back().first == p) {
        res.back().second ++;
      }
      else {
        res.emplace_back(p, 1);
      }
    }
      return res;
    }
  };
