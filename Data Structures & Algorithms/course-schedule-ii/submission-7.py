from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Build adjacency list + in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Start with all courses that have NO prerequisites
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        # BFS
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1        # one prereq done
                if in_degree[next_course] == 0:
                    queue.append(next_course)      # now ready

        # If not all courses processed → cycle
        return order if len(order) == numCourses else []
