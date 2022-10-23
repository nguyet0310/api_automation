import logging
from utils.data_test import Data
from bases.post_request import PostRequest
from faker import Faker
from utils.log_util import Logger
from utils.route import Route
import pytest

log = Logger(__name__, logging.INFO)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


fake = Faker()


class TestSignup:
    @pytest.mark.parametrize(
        "name,job",
        [("morpheus", "leaser"), ("", ""), ("12345678", "0987654")],
    )
    def test_create_user_with_valid_data(self, name, job):
        payload = {"name": name, "job": job}
        r = PostRequest.send_post_request(self, Route.user_url, payload)
        assert r["name"] == name
        assert r["job"] == job
        assert r["id"] != ""

    def test_register_user_with_valid_data(self):
        payload = {"email": "eve.holt@reqres.in", "password": "QpwL5tke4Pnpja7X4"}
        r = PostRequest.send_register_request(self, Route.register_url, payload)
        assert r["id"] == 4
        assert r["token"] == "QpwL5tke4Pnpja7X4"

    @pytest.mark.parametrize(
        "email,password",
        [
            ("eve.holt2@reqres.in", "QpwL5tke4Pnpja7X4"),
            ("eve.holt@", "QpwL5tke4Pnpja7X4"),
            ("12345678", "QpwL5tke4Pnpja7X4"),
        ],
    )
    def test_register_user_with_invalid_data(self, email, password):
        payload = {"email": email, "password": password}
        r = PostRequest.send_invalid_register_request(self, Route.register_url, payload)
        assert r["error"] == "Note: Only defined users succeed registration"
