import logging
import requests
import json
from utils.log_util import Logger

log = Logger(__name__, logging.INFO)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


class PostRequest:
    def send_post_request(self, url, payload):
        log.logger.info("request is: " + str(payload))
        r = requests.post(url, json=payload)
        response_content = json.loads(r.content)
        log.logger.info("response is: " + str(response_content))
        assert r.status_code == 201
        return response_content

    def send_register_request(self, url, payload):
        log.logger.info("request is: " + str(payload))
        r = requests.post(url, json=payload)
        response_content = json.loads(r.content)
        log.logger.info("response is: " + str(response_content))
        assert r.status_code == 200
        return response_content

    def send_invalid_register_request(self, url, payload):
        log.logger.info("request is: " + str(payload))
        r = requests.post(url, json=payload)
        response_content = json.loads(r.content)
        log.logger.info("response is: " + str(response_content))
        assert r.status_code == 400
        return response_content
