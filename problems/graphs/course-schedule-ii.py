"""Course Schedule II

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/course-schedule-ii/

Problem summary: Return a valid order to take all courses, or an empty list if impossible.
Approach: Topologically sort the prerequisite graph with Kahn's algorithm.
Complexity: O(V+E) time and O(V+E) space.
"""

from collections import deque

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course); indegree[course] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    order = []
    while queue:
        node = queue.popleft(); order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0: queue.append(nxt)
    return order if len(order) == num_courses else []

order = find_order(2, [[1, 0]])
assert order.index(0) < order.index(1)
assert find_order(2, [[1, 0], [0, 1]]) == []
assert set(find_order(3, [])) == {0, 1, 2}
