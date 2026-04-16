# ======================================================
# COURSE SCHEDULE (LeetCode 207)
# ======================================================

# Problem:
# There are numCourses courses labeled from 0 to numCourses-1.
# You are given prerequisites where prerequisites[i] = [a, b]
# means you must take course b before course a.
# Return True if you can finish all courses, else False.
#
# (Cycle detection in Directed Graph)


# ------------------------------------------------------
# 1️⃣ Brute Force (Try All Paths - Inefficient)
# ------------------------------------------------------

class BruteForceSolution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course, visited):
            if course in visited:
                return False

            visited.add(course)

            for nei in graph[course]:
                if not dfs(nei, visited):
                    return False

            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True


# ------------------------------------------------------
# 2️⃣ DFS with Recursion Stack (Cycle Detection)
# ------------------------------------------------------

class DFSSolution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses  # 0=unvisited,1=visiting,2=visited

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


# ------------------------------------------------------
# 3️⃣ BFS (Kahn’s Algorithm - Topological Sort)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Using Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        for i in range(numCourses):
            if visited[i] != 0:
                continue

            stack = [(i, False)]

            while stack:
                node, processed = stack.pop()

                if processed:
                    visited[node] = 2
                    continue

                if visited[node] == 1:
                    return False
                if visited[node] == 2:
                    continue

                visited[node] = 1
                stack.append((node, True))

                for nei in graph[node]:
                    stack.append((nei, False))

        return True


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Kahn’s Algorithm BFS)
# ------------------------------------------------------

class OptimalSolution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return completed == numCourses






