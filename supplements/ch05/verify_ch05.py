"""Chapter 5 exact finite-model checks. Python 3.12+, standard library.
Prints JSON; writes no files. No observations or random simulation.
The grid supplements, and does not replace, the general proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import log2, isclose
import json
import platform


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def entropy(probabilities):
    return -sum(float(p) * log2(float(p)) for p in probabilities if p)


def enumerate_joint(epsilon):
    law = {(a, b): F(0) for a, b in product(range(2), repeat=2)}
    for z, na, nb in product(range(2), repeat=3):
        weight = F(1, 2)
        weight *= epsilon if na else 1 - epsilon
        weight *= epsilon if nb else 1 - epsilon
        law[z ^ na, z ^ nb] += weight
    return law


def verify(epsilon):
    law = enumerate_joint(epsilon)
    r = 2 * epsilon * (1 - epsilon)
    expected = {(a, b): (1 - r) / 2 if a == b else r / 2
                for a, b in product(range(2), repeat=2)}
    require(law == expected, "joint law from eight latent assignments")
    require(sum(law.values()) == 1 and min(law.values()) >= 0,
            "positive diagonal density with trace one")
    pa = [sum(law[a, b] for b in range(2)) for a in range(2)]
    pb = [sum(law[a, b] for a in range(2)) for b in range(2)]
    require(pa == pb == [F(1, 2)] * 2, "uniform marginals")
    alignment = law[0, 0] + law[1, 1]
    independent = sum(pa[a] * pb[a] for a in range(2))
    require(alignment == 1 - r, "alignment")
    require(alignment - independent == (1 - 2 * epsilon)**2 / 2,
            "alignment gain")
    weight = (1 - 2 * epsilon)**2
    initial = [F(1, 2), F(0), F(0), F(1, 2)]
    diagonal = [law[a, b] for a, b in product(range(2), repeat=2)]
    require(diagonal == [weight * p + (1 - weight) / 4 for p in initial],
            "Chapter 4 depolarizing identity")
    require((diagonal == [F(1, 4)] * 4) == (epsilon == F(1, 2)),
            "product iff endpoint")
    branches = []
    for a in range(2):
        projected = [law[x, y] if x == a else F(0)
                     for x, y in product(range(2), repeat=2)]
        probability = sum(projected)
        require(probability == F(1, 2), "branch probability")
        posterior = [x / probability for x in projected]
        target = [((1 - r) if x == y else r) if x == a else F(0)
                  for x, y in product(range(2), repeat=2)]
        require(posterior == target and sum(posterior) == 1,
                "normalized conditional state")
        branches.append(projected)
    require([sum(v) for v in zip(*branches)] == diagonal,
            "nonselective projection unchanged")
    successes = {''.join(map(str, g)): sum(law[a, g[a]] for a in range(2))
                 for g in product(range(2), repeat=2)}
    require(max(successes.values()) == successes["01"] == 1 - r,
            "all four deterministic predictors")
    require(max(pb) == F(1, 2), "best uninformative prediction")
    hjoint = entropy(law.values())
    mi_entropy = entropy(pa) + entropy(pb) - hjoint
    mi_direct = sum(float(p) * log2(float(p / (pa[a] * pb[b])))
                    for (a, b), p in law.items() if p)
    mi_formula = 1 - entropy([r, 1 - r])
    require(isclose(hjoint, 1 + entropy([r, 1-r]), rel_tol=0, abs_tol=1e-12),
            "joint entropy identity")
    require(isclose(mi_entropy, mi_direct, rel_tol=0, abs_tol=1e-12)
            and isclose(mi_direct, mi_formula, rel_tol=0, abs_tol=1e-12),
            "mutual information, three expressions")
    return {"epsilon": str(epsilon), "r": str(r),
            "probabilities_00_01_10_11": [str(p) for p in diagonal],
            "alignment": str(alignment), "independent": str(independent),
            "predictor_success_by_outputs_for_A0_A1":
                {g: str(v) for g, v in successes.items()},
            "mutual_information_bits": mi_direct}


def main():
    rows = [verify(F(k, 20)) for k in range(11)]
    table = [row for row in rows if row["epsilon"] in ("0", "1/4", "1/2")]
    require([r["probabilities_00_01_10_11"] for r in table] ==
            [["1/2", "0", "0", "1/2"],
             ["5/16", "3/16", "3/16", "5/16"],
             ["1/4", "1/4", "1/4", "1/4"]], "Table 5.1 probabilities")
    require([r["alignment"] for r in table] == ["1", "5/8", "1/2"],
            "Table 5.1 alignment")
    print(json.dumps({"status": "passed", "chapter": 5,
                      "python": platform.python_version(),
                      "method": "exact rational enumeration; floating-point entropy cross-check",
                      "grid": "epsilon = k/20 for k=0,...,10",
                      "latent_assignments_per_parameter": 8,
                      "predictors_per_parameter": 4,
                      "entropy_absolute_tolerance": 1e-12,
                      "empirical_data_used": False, "random_simulation": False,
                      "table_5_1": table, "all_results": rows}, indent=2))


if __name__ == "__main__":
    main()
