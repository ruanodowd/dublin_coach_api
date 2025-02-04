from typing import Dict, List
import requests

class BusClient:
    """Main client for interacting with the Dublin Coach API."""
    
    BASE_URL = "https://ticketbooking.dublincoach.ie/MobileAPI/MobileBooking"
    
    def __init__(self):
        """Initialize the Dublin Coach API client."""
        self.session = requests.Session()
    
    def _make_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Make a request to the API."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_journeys(self, from_stage: str, to_stage: str) -> Dict:
        """
        Get journey list between two stages.
        
        Args:
            from_stage: Name of the origin stage/stop
            to_stage: Name of the destination stage/stop
        
        Returns:
            Dictionary containing journey information
        """
        params = {
            "FromStageName": from_stage,
            "ToStageName": to_stage,
            "JourneyType": 0,
            "RouteID": 0,
            "JrEndStageID": 0,
            "IsStageSelection": 1
        }
        return self._make_request("GetJourneyList", params)
    
    def get_stops(self, from_stage: str = "") -> Dict:
        """
        Get list of available stops for a specific route.
        
        Args:
            from_stage: Optional filter for stops from a specific stage
        
        Returns:
            Dictionary containing stop information
        """
        params = {"FromStage": from_stage}
        return self._make_request("GetTrackToStageName", params)
    
    def get_intercity_stops(self) -> Dict:
        """
        Get list of all intercity stops available on the Dublin Coach network.
        
        Returns:
            Dictionary containing all intercity stop information
        """
        return self._make_request("GetStageName")
