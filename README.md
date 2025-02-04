# Dublin Coach API Client

A Python package for interacting with the Dublin Coach API. It's currently very barebones, but I'm hoping on snooping more Dublin Coach API endpoints in the future.

The library is made to compliment a project I'm working on to analyze how late the buses usually are at different times and locations 

Currently it seems the 310 buses are on average 14 minutes late from UL, which is fairly poor for a bus that runs every 30 minutes.

<!-- ## Installation

```bash
pip install -e .
```-->

## Quick Start

```python
from bus_api import BusClient

# Initialize the client
client = BusClient()

# Get journeys between two stops
journeys = client.get_journeys(
    from_stage="Dublin",
    to_stage="Limerick"
)

#Get list of available stops on a route
stops = client.get_stops(
    from_stage="Bunratty"
)

#Or use an Enum to get the stop names
from bus_api.stops import DublinCoachStop
stops = client.get_stops(
    from_stage=DublinCoachStop.BUNRATTY
)
```

## License

This project can be used and abused by anyone as long as it's legal. 
