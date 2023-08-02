from abc import ABC, abstractmethod
from models.enums import *

class ParkingLot:
    floors = []
    gates = []
    capacity = None

class Gate:
    id = None
    gateNumber = None
    status = None
    operator = None 
    type = None


class ParkingFloor:
    id = None
    floorNumber = None

class ParkingSpot:
    id = None
    number = None
    typesofVehicle = None
    status = None
    vehicle = None
    parkingFloor = None
 
class Vehicle:
    id = None
    vehicleNumber = None
    type = None 

class Operator:
    id = None 
    name = None 
    empID = None 

class Ticket:
    id = None 
    parkingSpot = None 
    entryTime = None 
    vehicle = None 
    gate = None 
    operator = None 

class Bill:
    id = None 
    exitTime = None 
    ticket = None 
    operator = None 
    amount = None 
    status = None 
    gate = None 
    onlinepaymentLink = None 
    payments = None 

class Payment:
    id  = None 
    mode = None 
    amount = None 
    status = None 
    refID = None 

