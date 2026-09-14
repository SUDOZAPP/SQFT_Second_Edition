"""Exact algebra checks for Chapter 4; Python 3.12+, standard library only.
Prints JSON; no file writes, network, data files or random seeds are required.
This verifies the specified examples, not the general proofs or social validity.
"""
from fractions import Fraction as Q
import json

def zero(n): return [[Q(0) for _ in range(n)] for _ in range(n)]
def basis(n,j,k):
    a=zero(n); a[j][k]=Q(1); return a
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a): return [[c*x for x in ar] for ar in a]
def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b))] for i in range(len(a))]
def adj(a): return [list(row) for row in zip(*a)] # all matrices here are real
def tr(a): return sum(a[i][i] for i in range(len(a)))
def total(items,n):
    out=zero(n)
    for x in items: out=add(out,x)
    return out
def eye(n): return total((basis(n,i,i) for i in range(n)),n)
def kraus(vs,x): return total((mul(mul(v,x),adj(v)) for v in vs),len(x))
def require(condition,name):
    if not condition: raise AssertionError(name)

n=4; ident=eye(n)
vs=[scale(Q(1,2),basis(n,j,k)) for j in range(n) for k in range(n)]
require(total((mul(adj(v),v) for v in vs),n)==ident,'Kraus completeness')
R=lambda x:scale(tr(x)/4,ident)
E=lambda w,x:add(scale(w,x),scale(1-w,R(x)))
weights=[Q(0),Q(1,4),Q(1,2),Q(1)]
for j in range(n):
    for k in range(n):
        x=basis(n,j,k)
        require(kraus(vs,x)==R(x),'replacement on matrix basis')
        require(R(R(x))==R(x),'replacement idempotence')
        # L_jk = sqrt(gamma) V_jk; check the coefficient of gamma.
        loss=scale(Q(1,2),add(mul(ident,x),mul(x,ident)))
        require(add(kraus(vs,x),scale(-1,loss))==add(R(x),scale(-1,x)),'generator')
        for w in weights:
            require(tr(E(w,x))==tr(x),'trace preservation')
            for u in weights:require(E(w,E(u,x))==E(w*u,x),'composition')
P=[basis(n,j,j) for j in range(n)]
require(total(P,n)==ident,'projective completeness')
rho=scale(Q(1,2),add(P[0],P[3])); C=add(P[0],P[3])
scores={}
for w in weights:
    out=E(w,rho)
    require(tr(out)==1,'state trace')
    require(all(out[i][j]==0 for i in range(n) for j in range(n) if i!=j),'diagonal state')
    require(all(out[i][i]>=0 for i in range(n)),'diagonal positivity')
    score=tr(mul(out,C));require(score==(1+w)/2,'expected score')
    scores[str(w)]=str(score)
rho2=scale(Q(1,2),eye(2));p=basis(2,0,0);num=mul(mul(p,rho2),p)
prob=tr(num);require(prob==Q(1,2),'projection probability')
require(scale(1/prob,num)==p,'normalized posterior')
print(json.dumps({'chapter':4,'arithmetic':'exact fractions','matrix_basis_tests':16,
    'weights':[str(w) for w in weights],'weights_meaning':'w = exp(-gamma*t); w=0 includes limiting replacement map',
    'kraus_completeness':True,'replacement_identity':True,'generator_identity':True,
    'composition_identity':True,'projection_probability':str(prob),'posterior_trace':'1',
    'scores':scores,'status':'passed','scope':'specified algebraic identities and examples; not empirical validation'},indent=2))
