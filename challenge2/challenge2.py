from logger.logger import logging
import requests
from helper.helper import verifyJson
import json
from challenge1.exception import _CommonBaseException

__author__='Vishal Sharma'
__package__='challenge2'
__name__ = 'challenge2'

class Challenge2:
    """
        Challenge2 support REST API CALL through config file
        initilizeVariables -
        runAllApiMethods  - This can call all operations [GET,PUT,POST,DELETE]
        :return
    """
    def __init__(self,config):
        self.config = config
        self.body=''
        self.initilizeVariables()

    def initilizeVariables(self):
        """
        Validate Obj Keys
        :param config:
        :return:
        """
        vJson = verifyJson(self.config)
        if vJson==-1:
            logging.error("Error - getToken",100,ex=True)
        self._vConfig = vJson
        self.body = self._vConfig.get('body')

    def getToken(self):
        """
            Get Token
        :return:
        """
        #TO DO can be extended
        return self._vConfig.get("token")

    def refreshToken(self):
        """
            Refresh Token
        :return:
        """
        #TO DO can be extended
        return self._vConfig.get("token")

    def getBaseUrl(self):
        """
            Get Base URL
        :return:
        """
        return self._vConfig.get("baseUrl")

    def concatInBaseUrl(self,pk):
        """
        Concat Primary Key
        :param pk:
        :return:
        """
        self._vConfig["newUrl"] = f'{self.getBaseUrl()}/{pk}'
        logging.info(f'New url {self._vConfig["newUrl"]}')

    def getNewUrl(self):
        """
        Get New URL with Endpoints
        :return:
        """
        if 'newUrl' in self._vConfig:
            return self._vConfig["newUrl"]
        logging.error("Set newUrl First",100,ex=True)

    def setBody(self,body):
        """
        Set Body
        :param body:
        :return:
        """
        self.body = body

    def getbody(self):
        """
        GET Body
        :return:
        """
        return self.body

    def patchBody(self,data):
        """
        Update Request Data
        :param data:
        :return:
        """
        if not isinstance(data,dict):
            logging.error(f'Only Dict is allowed, Recieved {data}',100,ex=True)
        self.body.update(data)

    def runAllApiMethods(self, url, method='GET', body=None, username=None, password=None, headers=None, retry=3):
        """
        Call ALL REST Methods
        :param url:
        :param method:
        :param body:
        :param username:
        :param password:
        :param headers:
        :param retry: Number of retries
        :return:
        """
        # Headers
        vheaders = {
            "Authorization": f'Bearer {self.getToken()}',
            "Content-Type": "application/json"
        }
        if headers is not None:
            vheaders.update(headers)

        for _ in range(retry):
            if method.upper() in ['POST']:
                response = requests.request(method, url, data=json.dumps(body), headers=vheaders)
            elif method.upper() in ['PUT', 'PATCH']:
                if body is None:
                    logging.error("body can't be None in case of [PUT, PATCH] REQUEST]", 100, ex=True)
                response = requests.request(method, url, data=json.dumps(body), headers=vheaders)
            elif method.upper() in ['DELETE']:
                response = requests.request(method, url, headers=vheaders)
            else:
                response = requests.request(method, url, headers=vheaders)

            if response.status_code == 401:
                logging.info("Token expired. Refreshing...")
                if self.refreshToken():
                    vheaders["Authorization"] = f'Bearer {self.getToken()}'
                    continue  # Retry the request with the new token
                else:
                    logging.error("Failed to refresh token.",100)
                    return -1
            elif response.status_code in [200, 201, 204]:
                logging.info(f'API Status Code {response.status_code} API URL {url}')
                if method =="DELETE":
                    return response.status_code
                logging.info('METHOD - {} , URL -{} , Response {}'.format(method,url,json.dumps(response.text)))
                return json.loads(response.text)
            else:
                if response.status_code == 422:
                    logging.info(f'BaseUrl {url} ,API Status Code {response.status_code} - Reason - {response.text}')
                    return response.text
                else:
                    logging.error(f'BaseUrl {url} ,API Status Code {response.status_code} Reason {response.text}', 100)
                return -1
        logging.error(f'Reached maximum retry limit ({retry}).')
        return -1

    def getPk(self,url):
        """
        Authenticate Users
        :return:
        """
        try:
            user = self.body['name'].lower()
            for item in self.runAllApiMethods(url=url):
                userName = item.get("name",None)
                if userName is not None:
                    if userName.lower() == user:
                        pk = item.get("id")
                        logging.info(f'PK is {pk}')
                        return pk
            return -1
        except Exception as error:
            _CommonBaseException(error)

    




