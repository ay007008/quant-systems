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
