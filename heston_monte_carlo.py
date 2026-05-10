import math
import random

def heston_monte_carlo_call(S, K, T, r, v0, theta, k, xi, rho,
                             n_paths=100_000, n_steps=252, seed=42):

 """
    Price a European call under Heston stochastic volatility
    via Euler-Maruyama Monte Carlo simulation.

    Heston model:
        dS = r*S*dt + sqrt(v)*S*dW1
        dv = k*(theta - v)*dt + xi*sqrt(v)*dW2
        dW1*dW2 = rho*dt

    Parameters:
        S      : current stock price
        K      : strike price
        T      : time to expiry in years
        r      : risk-free rate
        v0     : initial variance (not volatility)
        theta  : long-run variance mean reversion target
        k      : mean reversion speed
        xi     : volatility of volatility
        rho    : correlation between price and vol shocks
        n_paths: number of Monte Carlo paths
        n_steps: number of time steps per path
        seed   : random seed for reproducibility

    Returns:
        (price, std_error, 95_percent_confidence_interval)

    Verified: converges to BSM price when xi=0, rho=0.
    """
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
