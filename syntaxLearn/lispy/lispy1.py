#-*_coding:utf-8_*_

def eval(x,env=global_env):
    '''evalute an expr in an  env'''
    if isa(x,Symbol): #variable
        return env.find(x)[x]
    
    elif not isa(x,list): #constant litereal
        return x
    elif x[0]=='quote': #(quote exp)
        (_,exp)=x
        return exp
    
    elif x[0]=='if': #(if test conseq alter)
        (_,test,conseq,alt)=x
        return eval((conseq if eval(test,env) else alt),env)
    
    elif x[0]=='set!': #(set! var exp)
        (_,var,exp)=x
        env.find(var)[var]=eval(exp,env)
    
    elif x[0]=='define': #(define var exp)
        env[var]=eval(exp,env)
    elif x[0]=='lambda': #(lambda (var *)exp)
        (_,vars,exp)=x
        return lambda *args:eval(exp,Env(vars,env))
    elif x[0]=='begin': #(begin exp *)
        for exp in x[1:]:
            val = eval (exp,env)
        return val
    else:               #(proc exp*)
        exps=[eval(exp,env) for exp in x]
        proc=exps.pop(0)
        return proc(*exps)
    
isa=isinstance

    