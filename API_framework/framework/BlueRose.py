import json
import traceback

import requests

from framework.Logger import Logger


class BlueRose:
    # 记录日志
    logger = Logger('blueRose.log', level='info').logger

    # 请求的返回结果
    response = ""

    def sendRequests(self, url, headers=None, method="post", data=None):
        """Send http requests to site

           :param url: Http url string.
           :param headers: requests headers param.
           :param method: requests method post or get.
           :param data: requests body param.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
       """
        try:
            requests.packages.urllib3.disable_warnings()
            if method == "post":
                self.logger.info("send post request to site " + url)
                response = requests.post(url, headers=headers, data=data, verify=False)
            elif method == "get":
                self.logger.info("send get request to site " + url)
                response = requests.get(url, headers=headers, data=data, verify=False)
            elif method == "put":
                self.logger.info("send put request to site " + url)
                response = requests.put(url, headers=headers, data=data, verify=False)
            elif method == "delete":
                self.logger.info("send delete request to site " + url)
                response = requests.delete(url, headers=headers, data=data, verify=False)
            else:
                self.logger.error("The requests method should be post or get")
                raise NameError("The requests method should be post or get")
            return response
        except Exception as e:
            print(traceback.format_exc())
            self.logger.error("The requests has been send,but happen error")

    def getCookiesValue(self, response, key):
        """Get cookies value from response headers

           :param response: Http response object.
           :param key: cookies key.
           :return: :cookies value
           :rtype: string
       """
        try:
            cookiesValue = requests.utils.dict_from_cookiejar(response.cookies)[key]
            self.logger.info("get cookies " + key + " is: " + cookiesValue)
            return cookiesValue
        except:
            self.logger.error("get cookies " + key + " error!!!")

    def getJsonFilesValue(self, response, jsonPath):
        """Get fields value from json object

           :param response: Http response object.
           :param jsonPath: json path of json object.
           :return: :fields value
           :rtype: string
       """
        try:
            filesValue = json.loads(response.content)[jsonPath]
            self.logger.info("get json fields value " + jsonPath + " is: " + str(filesValue))
            return filesValue
        except:
            self.logger.info("get json fields value " + jsonPath + " error!!!")
