# bottom-up DP joint distribution

from collections import defaultdict


def Skew(t, eps = 1e-9):
    joint = {(0,1): 1.0}  # (X_0, X_1)

    for t in range(2, t+1):
        new_joint = defaultdict(float)
        
        for (xt2, xt1), prob in joint.items():
            if prob > eps:
                new_joint[(xt1, xt1 + xt2)] += prob / 2
                new_joint[(xt1, xt1 - xt2)] += prob / 2

        joint = new_joint

        del new_joint

        print(t, len(joint))
        #print(max(xt for xt1, xt in joint))

    # marginal dist for X_t
    marginal = defaultdict(float)
    for (xt1, xt), prob in joint.items():
        marginal[xt] += prob

    mu = sum(xt * prob for xt, prob in marginal.items())

    # distribution X_t - mu
    shift = {(xt - mu) : prob for (xt, prob) in marginal.items()}

    # SD = squareroot of second moment
    sd = sum(xt**2 * prob for xt, prob in shift.items()) ** 0.5

    print(f"mu={mu} sd={sd}")

    # normalized distribution (X - mu) / sd
    norm = {(xt - mu) / sd : prob for xt, prob in marginal.items()}

    skew = sum(x**3 * prob for x, prob in norm.items())

    return skew


print(round(Skew(50), 8))
