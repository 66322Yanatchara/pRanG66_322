
Project Structure
=================

|-- requirements.txt
|-- docker-compose.yml
|-- service_a
|   |-- grpc_server.py
|   |-- main.py
|   |-- proto
|       |-- user.proto
|-- service_b
|   |-- grpc_client.py
|   |-- main.py
|   |-- proto
|       |-- user.proto
|-- service_c
|   |-- main.py

System Explanation
==================
The project consists of 3 Microservices communicating via HTTP (REST) and gRPC.

1. Service A (BTS Member Service)
   - Function: Acts as the Database/Source of Truth for BTS Members.
   - Protocols: 
     - HTTP (Port 8000): Check status.
     - gRPC (Port 50051): Serves member details (Name, Birthday, Province) to other services.
   
2. Service B (Gateway Service)
   - Function: Acts as a Gateway for users to request member info.
   - Protocols:
     - HTTP (Port 8001): Receives GET requests from users.
   - Flow:
     [User] --HTTP GET /bts/{id}--> [Service B] --gRPC GetMember(id)--> [Service A]
                                                                         |
     [User] <---HTTP JSON Resp----- [Service B] <----gRPC Reply----------+

3. Service C (Region Service)
   - Function: Provides region information for provinces.
   - Protocols:
     - HTTP (Port 8002).

How to Run
==========
1. Ensure you have Docker and Docker Compose installed.
2. Open a terminal in the project folder (Prang66_322).
3. Run the command:
   docker-compose up --build

Expected Results
================
After the containers start successfully:

1. Request Member Info (Service B -> A):
   Open browser or Postman to: http://localhost:8001/bts/1
   - Result: JSON data for member ID 1 (RM).
     {
       "name": "RM",
       "birthday": "1994-09-12",
       "province": "Goyang"
     }

2. Check Service A Status:
   Go to: http://localhost:8000/
   - Result: {"service": "A", "status": "ok"}

3. Check Service C Region Info:
   Go to: http://localhost:8002/region/Daegu
   - Result: {"province": "Daegu", "region": "North Gyeongsang"}
