#----------------------------------------------------------#
#File: habbit_tracker                                      #
#Programmed by: Luka Henig (luka.henig@gmail.com)          #
#Curse: 100 Days of Code udemy                             #
#Date: 06/03/2022                                          #
#Description: Programm to learn API post requests and      #
#headers, it shows a graph with pixela about coding hours  #
#----------------------------------------------------------#

#-----------------------IMPORTS--------------------------#
import requests
from datetime import date, datetime

#---------------------CONSTANTS--------------------------#
#This token is random and just for my pixela side, dont need to hide :D
TOKEN = "skgk528sjadntlxpyn345msmrcq1"
USERNAME = "lukahenig"
GRAPH_ID = "graph1"

#------------------VARIABLES----------------------------#
hours = input("How many hours did you code to day? ")
today = date.today()

#-------------------ENDPOINTS---------------------------#
pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_pixel_endpoint = f"{create_graph_endpoint}/{GRAPH_ID}"
update_pixel_endpoint = f"{graph_pixel_endpoint}/{today.strftime('%Y%m%d')}"

#--------------------PARAMS----------------------------#
headers = {
    "X-USER-TOKEN": TOKEN
}

create_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

create_graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

graph_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": hours,
}

update_pixel_params = {
    "quantity": hours,
}

#-------------------FUNCTIONS----------------------#
#only used once to create a user
#response =requests.post(url=pixela_endpoint, json=create_user_params)
#print(response.text)

#to create the graph
#response = requests.post(url=create_graph_endpoint, json=create_graph_params, headers=headers)
#print(response.text)

def create_new_pixel():
    responds = requests.post(url=graph_pixel_endpoint, json=graph_pixel_params, headers=headers)
    print(responds.text)

def update_pixel():
    responds = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
    print(responds.text)

def delete_pixel():
    responds = requests.delete(url=update_pixel_endpoint, headers=headers)
    print(responds.text)

create_new_pixel()