import requests
import json
from requests_api_pytest.common.api_request.request_config import RestAPIConfig
from requests_api_pytest.common.helper.create_url import make_url,rest_response_handle

class Request_API:
    @staticmethod
    def requests_get(config:RestAPIConfig):
        url=make_url(config)
        response=requests.get(url=url,headers=config.headers,timeout=config.timeout,
                              params=config.params,auth=config.auth)
        response,statuscode,json,text=rest_resonse_handlge(response)
        return response

    @staticmethod
    def requests_post(config: RestAPIConfig,json_data=None):
        url = make_url(config)
        response = requests.get(url=url,params=config.params,json=json_data, headers=config.headers,
                                allow_redirects=config.allow_redirects,timeout=config.timeout,
                                 auth=config.auth)
        response, statuscode, json, text = rest_resonse_handlge(response)
        return response

    @staticmethod
    def requests_put(config: RestAPIConfig,json_data=None):
        url = make_url(config)
        response = requests.get(url=url, params=config.params, json=json_data, headers=config.headers,
                                allow_redirects=config.allow_redirects, timeout=config.timeout,
                                auth=config.auth)
        response, statuscode, json, text = rest_resonse_handlge(response)
        return response

    @staticmethod
 def requests_del(config:RestAPIConfig,json_data=None):
        url=make_url(config)
        response = requests.get(url=url, params=config.params, json=json_data, headers=config.headers,
                                allow_redirects=config.allow_redirects, timeout=config.timeout,
                                auth=config.auth)
        response,statuscode,json,text=rest_resonse_handlge(response)
        return response


    @staticmethod
    open_json_file=(filename,mode):
    data_file=open(filename,mode)
    requests_json=json.loads(data_file.read())
    return requests_json

