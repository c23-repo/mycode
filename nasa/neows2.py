#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    print("Choose a seven date range for request")
    input_start = input("Choose a start date (example: 2019-11-11):  ")
    input_end = input("Choose a end date (example: 2019-11-18):  ")

    if input_start == "":
        startdate = "start_date=2019-11-11"
        end_date = "end_date=2019-11-18"
    else:
        startdate = (f"start_date={input_start}")
        end_date = (f"end_date={input_start}")
        

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + end_date  + "&" + nasacreds)

    
    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)
    largest = 0.0
    largest_name = ""
    closest = 0.0
    closest_name = ""

    for everydate in neodata["near_earth_objects"]:
        for asterdict in neodata["near_earth_objects"][everydate]:
            print(asterdict["name"])
            if asterdict["estimated_diameter"]["meters"]["estimated_diameter_max"] > largest:
                largest = asterdict["estimated_diameter"]["meters"]["estimated_diameter_max"]
                largest_name = asterdict["name"]
            if asterdict["close_approach_data"][0]["miss_distance"]["kilometers"] > largest:
                largest = asterdict["close_approach_data"][0]["miss_distance"]["kilometers"]
                closest_name = asterdict["name"]
    print(f"largest NEO was {largest_name} and the closeset was {closest_name}")

if __name__ == "__main__":
    main()

