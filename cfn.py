# Regex (this is to make python pretty in html):
# .replace(/(def |import|if|elif|else|for|return|continue|break)/g,'<span style="color:#8A59A8;">$1</span>')
# .replace(/(None|False|True|\d+(?=]|:|<br\/>|,))/g,'<span style="color:#ED821C;">$1</span>')
# .replace(/( not | in |==|!=|\+| - |&amp;lt;|&amp;gt;| and | or )/g,'<span style="color:#3D999E;">$1</span>')
# .replace(/([\w\.]+\(.*?\))/g,'<span style="color:#5C70AD;">$1</span>')
# .replace(/(&quot;[\w ]+?&quot;)/g,'<span style="color:#4A9933;">$1</span>')
# .replace(/<\/span> </g,' </span><')

import json

# You can mess with this lots
def isNear(pos,target,d):
    return abs(pos[0]-target[0])&lt;d["size"]["width"]/2 and abs(pos[1]-target[1])&lt;d["size"]["height"]/2

# Definitely don't mess with this
def rcheck(states,targets,d):
    if len(states) != len(targets): return False
    if len(states) == 0: return True
    suitables = [state for state in states if isNear(state,targets[0],d)]
    for suitable in suitables:
        newStates=states
        newStates.remove(suitable)
        if rcheck(newStates,targets[1:],d): return True
    return False

# You probably shouldn't be messing with this (except for the first line)
def check(expect, ans):
    solution = #### your solution dictionary here
    par = json.loads(ans)
    init = json.loads(par["answer"])
    state = json.loads(par["state"])
    dN = {init["draggables"][i]["id"]: i for i in xrange(len(init["draggables"]))}
    for id in state:
        # If statement for draggables not defined in solution
        d=init["draggables"][dN[id]]
        pos = [d["pos"]["x"],d["pos"]["y"]]
        if solution.get(id)==None:
            if d.get("reusable"):
                if state[id][0]!=pos: return False
            else:
                if state[id]!=pos: return False
        # For reusable draggables defined in solution
        elif d.get("reusable"):
            if pos not in solution[id]: solution[id].append(pos)
            if not rcheck(state[id],solution[id],d): return False
        # For non-reusable draggables defined in solution
        else:
            if not isNear(state[id],solution[id],d): return False
    return True
