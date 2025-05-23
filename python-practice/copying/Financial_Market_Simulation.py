#  Scenario:
# You're simulating multiple trader agents. Each has:

# a portfolio (nested dict of assets),

# strategies (callables or config dicts),

# transaction history (list of dicts).

# You want to simulate market ticks where traders evolve, but retain the ability to rollback or branch simulations without affecting the original state.


import copy

class Trader:
    def __init__(self, name, portfolio, strategy):
        self.name = name
        self.portfolio = portfolio  # dict of {'AAPL': {'qty': 10, 'price': 150}, ...}
        self.strategy = strategy    # dict of rules
        self.history = []           # list of trades

    def execute_trade(self, symbol, qty, price):
        self.portfolio[symbol] = self.portfolio.get(symbol, {'qty': 0, 'price': 0})
        self.portfolio[symbol]['qty'] += qty
        self.portfolio[symbol]['price'] = price
        self.history.append({'symbol': symbol, 'qty': qty, 'price': price})

    def __repr__(self):
        return f"{self.name} Portfolio: {self.portfolio}"


# Default strategy and portfolio
default_strategy = {"type": "momentum", "threshold": 0.05}
default_portfolio = {
    "AAPL": {"qty": 10, "price": 150},
    "TSLA": {"qty": 5, "price": 700}
}

# Create base trader
original_trader = Trader("Alice", default_portfolio, default_strategy)

# Clone trader state for simulation
simulated_trader = copy.deepcopy(original_trader)

# Perform some simulation on the clone
simulated_trader.execute_trade("AAPL", 5, 160)
simulated_trader.execute_trade("GOOGL", 2, 2800)

print("Original:", original_trader)
print("Simulated:", simulated_trader)
