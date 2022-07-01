class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        keys = list()
        
        visited.add(0)
        keys.extend(rooms[0])
        
        while keys:
            random_key = keys.pop()
            
            if random_key not in visited:
                visited.add(random_key)
                
                keys.extend(rooms[random_key])
                
        return len(rooms) == len(visited)
