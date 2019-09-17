class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        while len(queue) != 0:
            cur = queue.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            for num in rooms[cur]:
                queue.append(num)
        if len(visited) == len(rooms):
            return True
        else:
            return False