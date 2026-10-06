class UnionFind:
    def __init__(self, v: List[int]):
        self.rep = { x: x for x in v }  # Everyone is its own rep
        self.rank = { x: 1 for x in v } # How many does it represent


    def find(self, x: int) -> int:
        cur = x
        while self.rep[cur] != cur:
            # self.rep[cur] = self.rep[self.rep[cur]]
            cur = self.rep[cur]
        return cur

    def union(self, x: int, y: int) -> bool:
        rep_x = self.find(x)
        rep_y = self.find(y)

        if rep_x == rep_y:
            return False

        if self.rank[rep_x] >= self.rank[rep_y]:
            self.rank[rep_x] += self.rank[rep_y]
            self.rep[rep_y] = rep_x
        else:
            self.rank[rep_y] += self.rank[rep_x]
            self.rep[rep_x] = rep_y
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(list(range(n)))

        result = n
        for u, v in edges:
            if uf.union(u, v):
                result -= 1

        print(list(filter(lambda i: i[0] == i[1], uf.rep.items())))

        # return len(list(filter(lambda i: i[0] == i[1], uf.rep.items())))
        return result
        