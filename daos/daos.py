"""DAO (Data Access Object) is a pattern that acts as an abstraction between the database and the main application.
   It takes care of adding, modifying, retrieving, and deleting (CRUD) the data.
   DAOs is sometimes also referred as repositories.
"""

from models.models import *

# We can also use a IGateDAO as a parent class for handling different implementaions.
# Assuming that these repositories are map data structures.
class GateDAO:
    gatesDict = None
    
    def findGatebyID(self, gateID):
        if (gateID in self.gatesDict):
            return self.gatesDict[gateID]
        return None
    
class VehicleDAO:
    vehiclesDict = None
    lastSavedID = 0

    def findVehicle(self, vehicleNumber):
        for vehID in self.vehiclesDict:
            if (vehicleNumber == self.vehiclesDict[vehID].vehicleNumber):
                return self.vehiclesDict[vehID]
        return None
    
    def save(self, vehicle):
        vehicle.ID = self.lastSavedID + 1
        self.lastSavedID +=  1
        self.vehiclesDict[self.lastSavedID] = vehicle
        
        return vehicle
    
class TicketDAO:
    ticketsDict = None
    lastSavedID = 0

    def save(self, ticket):
        ticket.ID = self.lastSavedID + 1
        self.lastSavedID +=  1
        self.ticketsDict[self.lastSavedID] = ticket
        
        return ticket
    
class ParkingLotDAO:
    parkingLotsDict = None

    def getParkingLotfromGate(self, gate):
        for parkingLotID in self.parkingLotsDict():
            if (gate in self.parkingLotsDict[parkingLotID].gates):
                return self.parkingLotsDict[parkingLotID]