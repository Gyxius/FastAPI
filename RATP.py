import requests
import pprint

def get_time(retour=False):
    api_key = "hqxVduT45PIFFXTEn4i3P6QoNJBVC2D5"
    if retour:
        stop = 'STIF:StopPoint:Q:27080:'
    else:
        stop = "STIF:StopPoint:Q:27077:"
    line = "STIF:Line::C01123:"
    # stop = "STIF:StopPoint:Q:22973:" 
    # line = "STIF:Line::C01421:"


    headers = {
        "Accept": "application/json",
        "apiKey": api_key 
    }

    # Construct API URL with parameters (you can also use `params` instead)
    api_url = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"

    params = {
        "MonitoringRef": stop,
        "LineRef": line
    }

    # Send the request
    response = requests.get(api_url, headers=headers, params=params)

    # Print response JSON
    # print(response.status_code)
    # pprint.pprint(response.json())
    destination_json = response.json()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']
    time = destination_json['MonitoredCall']['ExpectedDepartureTime']
    # pprint.pprint(destination_json['MonitoredCall']['ExpectedDepartureTime'])

    from datetime import datetime
    from zoneinfo import ZoneInfo  # Available in Python 3.9+

    utc_time = datetime.fromisoformat(time.replace("Z", "+00:00"))
    paris_time = utc_time.astimezone(ZoneInfo("Europe/Paris"))
    hours = paris_time.strftime("%H:%M:%S")
    print(hours)
    return hours