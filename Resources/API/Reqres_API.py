from robot.api.deco import keyword
import json
import sys
sys.path.insert(1,"/Users/plaad/PycharmProjects/APIAutomation1")
from core.EndpointKeywords import EndpointKeywords
from robot.libraries.BuiltIn import BuiltIn

from robot.libraries.BuiltIn import BuiltIn

class Reqres_API:
    endpointkeywords = EndpointKeywords()
    builtin = BuiltIn()
    @keyword("I hit endpoint to test the API")
    def TestAPI(self):
        dic = {}
        dic = self.builtin.get_variable_value("${dict}")
        # print(dic[0])
        # dic[0]
        # self.endpointkeywords.get(dic[0],params=)
        for ep,method in dic.items():
            print(ep)
            path = ep.split('?')
            print(path)
            path1 = "https://reqres.in" + path[0]
            # print(path[0])
            if method == "get":
                response = self.endpointkeywords.get(path1, params=path[1])
                print(response.content)
            else:
                break


