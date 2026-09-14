"""Chapter 6 deterministic verification. Python 3.12+, standard library.
Exact Fraction checks and separately labelled floating-point checks.
Prints JSON; no files, external data, random sampling or network access.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, sin, cos, pi, log2
import json
import platform

TOL = 1e-12


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def add(a, b, scale=1):
    return [[x + scale * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def inner(v, w):
    return sum(x.conjugate() * y for x, y in zip(v, w))


def outer(v):
    return [[x * y.conjugate() for y in v] for x in v]


def near_matrix(a, b):
    return all(abs(x - y) <= TOL for ar, br in zip(a, b)
               for x, y in zip(ar, br))


def distance(v, w):
    return sqrt(max(0, 2 - 2 * abs(inner(v, w))))


def main():
    v1, v2 = [F(1), F(0)], [F(3, 5), F(4, 5)]
    alpha, beta = F(3, 5), F(4, 5)
    v = [alpha*x + beta*y for x, y in zip(v1, v2)]
    norm2 = inner(v, v)
    require(inner(v1,v1) == inner(v2,v2) == alpha**2+beta**2 == 1,
            "unit inputs and coefficient normalization")
    require(v == [F(27,25), F(16,25)] and norm2 == F(197,125),
            "nonorthogonal counterexample")
    require(norm2 == alpha**2+beta**2+2*alpha*beta*inner(v1,v2),
            "cross term identity")
    require([x-y for x,y in zip(v1,v1)] == [0,0], "zero sum excluded")
    old_formation = F(71,100)**2 + 2*F(1,2)**2
    require(old_formation == F(10041,10000), "first-edition rounding")
    require(F(1,2)+2*F(1,2)**2 == 1, "corrected formation normalization")
    h = F(1,2)
    rho_plus = [[h,h],[h,h]]
    rho_minus = [[h,-h],[-h,h]]
    mix = [[h,F(0)],[F(0),h]]
    p0 = [[F(1),F(0)],[F(0),F(0)]]
    p1 = [[F(0),F(0)],[F(0),F(1)]]
    identity = [[F(1),F(0)],[F(0),F(1)]]
    require(add(rho_plus,rho_minus)==identity==add(p0,p1),
            "nonunique equal ensembles")
    table = []
    for label, rho, expected in [
            ("rho_plus",rho_plus,[h,F(1)]),
            ("rho_minus",rho_minus,[h,F(0)]),
            ("rho_mix",mix,[h,h])]:
        probs = [trace(mul(rho,p0)),trace(mul(rho,rho_plus))]
        require(probs == expected, "Table 6.1 "+label)
        require(adj(rho)==rho and trace(rho)==1, "Hermitian trace-one state")
        # For a Hermitian 2x2 matrix these principal minors certify PSD.
        require(rho[0][0]>=0 and rho[1][1]>=0
                and rho[0][0]*rho[1][1]-rho[0][1]*rho[1][0]>=0,
                "two-dimensional positivity")
        table.append({"state":label,"P0":str(probs[0]),"Pplus":str(probs[1])})
    bell = [[F(0) for _ in range(4)] for _ in range(4)]
    for i,j in product([0,3],repeat=2):
        bell[i][j]=h
    reduced = [[sum(bell[2*i+b][2*j+b] for b in range(2))
                for j in range(2)] for i in range(2)]
    require(reduced==mix, "partial trace")
    local = [[rho_plus[i//2][j//2] * int(i%2==j%2)
              for j in range(4)] for i in range(4)]
    require(trace(mul(bell,local))==trace(mul(reduced,rho_plus))==h,
            "local probability from reduced state")
    a=[[F(0),F(1)],[F(0),F(0)]]
    comm=add(mul(a,adj(a)),mul(adj(a),a),-1)
    require(comm==[[1,0],[0,-1]] and trace(comm)==0 and trace(identity)==2,
            "finite commutator obstruction")
    def entropy(probs):
        return -sum(float(p)*log2(float(p)) for p in probs if p)
    require(entropy([1,0])==0 and entropy([h,h])==1,
            "entropy not affine")
    # Floating-point checks, explicitly separate from the exact checks.
    s=1/sqrt(2)
    vectors=[[1+0j,0j],[0j,1+0j],[s+0j,s+0j],
             [s+0j,-s+0j],[s+0j,1j*s]]
    phase_count=0
    for v in vectors:
        for phase in [1,-1,1j,-1j]:
            phased=[phase*x for x in v]
            require(near_matrix(outer(v),outer(phased)), "global phase")
            require(distance(v,phased)<1e-7,"ray zero for equal rays")
            phase_count+=1
    # Values very close to overlap one need a looser distance tolerance
    # because the square root magnifies cancellation.
    for v,w in product(vectors,repeat=2):
        z=inner(v,w)
        phase=z.conjugate()/abs(z) if abs(z)>TOL else 1
        diff=[x-phase*y for x,y in zip(v,w)]
        require(abs(inner(diff,diff).real-distance(v,w)**2)<=TOL,
                "phase-minimized squared distance")
        delta=add(outer(v),outer(w),-1)
        require(abs(trace(mul(delta,delta)).real-(2-2*abs(z)**2))<=TOL,
                "pure-state Hilbert-Schmidt identity")
    for v,w,x in product(vectors,repeat=3):
        require(distance(v,x)<=distance(v,w)+distance(w,x)+1e-7,
                "sample ray triangle inequality")
    # Two measurement settings leave the imaginary entry unobserved.
    ip,im=outer([s,1j*s]),outer([s,-1j*s])
    require(not near_matrix(ip,im), "distinct relative phases")
    for effect in [p0,rho_plus]:
        require(abs(trace(mul(ip,effect))-trace(mul(im,effect)))<=TOL,
                "two-setting incompleteness")
    trajectory=[]
    for t in [0,0.25,0.5,1,pi]:
        u=[[cos(t),-1j*sin(t)],[-1j*sin(t),cos(t)]]
        psi=[cos(t),-1j*sin(t)]
        derivative=[-sin(t),-1j*cos(t)]
        require(near_matrix(mul(adj(u),u),identity), "unitarity")
        require(abs(inner(psi,psi)-1)<=TOL, "trajectory norm")
        require(all(abs(1j*derivative[i]-psi[1-i])<=TOL for i in range(2)),
                "Schrodinger equation for K=X")
        require(near_matrix(mul(mul(u,p0),adj(u)),outer(psi)),
                "pure density propagation")
        require(near_matrix(mul(mul(u,mix),adj(u)),mix), "mixed propagation")
        trajectory.append({"t":t,"squared_norm":inner(psi,psi).real})
    output={"status":"passed","chapter":6,"python":platform.python_version(),
            "exact_counterexample_norm_squared":str(norm2),
            "first_edition_formation_norm_squared":str(old_formation),
            "corrected_formation_norm_squared":"1",
            "table_6_1":table,"exact_matrix_checks":"passed",
            "floating_absolute_tolerance":TOL,
            "ray_distance_tolerance_near_zero":1e-7,
            "global_phase_checks":phase_count,"ray_triangle_samples":125,
            "unitary_trajectory":trajectory,
            "empirical_data_used":False,"random_sampling":False}
    print(json.dumps(output,indent=2))


if __name__=="__main__":
    main()
