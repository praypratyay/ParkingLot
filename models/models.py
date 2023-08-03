from models.enums import *

class BaseModel:
    id = None
    createdAt = None
    lastUpdated = None

class ParkingLot(BaseModel):
    floors = None
    gates = None
    capacity = None

class Gate(BaseModel):
    gateNumber = None
    status = None
    currentOperator = None 
    type = None

class ParkingFloor(BaseModel):
    floorNumber = None
    parkingSpots = None

class ParkingSpot(BaseModel):
    number = None
    supportedtypesofVehicle = None
    status = None
    vehicle = None
    parkingFloor = None
 
class Vehicle(BaseModel):
    vehicleNumber = None
    type = None 

class Operator(BaseModel):
    name = None 
    empID = None 

class Ticket(BaseModel):
    parkingSpot = None 
    entryTime = None 
    vehicle = None 
    gate = None 
    operator = None 

class Bill(BaseModel):
    exitTime = None 
    ticket = None 
    operator = None 
    amount = None 
    status = None 
    gate = None 
#    onlinepaymentLink = None 
#    payments = None 

class Payment(BaseModel):
    mode = None 
    amount = None 
    status = None 
    refID = None
    bill = None
    time = None

