"""Course Schedule

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/course-schedule/

Problem summary: Determine whether all courses can be completed given prerequisite edges.
Approach: Kahn's algorithm removes zero-indegree vertices; all courses are possible if every vertex is processed.
Complexity: O(V+E) time and O(V+E) space.
"""

from collections import deque

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course); indegree[course] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    seen = 0
    while queue:
        node = queue.popleft(); seen += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0: queue.append(neighbor)
    return seen == num_courses

assert can_finish(2, [[1, 0]])
assert not can_finish(2, [[1, 0], [0, 1]])
assert can_finish(3, [])
