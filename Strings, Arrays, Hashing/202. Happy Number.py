class Solution:
    def isHappy(self, n: int) -> bool:
        integer = n
        total = 0
        dic = dict()
        
        while True:
            
            integer_og = integer
            
            while integer != 0:
                total += pow(integer % 10, 2)
                integer = (integer - integer % 10) / 10
                
            if total == 1:
                return True
            else:
                if integer_og not in dic.keys():
                    dic[integer_og] = total
                    integer = total
                    total = 0
                    
                else:
                    if dic[integer_og] == total: 
                        return False
