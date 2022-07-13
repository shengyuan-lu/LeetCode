from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # graph should be recipes : [ingredients]
        
        graph = self.get_graph(recipes, ingredients)
        
        can_be_made = set()
        
        while supplies:
            
            temp_supplies = list()
            
            for key, value in list(graph.items()):
                graph[key] = [item for item in graph[key] if item not in supplies]
                
                if len(graph[key]) == 0 and key in recipes:
                    can_be_made.add(key)
                    temp_supplies.append(key)
                    del graph[key]
                
            supplies.clear()
            
            supplies.extend(temp_supplies)
            
        return list(can_be_made)
          
    
    
    def get_graph(self, recipes, ingredients) -> defaultdict:
        
        graph = defaultdict(list)
        
        for index in range(len(recipes)):
            graph[recipes[index]] = ingredients[index]
        
        return graph
