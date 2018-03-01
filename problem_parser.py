class Problem:
    def __init__(self, filepath):
        self.rows = 0
        self.columns = 0
        self.vehicles = 0
        self.rides = 0
        self.bonus = 0
        self.steps = 0

        self.rides = dict()

        with open(filepath, 'r') as f:
            for num, line in enumerate(f):
                items = line.split(" ")

                if num == 0:
                    self.rows = int(items[0])
                    self.columns = int(items[1])
                    self.vehicles = int(items[2])
                    self.rides = int(items[3])
                    self.bonus = int(items[4])
                    self.steps = int(items[5])
                else:
                    ride = dict()

                    ride['start_row'] = int(items[0])
                    ride['start_column'] = int(items[1])
                    ride['end_row'] = int(items[2])
                    ride['end_column'] = int(items[3])
                    ride['earliest_start'] = int(items[4])
                    ride['latest_finish'] = int(items[5])

                    self.rides[num - 1] = ride

        print("Parsed problem from file: %s" % filepath)
