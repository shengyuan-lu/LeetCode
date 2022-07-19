class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        graph = defaultdict(set)
        
        rotten_stack = list()
        
        total_orange_count = 0
        total_rotten_set = set()
        
        # build the graph
        for i in range(0, m):
            
            for j in range(0, n):
                
                if grid[i][j] != 0: # fresh or rotten
                    
                    if grid[i][j] == 2:
                        rotten_stack.append((i,j))
                        total_rotten_set.add((i,j))

                    if i - 1 >= 0:
                        if grid[i-1][j] == 1:
                            graph[(i,j)].add((i-1,j))

                    if i + 1 < m:
                        if grid[i+1][j] == 1:
                            graph[(i,j)].add((i+1,j))

                    if j - 1 >= 0:
                        if grid[i][j-1] == 1:
                            graph[(i,j)].add((i,j-1))

                    if j + 1 < n:
                        if grid[i][j+1] == 1:
                            graph[(i,j)].add((i,j+1))
                            
                    total_orange_count += 1
        
        print(graph)

        if total_orange_count - len(total_rotten_set) == 0:
            return 0
        
        cycle_count = 0
        
        while rotten_stack:
            print(rotten_stack)
            
            cycle_count += 1
            
            temp_lst = list()
            
            for tup in rotten_stack:
            
                total_rotten_set = total_rotten_set | graph[tup]
                    
                temp_lst.extend(list(graph[tup]))

                del graph[tup]

                for key in graph.keys():
                    graph[key] -= set(rotten_stack)
            
            rotten_stack.clear()
            rotten_stack.extend(temp_lst)
            
            if total_orange_count == len(total_rotten_set):
                return cycle_count
        
        return -1
        
        
        
