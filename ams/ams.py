class Ams:

    def time_to_collect(self, minute):
        return minute in list(range(0, 60, self.collect_interval))