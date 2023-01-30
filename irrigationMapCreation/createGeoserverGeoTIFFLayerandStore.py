#!/usr/bin/python3

#Create the layer and the store on GeoServer (Updating the layer is not possible):
import requests
name = ['VRI_ru_application_map','VRI_bursa_application_map','VRI_ugent_application_map']
url = 'https://geoportal.addferti.eu/geoserver/rest/workspaces/'


for i in range(0,3):
    file = name[i] + '.tif'
    datastore = name[i]
    print('with ' + file)
    try:
        with open(file,'rb') as f:
            data = f.read()
        
        response = requests.put(
            url + 'geonode/coveragestores/' + datastore + '/file.geotiff',
            headers={'Content-type': 'image/tiff'},
            data=data,
            verify=False,
            auth=('admin', 'addferti')
        )
        print(url + 'geonode/datastores/' + datastore + '/input/file.geotiff')
    except FileNotFoundError: 
        print(file + " not found")
       