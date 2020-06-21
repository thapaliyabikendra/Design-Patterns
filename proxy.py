import time

class Producer:
    """Resource intensive object to instantiate"""

    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet")

class Proxy:
    """middleman to provide access to object"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None
    
    def produce(self):
        """Check if producer is available"""
        print("""Checking if producer is avilable""")

        if self.occupied == "No":

            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy")

p = Proxy()

p.produce()

p.occupied = "Yes"
p.produce()