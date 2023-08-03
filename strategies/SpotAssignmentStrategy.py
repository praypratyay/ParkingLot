from abc import abstractmethod
from models.enums import *

class SpotAssignmentStrategy:

    @abstractmethod
    def findSpot(self, vehicleType, parkingLot, entryGate):
        pass

class RandomSpotAssignmentStrategy(SpotAssignmentStrategy):

    def findSpot(self, vehicleType, parkingLot, entryGate):

        for parkingFloor in parkingLot.floors:
            for parkingSpot in parkingFloor.parkingSpots:
                if (parkingSpot.status == ParkingStatus.EMPTY and vehicleType in parkingSpot.supportedtypesofVehicle):
                    return parkingSpot

        return None 
    
class NearestSpotAssignmentStrategy(SpotAssignmentStrategy):

    def findSpot():
        return None
    
class ComplexSpotAssignmentStrategy(SpotAssignmentStrategy):

    def findSpot():
        return None
    