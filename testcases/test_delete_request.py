from ast import Del
import logging
from utils.log_util import Logger
from utils.route import Route
from utils.data_test import Data
from faker import Faker
from bases.delete_request import DeleteRequest

log = Logger(__name__, logging.INFO)
fake = Faker()
test_nick_name = fake.name()


class TestDelete:
    def test_get_user_profile(self):
        payload = {"name": "morpheus", "job": "leader2"}
        resp = DeleteRequest.send_delete_request(self, Route.delete_url, payload)
        assert resp.status_code == 204
