class ConsumersClass:
    """ Defines a two person consumer problem"""
    def __init__(self, omega_1=[0.8,1-0.8], omega_2=[0.3,1-0.3], alpha=1/3, beta=2/3):

        self.omega_A1 = omega_1[0] # A's endowment of good 1
        self.omega_A2 = omega_2[0] # A's endowment of good 2
        
        self.omega_B1 = omega_1[1] # B's endowment of good 1
        self.omega_B2 = omega_2[1] # B's endowment of good 2

        self.alpha = alpha # Calibration parameter
        self.beta = beta # Calibration parameter

        self.p1 = 1 # price for item 1 -> optimize w.r.t
        self.p2 = 1 # sets price for item 2 to numeraire
        #hej
        #cancer
        #fuck af. Vi prøver igen
    def utility_function(self, consumer):
        "defines the utility function, given who the consumer is"
        #remove code below and return consumer A and B utility as a tuple
        
        if consumer == "A": # goods and calibration for consumer A
            x_1 = self.omega_A1
            x_2 = self.omega_A2
            cal = self.alpha
            
            
        elif consumer == "B": # goods and calibration for consumer B
            x_1 = self.omega_B1
            x_2 = self.omega_B2
            cal = self.beta

        else:
            print("Error, consumer not defined")

        return x_1**cal * x_2**(1-cal) # utility calculation
    
    def goods_equilibrium(self):
        # Define the optimal solution for each consumer

        x_1Astar = self.alpha * (self.p1*self.omega_A1 + self.p2 * self.omega_A2)/self.p1
        x_2Astar = (1-self.alpha) * (self.p1 * self.omega_A2 + self.p2 * self.omega_A2)/self.p2
        x_1Bstar = self.beta * (self.p1*self.omega_B1 + self.p2 * self.omega_B2)/self.p1
        x_2Bstar = (1-self.beta) * (self.p1 * self.omega_B2 + self.p2 * self.omega_B2)/self.p2

        #return tuple of optimal goods.

#class ExchangeEconomyClass:
    
    # 1. Define Edgeworth box
    # 2. Calculate error in the market clearing condition
    # 3. What is the market clearing condition?
    # 4.a Find the allocation if only prices in P1 can be chosen
    # 4.b Find the allocation if any positive price can be chosen
    # 5.
