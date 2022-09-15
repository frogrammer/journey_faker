# Spatial Faker 

## It currently does this stuff:

* Within a radius of a point
* For a configurable number of people, waypoints and meetings
* And for scriptable stories

1. Models random people travelling to real world points of interest by feasible real world routes
2. Models a subset having a random meeting at a place and time
3. Calculates routes for a story where people travel to meet each other and/or through predetermined waypoints
4. Simulates signal strength for somebody who is travelling with equipment, and a set of people sending signals

## Key tech

* Azure Maps - find real world points of interest, routes and for some visualisations
* Faker - a python library to generate fake data, to generate mac addresses, SSIDs, names etc.

## Workflow

1. Configure parameters (.env)
2. Write "stories"
3. Generate people
4. Generate waypoints
5. Group people together to simulate routing and meeting
6. Generate "telemetry" of various forms

## How to run
```
python3 -m app.generator.[people, waypoints, routes, telemetry, signals]
```