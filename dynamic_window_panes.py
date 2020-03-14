from functools import lru_cache


WIDTH = 4
HEIGHT = 3
COST = 5
panes = [(2, 1, 10)]


def get_max_profit(width, height, cost, pane_info):
    
    @lru_cache(None)
    def recurse_max_profit(w, h):
        if nothing_fits(w, h, pane_info):
            return 0
        
        one_left, pane = one_fits(w, h, pane_info)
        if one_left:
            return pane[2]
            
        else:
            #get max option cutting vertically
            max_vert_widths = max((recurse_max_profit(w - x[0], h) + recurse_max_profit(x[0], h) for x in pane_info if x[0] < w), default=0)
            #print(w, h, max_vert_widths)
            max_vert_heights = max((recurse_max_profit(w - x[1], height) + recurse_max_profit(x[1], h) for x in pane_info if x[1] < w), default=0)
            
            #get max option cutting horizontally
            max_hori_widths = max((recurse_max_profit(w, h - x[0]) + recurse_max_profit(w, x[0]) for x in pane_info if x[0] < h), default=0)
            max_hori_heights = max((recurse_max_profit(w, h - x[1]) + recurse_max_profit(w, x[1]) for x in pane_info if x[1] < h), default=0)
            
            #print(max_vert_heights, max_vert_widths, max_hori_widths, max_hori_heights)
            return max(max(max_hori_widths, max_hori_heights, max_vert_heights, max_vert_widths), 0)
        
        
    return recurse_max_profit(width, height)
            
            
            
def nothing_fits(width, height, panes):
    for item in panes:
        if min(item[0], item[1]) <= min(width, height) and max(item[0], item[1]) <= max(width, height):
            return False
        
    return True



def one_fits(width, height, panes):
    only_one_fits = []
    for pane in panes:
        max_dim = max(pane[0], pane[1])
        if not nothing_fits(max(width, height) - max_dim, min(width, height), panes):
            return False, None
        else:
            only_one_fits.append(pane)
            
    return True, max(only_one_fits, key=lambda x : x[2])



print(get_max_profit(WIDTH, HEIGHT, COST, panes))