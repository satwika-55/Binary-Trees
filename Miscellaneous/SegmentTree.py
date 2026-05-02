class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # range sum query [l, r]
    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0  # no overlap
        if l <= start and end <= r:
            return self.tree[node]  # full overlap
        
        mid = (start + end) // 2
        return self._query(2 * node + 1, start, mid, l, r) + \
               self._query(2 * node + 2, mid + 1, end, l, r)

    # point update: set index idx to val
    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node + 1, start, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, val)

            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


# Example usage
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print(st.query(1, 3))  # 3 + 5 + 7 = 15
st.update(1, 10)
print(st.query(1, 3))  # 10 + 5 + 7 = 22
