from daos.daos import *
from strategies.SpotAssignmentStrategy import *
from services.TicketService import *
from controllers.TicketController import *


def main():
    """Object Creation Order (Automatically implemeted by Frameworks)
       1. DAOs
       2. Strategies
       3. Services
       4. Controller
    """
    gateDAO = GateDAO()
    vehicleDAO = VehicleDAO()
    ticketDAO = TicketDAO()
    parkingLotDAO = ParkingLotDAO()
    spotAssignmentStrategy = SpotAssignmentStrategy()
    
    ticketService = TicketService(gateDAO, vehicleDAO, ticketDAO, parkingLotDAO, spotAssignmentStrategy)

    ticketController = TicketController(ticketService)

    print("Application has STARTED")


main()