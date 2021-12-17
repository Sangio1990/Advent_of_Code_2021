# Solutions do Day15 puzzle at https://adventofcode.com/2021
import heapq


class Day15:
    def __init__(self):
            with open('puzzle_input/input_day15.txt', 'r') as file:
                raw_data = file.read()
            file.close()
            self.cavern = self.parse_input(raw_data)
            self.n, self.m = len(self.cavern), len(self.cavern[0])
            print(f'Part 1: {self.part_one()}')  # 748
            print(f'Part 2: {self.part_two()}')  # 3045

    @staticmethod
    def parse_input(raw_data):
        res = []
        for line in raw_data.split('\n'):
            res.append(list(map(int, line)))
        return res

    @staticmethod
    def dijkstra(graph):
        r, c = len(graph), len(graph[0])
        costs = {}
        heap = [(0, 0, 0)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) == (r - 1, c - 1):
                return cost
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < r and 0 <= nj < c:
                    ncost = cost + graph[ni][nj]
                    if costs.get((ni, nj), float('inf')) <= ncost:
                        continue
                    costs[(ni, nj)] = ncost
                    heapq.heappush(heap, (ncost, ni, nj))

    def part_one(self):
        return self.dijkstra(self.cavern)

    def part_two(self):
        r, c = len(self.cavern) * 5, len(self.cavern[0]) * 5
        expanded = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                dist = i // self.n + j // self.m
                cur = self.cavern[i % self.n][j % self.m] + dist
                cur = cur % 9 or cur
                expanded[i][j] = cur
        return self.dijkstra(expanded)


