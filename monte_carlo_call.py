import math
import random

def monte_carlo_call(S, K, T, r, sigma, n_paths=100_000, seed=42):
    random.seed(seed)
    payoffs = []

    for _ in range(n_paths):
        Z = random.gauss(0, 1)
        S_T = S * math.exp((r - 0.5*sigma**2)*T + sigma*math.sqrt(T)*Z)
        payoffs.append(max(S_T - K, 0))

    mean_payoff = sum(payoffs) / n_paths
    price = math.exp(-r*T) * mean_payoff

    variance = sum((p - mean_payoff)**2 for p in payoffs) / (n_paths - 1)
    std_err = math.exp(-r*T) * math.sqrt(variance / n_paths)
    ci = (price - 1.96*std_err, price + 1.96*std_err)

    return price, std_err, ci
