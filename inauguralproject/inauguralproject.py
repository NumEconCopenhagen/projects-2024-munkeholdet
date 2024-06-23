from types import SimpleNamespace
import numpy as np
class ExchangeEconomyClass:

    def __init__(self):
        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1 - par.w1A
        par.w2B = 1 - par.w2A

    def utility_A(self, x1A, x2A):
        
        return (x1A ** self.par.alpha) * (x2A ** (1 - self.par.alpha))

    def utility_B(self, x1B, x2B):
        
        return (x1B ** self.par.beta) * (x2B ** (1 - self.par.beta))

    def demand_A(self, p1):
        budget = self.par.w1A * p1 + self.par.w2A
        x1A = (self.par.alpha / p1) * budget
        x2A = ((1 - self.par.alpha) / 1) * budget  # p2 is the numeraire and equals 1
        return x1A, x2A

    def demand_B(self, p1):
        budget = self.par.w1B * p1 + self.par.w2B
        x1B = (self.par.beta / p1) * budget
        x2B = ((1 - self.par.beta) / 1) * budget  # p2 is the numeraire and equals 1
        return x1B, x2B

    def check_market_clearing(self, p1):
        
        x1A, x2A = self.demand_A(p1)
        x1B, x2B = self.demand_B(p1)

        # Calculate excess demand for both goods
        eps1 = x1A + x1B - 1  # Total endowment for good 1 is 1
        eps2 = x2A + x2B - 1  # Total endowment for good 2 is 1

        return eps1, eps2

def calculate_utility_and_allocations(economy, N=75):
    # Generate a range of prices
    p_values = np.linspace(0.5, 2.5, N)
    allocations = []
    for price in p_values:
        x1B, x2B = economy.demand_B(price)
        x1A, x2A = 1 - x1B, 1 - x2B
        allocations.append([x1A, x2A])
    return p_values, np.array(allocations)
