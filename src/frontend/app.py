import streamlit as st
import requests
from streamlit_geolocation import streamlit_geolocation
import json
import pandas as pd


st.title("Outing Recommender")


st.write("Click the button below to get your location:")

location = streamlit_geolocation()
if location and location['latitude'] is not None:
    st.write("Latitude:", location["latitude"])
    st.write("Longitude:", location["longitude"])
else:
    st.write("Waiting for location...")

st.write("Click the button below to choose the type of needed places:")
options = ["school","university","travel_agency","supermarket" ,"mosque", "church","resturant", "bank","atm","bakery","beauty_salon","book_store","bicycle_store",
            "cafe","car_wash","clothing_store","shopping_mall","hospital","dentist","doctor","electronics_store"
            "gas_station","gym","laundry","pharmacy","parking","park","museum","library"]
search_type = st.pills("search_type", options , selection_mode="single")
st.write("Your outing option is  :", search_type)


distance = st.slider("How far you want to go",0, 10, 1)
st.write("Distance in KM :", distance)

count_of_results = st.number_input(
    "Insert a number of max needed places", value=None, placeholder="Type a number..."
)
st.write("The current number is ", count_of_results)


latitude=location['latitude']
longitude=location['longitude']   
distance_km=distance
search_type =search_type
count_of_results = count_of_results

payload = {
    "latitude": latitude,
    "longitude": longitude,
    "distance_km": distance_km,
    "search_type": search_type,
    "maxCrawledPlacesPerSearch": 30,
    "count_of_results" :count_of_results
}
if st.button("search"):

    response = requests.post(
        "http://127.0.0.1:5000/api/searchgooglemaps/",json=payload
    )

    # st.write(response.json())
    data = response.json()


    final_data = pd.DataFrame(data)    
    final_data=final_data[['title',
                            'categoryName',
                            'categories',
                            'OverallRank',
                            'distance_km',
                            'ReviewScore',
                            'reviewsCount',
                            'address',
                            'phone',
                            'url',
                            'floor',
                            'menu',
                            'reserveTableUrl',
                            'googleFoodUrl',
                            'openingHours',
                            'additionalInfo']]
   

    st.dataframe(final_data,column_config={
        "url": st.column_config.LinkColumn(
            "Google Maps",
            help="Open location in Google Maps",
            display_text="Open"
        )
    },hide_index=True)

#    