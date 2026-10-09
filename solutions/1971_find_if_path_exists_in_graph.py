class Solution:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int
    ) -> bool:

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = {source}
        stack = [source]

        while stack:
            current = stack.pop()

            if current == destination:
                return True

            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return False
