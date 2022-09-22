import requests

class EndpointKeywords:

    def get(self,path,params=None):
        response = requests.get(url=path,params=params)
        return response

