from functools import lru_cache



#basic format of test data
WIDTH = 3
HEIGHT = 4
COST = 5
panes = [(3,3,10), (1,2,3), (1,3,4)]



def get_max_profit(width, height, cost, pane_info):
    
    @lru_cache(None)
    def recurse_max_profit(w, h):

        if nothing_fits(w, h, pane_info):
            return 0
        
        one_left, pane = one_fits(w, h, pane_info)
        if one_left:
            #take into account possibility of one cut remaining
            if sorted([pane[0], pane[1]]) == sorted([w, h]):
                return pane[2]
            else:
                return max(pane[2] - cost, 0)
            
        else:
            #check option of current size matching pane
            best_pane = 0
            for pane in pane_info:
                if sorted([pane[0], pane[1]]) == sorted([w, h]):
                    best_pane = max(best_pane, pane[2])
            #get max option cutting vertically
            max_vert_widths = max((recurse_max_profit(w - x[0], h) + recurse_max_profit(x[0], h) for x in pane_info if x[0] < w), default=0)
            max_vert_heights = max((recurse_max_profit(w - x[1], h) + recurse_max_profit(x[1], h) for x in pane_info if x[1] < w), default=0)
            
            #get max option cutting horizontally
            max_hori_widths = max((recurse_max_profit(w, h - x[0]) + recurse_max_profit(w, x[0]) for x in pane_info if x[0] < h), default=0)
            max_hori_heights = max((recurse_max_profit(w, h - x[1]) + recurse_max_profit(w, x[1]) for x in pane_info if x[1] < h), default=0)
            
            return max(max(max_hori_widths, max_hori_heights, max_vert_heights, max_vert_widths) - cost, best_pane)
        
        
    return recurse_max_profit(width, height)
            
            
            
def nothing_fits(width, height, panes):
    for pane in panes:
        if pane_fits(width, height, pane):
            return False
        
    return True



def one_fits(width, height, panes):
    only_one_fits = []
    for pane in panes:
        max_dim = max(pane[0], pane[1])
        if not nothing_fits(max(width, height) - max_dim, min(width, height), panes) and pane_fits(width, height, pane):
            return False, None
        elif pane_fits(width, height, pane):
            only_one_fits.append(pane)
            
    return True, max(only_one_fits, key=lambda x : x[2])



def pane_fits(width, height, pane):
    if max(pane[0], pane[1]) <= max(width, height) and min(pane[0], pane[1]) <= min(width, height):
        return True
    
    return False
    
    
    
def main():
    n = int(input())
    for _ in range(n):
        problem_info = input().split(" ")
        width, height, cost = int(problem_info[0]), int(problem_info[1]), int(problem_info[2])
        num_panes = int(problem_info[3])
        panes = []
        
        for _ in range(num_panes):
            pane = input().split(" ")
            pane_info = (int(pane[0]), int(pane[1]), int(pane[2]))
            panes.append(pane_info)
            
        print(get_max_profit(width, height, cost, panes))
            
            
main()
#print(get_max_profit(WIDTH, HEIGHT, COST, panes))