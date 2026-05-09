import math
import random

def heston_monte_carlo_call(S, K, T, r, v0, theta, k, xi, rho,
                             n_paths=100_000, n_steps=252, seed=42):
    random.seed(seed)
    dt = T / n_steps
    payoffs = []

    for _ in range(n_paths):
        S_t = S
        v_t = v0

        for _ in range(n_steps):
            Z1 = random.gauss(0, 1)
            Z2 = random.gauss(0, 1)
            W1 = Z1
            W2 = rho*Z1 + math.sqrt(1 - rho**2)*Z2

            v_t = max(v_t + k*(theta - v_t)*dt +
                      xi*math.sqrt(max(v_t, 0)*dt)*W2, 0)

            S_t = S_t * math.exp((r - 0.5*v_t)*dt +
                                  math.sqrt(max(v_t, 0)*dt)*W1)

        payoffs.append(max(S_t - K, 0))

    mean_payoff = sum(payoffs) / n_paths
    price = math.exp(-r*T) * mean_payoff

    variance = sum((p - mean_payoff)**2 for p in payoffs) / (n_paths - 1)
    std_err = math.exp(-r*T) * math.sqrt(variance / n_paths)
    ci = (price - 1.96*std_err, price + 1.96*std_err)

    return price, std_err, ci
