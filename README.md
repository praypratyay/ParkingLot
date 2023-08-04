# Design Parking Lot (Low Level Design)

## **OVERVIEW**

> Parking Lot is a typical place in a mall or airport or hospital, where people come to park their vehicles. They are issued a ticket for a spot at this place. Once they are done with their work, they pay the bill and exit the parking lot with their vehicle.
<p>
    <img src="parkinglot.jpg" width="1000" height="500" />
</p>

We dont want just entities for this. We want to build an entire software system thats takes hard coded input. Persist data in memory.

## Requirements and Clarifications

**Q) Is it an open parking lot or a closed parking lot with multiple floors?**

> _There are multiple floors._

**Q) Are there different kind of vehicles like Four/Two wheelers?**

> _Yes._

**Q) Are we allowing multiple two wheelers to be parked in the same spot?**

> _No, only one vehicle can be parked at one spot. Also, each spot has a dedicated set of vehicles that can be parked there._

**Q) Does it have multiple entry and exit gates?**

> _Yes._

**Q) Do we want to have dynamic ticket pricing?**

> _Yes, the system should allow to easily change how fees are calculated depending upon type of vehicle, time of stay or both._

**Q) We will be assigning the spot via a ticket to the incoming vehicle at the time of entry itself and releasing that spot when it leaves through the exit gate. Does that make sense?**

> _Yeah. There will be an operator that does this._

**Q) How are we assigning the parking spot? Do we want to have multiple ways of do this?**

> _Yes, keep it flexible._

**Q) Operator will calculate the bill amount at the exit time. Right?**

> _Yes._

**Q) Are there multiple mode of payments like Online/Cash/Pass?**

> _Our system supports online and offline payment only. No Pass._

## Classes - Attributes - Interfaces

### ParkingLot
- ID
- Floors (list of ParkingFloor)
- Gates (list of Gate)
- Capacity

### Gate
- ID
- GateNumber
- Status
- CurrentOperator (person who is assigned to the Gate) 
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
- SupportedTypesofVehicle (list of VehicleType)
- Status
- Vehicle
- ParkingFloor

### VehicleType
- CAR/BIKE/SUV/OTHERS

### ParkingStatus
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
- Status
- Gate
- OnlinePaymentLink
- Payments (list of Payment)

### Payment
- ID
- Mode
- Amount
- Status
- RefID
- Bill
= Time

### PaymentMode
- ONLINE/OFFLINE

### PaymentStatus
- SUCCESSFULL/FAILED

### BillStatus
- PAID/UNPAID

### SpotAssignmentStrategy

- #### RandomSpotAssignmentStrategy (SpotAssignmentStrategy)
- #### NearestSpotAssignmentStrategy (SpotAssignmentStrategy)
- #### ComplexSpotAssignmentStrategy (SpotAssignmentStrategy)

### FeesCalculatorStrategy

- #### FIXEDFeesCalculatorStrategy (FeesCalculatorStrategy)
- #### VEHICLEFeesCalculatorStrategy (FeesCalculatorStrategy)
- #### TIMEFeesCalculatorStrategy (FeesCalculatorStrategy)

### PaymentGatewayAdapter

- #### RazorPayPaymentGatewayAdapter (PaymentGatewayAdapter)
- #### PayUPaymentGatewayAdapter (PaymentGatewayAdapter)

## Notes

- It is a human Parking Lot system. There is an operator which makes sure that vehicle is parked at right place. Ticket generation and bill generation is also done by the operator currently at the gate.

- We are supporting partial payments in which a bill can be paid through multiple payments of different modes.

- ParkingSpot has a many to one _(m:1)_ relationship with ParkingFloor. So, we can store this relationship in ParkingSpot class directly. But in cases when the realtionship is _(m:m)_ and that said relationship has attributes, we use a relationship class.

## Schema Design (TABLES)

### STEPS to follow

- For every class representing entities, create a separate table.

- Use the primitive attributes of these classes as columns in the correspnding table.

- For non primitive attributes, find the cardinality of the relationship and represent it in the required table.

- For every enum, use a separate table.

### ParkingLot
| `ID` | `Capacity`
| --- | ---
| xx | xx 

### ParkingFloor
| `ID` | `FloorNo` | `LotID`
| --- | --- | ---
| xx | xx | xx

### Gate
| `ID` | `GateNo`  | `LotID` | `CurrentOperatorID` | `GateStatusID` | `GateTypeID`
| --- | --- | --- | --- | --- | ---
| xx | xx | xx | xx | xx | xx

### ParkingSpot
| `ID` | `SpotNo` | `parkingFloorID` | `ParkingStatusID` | `VehicleID`
| --- | --- | --- | --- | ---
| xx | xx | xx | xx | xx 

### Vehicles
| `ID` | `VehicleNo` | `VehicleTypeID`
| --- | --- | ---
| xx | xx | xx

### Operators
| `ID` | `Name` | `EmpID`
| --- | --- | ---
| xx | xx | xx

### Tickets
| `ID` | `EntryTime` | `GateID` | `VehicleID` | `OperatorID` | `ParkingSpotID`
| --- | --- | --- | --- | --- | --- 
| xx | xx | xx  | xx | xx  | xx 

### Bills
| `ID` | `ExitTime` | `Amount` | `OnlinePaymentLink` | `TicketID` | `GateID` | `OperatorID` | `BillStatusID`
| --- | --- | --- | --- | --- | --- | --- | ---
| xx | xx | xx | xx | xx | xx | xx | xx 

### Payments
| `ID` | `Amount` | `RefID` | `Time` | `BillID` | `PaymentModeID` | `PaymentStatusID`
| --- | --- | --- | --- | --- | --- | ---
| xx | xx | xx | xx | xx | xx | xx

### GateType
| `ID` | `Value`
| --- | ---
| xx | xx 

### GateStatus
| `ID` | `Value`
| --- | ---
| xx | xx 

### ParkingStatus
| `ID` | `Value`
| --- | ---
| xx | xx 

### VehicleType
| `ID` | `Value`
| --- | ---
| xx | xx 

### BillStatus
| `ID` | `Value`
| --- | ---
| xx | xx 

### PaymentStatus
| `ID` | `Value`
| --- | ---
| xx | xx 

### PaymentMode
| `ID` | `Value`
| --- | ---
| xx  | xx 


## HOW TO RUN?
```python 
python3 application.py
```
