# Design Parking Lot (Low Level Design)

## **OVERVIEW**

Parking Lot is a typical place in a mall or airport or hospital, where people come to park their vehicles. They are issued a ticket for a spot at this place. Once they are done with their work, they pay the bill and exit the parking lot with their vehicle.
<p>
    <img src="parkinglot.jpg" width="1000" height="500" />
</p>

We dont want just entities for this. We want to build an entire software system thats takes hard coded input. Persist data in memory.

## Requirements and Clarifications

**Q) Is it an open parking lot or a closed parking lot with multiple floors?**

- _There are multiple floors._

**Q) Are there different kind of vehicles like Four/Two wheelers?**

- _Yes_

**Q) Are we allowing multiple two wheelers to be parked in the same spot?**

- _No, only one vehicle can be parked at one spot. Also, each spot has a dedicated set of vehicles that can be parked there._

**Q) Does it have multiple entry and exit gates?**

- _Yes._.

**Q) Do we want to have dynamic ticket pricing?**

- _Yes, the system should allow to easily change how fees are calculated depending upon type of vehicle, time of stay or both._

**Q) We will be assigning the spot via a ticket to the incoming vehicle at the time of entry itself and releasing that spot when it leaves through the exit gate. Does that make sense?**

- Yeah. There will be an operator that does this._

**Q) How are we assigning the parking spot? Do we want to have multiple ways of do this?**

- _Yes, keep it flexible._

**Q) Operator will calculate the bill amount at the exit time. Right?**

- _Yes._

**Q) Are there multiple mode of payments like Online/Cash/Pass?**

- _Our system supports online and offline payment only. No Pass._

## Interfaces - Classes - Attributes 

### ParkingLot
- Floors (list of ParkingFloor)
- Gates (list of Gate)
- Capacity

### Gate
- ID
- GateNumber
- Status
- Operator (person who is assigned to the Gate) 
- Type

### GateType
- ENTRY/EXIT

### GateStatus
- OPEN/CLOSED

### ParkingFloor
- ID
- FloorNumber
- ParkingSpots (list of ParkingSpot)

### ParkingSpot
- ID
- Number
- TypesofVehicle (list of VehicleType)
- Status
- Vehicle

### VehicleType
- CAR/BIKE/SUV/OTHERS

### SpotStatus
- FILLED/EMPTY/BLOCKED
 
### Vehicle
- ID
- VehicleNumber
- Type 

### Operator
- ID
- Name
- EmpID

### Ticket
- ID
- ParkingSpot
- EntryTime
- Vehicle
- Gate
- Operator (person who generated the Ticket) 

### Bill
- ID
- ExitTime
- Ticket
- Operator (person who issued the Bill) 
- Amount
- Gate
- OnlinePaymentLink
- Payments (list of Payment)

### Payment
- ID
- Mode
- Amount
- Status
- RefID

### PaymentMode
- ONLINE/OFFLINE

### PaymentStatus
- SUCCESSFULL/FAILED

### SpotAssignmentStrategy

- #### SpotAssignmentStrategy (SpotAssignmentStrategy)
- #### SpotAssignmentStrategy (SpotAssignmentStrategy)
- #### SpotAssignmentStrategy (SpotAssignmentStrategy)

### PriceCalculationStrategy

- #### PriceCalculationStrategy (PriceCalculationStrategy)
- #### PriceCalculationStrategy (PriceCalculationStrategy)
- #### PriceCalculationStrategy (PriceCalculationStrategy)


## Notes

- It is a human Parking Lot system. There is an operator which makes sure that vehicle is parked at right place. Ticket generation and bill generation is also done by an operator.

- We are supporting partial payments in which a bill can be paid through multiple modes.

- **ParkingSpot Calculation 1**: Hello

## HOW TO RUN?
```python 
python3 client.py
```
