"""Data Transfer Object (DTO) can be assumed as a data store. 
   It is used to transfer data between different layers.
   The only work of a Data Transfer Object is to get the data and transfer it. 
   In some situations, the data needs to be serialized or deserialized before sending it to the database or at the time of retrieving it from the database.
   That's why we use DTOs, DAOs to handle change in databases.
"""
class InvalidGateException(Exception):
    pass

class NoAvailableSpotException(Exception):
    pass