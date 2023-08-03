from dtos.dtos import *
from services.TicketService import *
from models.models import *
from models.enums import *

"""Note: 
   We dont require all atrtibutes of an object in our input data.
   Also no need to return all attributes in a response. 
   Never return complete internal models.
   Create separate classes for Requests/Responses(DTOs).
"""

class TicketController:
    ticketService = None

    def __init__(self, ticketService):
        self.ticketService = ticketService
    
    # def generateTicket(self, vehicleNumber, vehicleType, gateID):
    def generateTicket(self, request): 
        
        vehicleNumber = request.vehicleNumber
        vehicleType = request.vehicleType
        gateID = request.gateID
        
       
        ticket = Ticket()
        resp = GenerateTicketResponseDTO() 

        try:
            ticket = self.ticketService.generateTicket(vehicleNumber, vehicleType, gateID)
        except InvalidGateException as e:
            resp.responseStatus = ResponseStatus.FAILURE
            resp.responseMessage = e
            return resp
        except NoAvailableSpotException as e:
            resp.responseStatus = ResponseStatus.FAILURE
            resp.responseMessage = e
            return resp
        
        resp.responseStatus = ResponseStatus.SUCCESS
        resp.ticketID = ticket.ID  
        resp.operatorName = ticket.operator.name
        resp.parkingSpotNo = ticket.parkingSpot.number
       
        return resp
        