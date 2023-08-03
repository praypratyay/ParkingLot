from enum import Enum

""" ENUMS """
class GateType(Enum):
    ENTRY = 1 
    EXIT = 2

class GateStatus(Enum):
    OPEN = 1 
    CLOSED = 2

class VehicleType(Enum):
    CAR = 1 
    BIKE = 2
    SUV = 3 
    OTHERS = 4

class ParkingStatus(Enum):
    FILLED = 1
    EMPTY = 2
    BLOCKED = 3

class PaymentMode(Enum):
    ONLINE = 1
    OFFLINE = 2

class PaymentStatus(Enum):
    SUCCESSFULL = 1
    FAILED = 2

class BillStatus(Enum):
    PAID = 1
    UNPAID = 2

class ResponseStatus(Enum):
    SUCCESS = 1
    FAILURE = 2

