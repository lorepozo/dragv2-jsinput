# Regex (this is to make python pretty in html):
# .replace(/[\n\r]/g,'<br>')
# .replace(/\s{4}/g,'&nbsp;&nbsp;&nbsp;&nbsp;')
# .replace(/\s+/g,' ')
# .replace(/(def |import|if|elif|else|for|return|continue|break)/g,'<span style="color:#8A59A8;">$1</span>')
# .replace(/(None|False|True|\d+(?=]|:|<br>|,))/g,'<span style="color:#ED821C;">$1</span>')
# .replace(/( not | in |==|!=|\+| - |&amp;lt;|&amp;gt;| and | or )/g,'<span style="color:#3D999E;">$1</span>')
# .replace(/([\w\.]+\(.*?\))/g,'<span style="color:#5C70AD;">$1</span>')
# .replace(/("[\w\s]+?")/g,'<span style="color:#4A9933;">$1</span>')
# .replace(/<\/span> </g,' </span><')
# .replace(/(# .+?)<br/g,'<span style="opacity:.5">$1</span><br')
# .replace(/'/g,"\'")

import json

solutions = $VAL$ # [SOLUTION,...]
common_mistakes = [] # [[FALSE_SOLUTION,MSG],...] # For predictable false solutions and corresponding feedback.

# You can mess with this lots
def isNear(pos, target, d):
    return abs(pos[0]-target[0])&lt;d["size"]["width"]/2 and abs(pos[1]-target[1])&lt;d["size"]["height"]/2

# Definitely don't mess with this
def rcheck(states, targets, d):
    if len(states) != len(targets): return False
    if len(states) == 0: return True
    suitables = [state for state in states if isNear(state, targets[0], d)]
    for suitable in suitables:
        newStates=list(states)
        newStates.remove(suitable)
        if rcheck(newStates, targets[1:], d): return True
    return False

# You probably shouldn't be messing with this
def check(expect, ans):
    par = json.loads(ans)
    init = json.loads(par["answer"])
    state = json.loads(par["state"])
    dN = {init["draggables"][i]["id"]: i for i in xrange(len(init["draggables"]))}
    def grade(solution):
        if len(state)!=len(solution): return False
        for id in state:
            d=init["draggables"][dN[id]]
            if id not in solution: return [False,id+' used, not in solution']
            elif d.get("reusable"):
                if not rcheck(state[id], solution[id], d): return [False,id+" in wrong place"]
            else:
                if not isNear(state[id], solution[id], d): return [False,id+" in wrong place"]
        return True
    for solution in solutions:
        g = grade(solution)
        # For debugging of a single solution, use: return {'ok':False,'msg':g[1]}
        if grade(solution): return True
    for mistake in common_mistakes:
        # For debugging of a single common mistake, use: return {'ok':False,'msg':g[1]}
        if grade(mistake[0]): return {'ok':False,'msg':mistake[1]}
    return False;