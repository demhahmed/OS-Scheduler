class process:
    def __init__(self, pid, AT, BT, PR):
        self.pid = pid
        self.arrival = AT
        self.running = BT
        self.priority = PR
        self.tat = 0.0 #turnaround time
        self.wtat = 0.0 #weighted turnaround time
        self.wait = 0.0   #wait time