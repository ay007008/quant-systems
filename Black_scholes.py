import math
def N(x):
    return 0.5 * ( 1 + math.erf(x/math.sqrt(2)))
def black_scholes(S, K, T, r, sigma, option_type='call'):
    if T <= 0:                                    # edge case only
        return max(S-K, 0) if option_type == 'call' else max(K-S, 0)
    d1 = (math.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    if option_type == 'call':
        return S*N(d1) - K*math.exp(-r*T)*N(d2)
    else:
        return K*math.exp(-r*T)*N(-d2) - S*N(-d1)
#Verification using put-call parity#
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20
C = black_scholes(S, K, T, r, sigma, 'call')
P = black_scholes(S, K, T, r, sigma, 'put')
error = C - P - (S - K * math.exp(-r * T))
assert abs(error) < 1e-9, f"Parity violated: {error}"
print(f"Call: {C:.4f}")
print(f"Put:  {P:.4f}")
