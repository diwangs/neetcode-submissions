class UnionFind:
    def __init__(self, n):
        self.rep = { x: x for x in range(n)}
        self.rank = { x: 1 for x in range(n)}
        self.top = n

    def find(self, x: int) -> int:
        n = x
        while self.rep[n] != n:
            n = self.rep[n]
        return n

    def union(self, a: int, b: int) -> bool:
        a_rep = self.find(a)
        b_rep = self.find(b)

        if a_rep == b_rep:
            return False

        self.top -= 1
        if self.rank[a_rep] > self.rank[b_rep]:
            self.rep[b_rep] = a_rep
            self.rank[a_rep] += self.rank[b_rep]
        else:
            self.rep[a_rep] = b_rep
            self.rank[b_rep] += self.rank[a_rep]

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if len(edges) > n-1:
        #     return False
        
        uf = UnionFind(n)
        for (u, v) in edges:
            if not uf.union(u, v): # cycle detected
                return False
        return uf.top == 1