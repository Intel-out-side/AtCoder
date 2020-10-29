#TSPをbitDPで解く解説
#https://www.slideshare.net/chokudai/wap-atcoder4
class TSP:
    """
    巡回セールスマン問題をbitDPで解きます。時間計算量はO(2^N N^2)です。N=17くらいだったら解ける

    Attributes:
        V : int
            頂点の数
        dist : 二次元リスト
            頂点s->tへのコスト。有向グラフです。
    """
    def __init__(self, V:int, dist:list):
        self.V = V
        self.dist = dist

    def solve(self):
        V2 = 1<<self.V
        dp = [[float("inf") for _ in range(self.V)] for _ in range(V2)]

        #初期状態：はじめ頂点０には訪れていて、それ以外には未訪問
        dp[1][0] = 0

        #0に帰ってこないで、とりあえず全部の都市を一回ずつ回る場合の最短距離
        for S in range(V2):
            for now in range(self.V):
                if dp[S][now] == float("inf"): continue
                #次の状態に関して探索する
                for nxt in range(self.V):
                    #もしnxtがすでに訪れた場所ならcontinue
                    if (S>>nxt)&1: continue

                    #次の頂点も入れた場合のbitの状態は以下
                    nextState = S | 1<<nxt
                    nextDistance = dp[S][now] + dist[now][nxt]

                    #配るDPで更新を行う
                    #これまで調べたものより短くなっていれば更新する
                    dp[nextState][nxt] = min(dp[nextState][nxt], nextDistance)

        all = V2-1
        ans = float("inf")

        for i in range(self.V):
            #もし最後の都市がiであることがありえないならcontinue
            if dp[all][i] == float("inf"): continue
            tmp = dp[all][i] + dist[i][0]
            ans = min(ans, tmp)

        return ans

tsp = TSP(V, dist)
ans = tsp.solve()

if ans == float("inf"):
    print(-1)
else:
    print(ans)
