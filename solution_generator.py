class Solution:
    def __init__(self, problem):
        self.rides = dict()
        self.problem = problem

    def write(self, filepath):
        vehicles = sorted(self.rides.keys(), reversed=False)

        with open(filepath, 'w') as f:
            for vehicle in vehicles:
                f.write(str(vehicle))
                jouneys = self.rides[vehicle]

                for journey in jouneys:
                    f.write(' ' + str(journey))

        print("Written to file: %s" % filepath)

    def add_journey(self, vehicle, journey):
        if 0 <= vehicle < self.problem.vehicles:
            if 0 <= journey < self.problem.rides:
                if vehicle in self.rides.keys():
                    self.rides[vehicle].append(journey)
                else:
                    self.rides[vehicle] = [journey]
            else:
                print("Invalid journey num: %d (must be between 0 and %d)" % (journey, self.problem.rides))
        else:
            print("Invalid vehicle num: %d (must be between 0 and %d)" % (vehicle, self.problem.vehicles))
