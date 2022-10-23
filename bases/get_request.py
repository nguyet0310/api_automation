import logging
import requests
import json
from utils.log_util import Logger

log = Logger(__name__, logging.INFO)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


class GetRequest:
    def send_get_request(self, url, param):
        log.logger.info("get request is: " + str(url) + str(param))
        r = requests.get(url + param)
        response_content = json.loads(r.content)
        log.logger.info("response is: " + str(response_content))
        assert r.status_code == 200
        return response_content
