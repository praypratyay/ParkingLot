from models.models import *
from daos.daos import *
from exceptions.exceptions import *
from strategies.SpotAssignmentStrategy import *

class TicketService:
    gateDAO = None
    vehicleDAO = None
    ticketDAO = None
    parkingLotDAO = None
    spotAssignmentStrategy = None

    # Dependency Injection
    def __init__(self, gateDAO, vehicleDAO, ticketDAO, parkingLotDAO, spotAssignmentStrategy):
        self.gateDAO = gateDAO
        self.vehicleDAO = vehicleDAO
        self.ticketDAO = ticketDAO
        self.parkingLotDAO = parkingLotDAO
        self.spotAssignmentStrategy = spotAssignmentStrategy
    
    def generateTicket(self, vehicleNumber, vehicleType, gateID): 
        """STEPS
           1. Get Gate from GateID. Else throw an exception
           2. Check if Vehicle in DB, else add Vehicle 
           3. Need Parking Spot (Strategy)
           4. Ticket Generation
        """

        gate = self.gateDAO.findGatebyID(gateID)
        if gate is None:
            raise InvalidGateException("Gate Object is None")
        
        vehicle = self.vehicleDAO.findVehicle(vehicleNumber)
        if vehicle is None:
            # This can also be done by 
            vehicle = Vehicle()
            vehicle.vehicleNumber = vehicleNumber
            vehicle.type = vehicleType
            vehicle = self.vehicleDAO.save(vehicle)

        parkingLot = self.parkingLotDAO.getParkingLotfromGate(gate)
        parkingSpot = self.spotAssignmentStrategy.findSpot(vehicleType, parkingLot, gate)

        if parkingSpot is None:
            raise NoAvailableSpotException("No empty spots found")
    
        ticket = Ticket()
        ticket.parkingSpot = parkingSpot
        ticket.entryTime = "DATE"
        ticket.gate = gate
        ticket.vehicle = vehicle
        ticket.operator = gate.currentOperator

        return self.ticketDAO.save(ticket)