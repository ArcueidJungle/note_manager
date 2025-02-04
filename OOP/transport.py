class Transport:

    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def move(self):
        return 'Транспорт движется'


class Bus(Transport):

    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.route = route

    def move(self):
        return f"Автобус едет по маршруту {self.route}"

class Ship(Transport):

    def __init__(self, speed, capacity, max_depth  ):
        super().__init__(speed, capacity)
        self.max_depth = max_depth

    def move(self):
        return f"Корабль плывет на глубине до {self.max_depth} метров"

class Airplane(Transport):

    def __init__(self, speed, capacity, flight_number):
        super().__init__(speed, capacity)
        self.flight_number = flight_number

    def move(self):
        return f"Самолет {self.flight_number} взлетел"

bus = Bus(speed=60, capacity=50, route="Маршрут 12")
ship = Ship(speed=30, capacity=200, max_depth=100)
airplane = Airplane(speed=900, capacity=300, flight_number="SU-123")

transports = [bus, ship, airplane]
for transport in transports:
    print(transport.move())