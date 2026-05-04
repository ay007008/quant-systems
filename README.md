Quant Systems

Production-grade quantitative finance implementations 
built from first principles. No external pricing libraries.



Black-Scholes Options Pricer
File: Black_scholes.py

European call and put pricer using Black-Scholes formula.
Implements cumulative normal distribution via `math.erf` 
no scipy dependency. Verified with put-call parity.

| Input | Description |
|-------|-------------|
| S | Spot price |
| K | Strike price |
| T | Time to expiry (years) |
| r | Risk-free rate |
| sigma | Annualised volatility |

Verified output: Call(100,100,1,0.05,0.20) = 10.4506



Limit Order Book
File: order_book.py

Full order book with SortedDict price levels and 
hashmap for O(1) cancel lookup.

| Operation | Complexity |
|-----------|------------|
| add_order | O(log n) |
| cancel_order | O(log n) |
| best_bid | O(1) |
| best_ask | O(1) |

## Monte Carlo Options Pricer

European call pricer using Monte Carlo simulation with statistical 
validation.

- Simulates 100,000 GBM paths using Box-Muller normal sampling
- Computes discounted average payoff as fair value
- Returns 95% confidence interval via bootstrap standard error

```python
price, std_err, ci = monte_carlo_call(S=100, K=100, T=1, 
                                       r=0.05, sigma=0.20)
# Output: price=10.4432, CI=[10.4198, 10.4666]
```

MC price converges to BSM closed form as n_paths → ∞.
Prefer MC for path-dependent exotics where no closed form exists.

## Mathematical Foundation

All implementations derived from first principles:

- GBM solution derived via Maclaurin series expansion of the 
  stochastic exponential — original derivation published on 
  [Substack](https://substack.com/@ayomideakinola1?utm_source=share&utm_medium=android&r=5xlptl)
- N(d2) interpretation: risk-neutral probability S_T > K
- Ito drift correction -σ²/2 emerges from Jensen's inequality 
  E[exp(X)] > exp(E[X])

## Author

**Ayomide Akinola Babajide**  
Quantitative Developer | Options Pricing & Market Making  
[LinkedIn](www.linkedin.com/in/ayomide-a-62b28928b) • [GitHub](https://github.com/ay007008)






















