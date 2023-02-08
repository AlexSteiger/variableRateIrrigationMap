#!/usr/bin/python3

#Create the layer and the store on GeoServer (Updating the layer is not possible):
import requests
postgreSQLTable = ['ru_soil_moisture','bursa_soil_moisture','ugent_soil_moisture']
url = 'https://geoportal.addferti.eu/geoserver/rest/workspaces/'

for i in range(0,3):
    datastore = 'current_' + postgreSQLTable[i]
    folder = 'current_'+ postgreSQLTable[i]
    try:
        with open(folder + '/current_' + postgreSQLTable[i]+'.zip', 'rb') as f:
            data = f.read()

        response = requests.put(
            url + 'geonode/datastores/' + datastore + '/file.shp',
            headers={'Content-type': 'application/zip'},
            data=data,
            verify=False,
            auth=('admin', 'addferti')
        )
        print(folder + '/current_' + postgreSQLTable[i] + ".zip uploaded" )
    except FileNotFoundError: 
        print(postgreSQLTable[i] + " table not found")
