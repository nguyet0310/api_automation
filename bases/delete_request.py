import logging
import requests
import json
from utils.log_util import Logger

log = Logger(__name__, logging.INFO)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


class DeleteRequest:
    def send_delete_request(self, url, payload):
        log.logger.info("request is: " + str(payload))
        r = requests.delete(url, json=payload)
        return r
