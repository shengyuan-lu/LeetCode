class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True
        
        no_prereq = set()
        
        graph = dict()
        
        for prereq in prerequisites:
            course, pre = prereq
            
            if course in graph.keys():
                graph[course].add(pre)
            else:
                graph[course] = set()
                graph[course].add(pre)
                
            if pre not in graph.keys():
                graph[pre] = set()
                
                
        keys_involved = set(graph.keys())
        
        keys_visited = set()
            
        
        for key in graph.keys():
            if len(graph[key]) == 0:
                no_prereq.add(key)
                keys_visited.add(key)
       
    
        while len(no_prereq) != 0:
            random_key = no_prereq.pop()
            
            del graph[random_key]
              
            for k in graph.keys():
                if random_key in graph[k]:
                    graph[k].remove(random_key)
            
            for key in graph.keys():
                if len(graph[key]) == 0:
                    no_prereq.add(key)            
                    keys_visited.add(key)
                    
        return keys_involved == keys_visited
