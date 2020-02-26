

def build():
    t = input()
    s = input()
    retunr t, s

def run():
    t, s = build()


    def dfs(i, j, lst, ret):

        if t[i] == '*':
            
        else:
            if t[i] == s[j]:
                dfs(i+1, j+1, lst, ret)
            else:
                return []
        
