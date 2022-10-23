import logging
from utils.data_test import Data
from bases.get_request import GetRequest
from faker import Faker
from utils.log_util import Logger
from utils.route import Route

log = Logger(__name__, logging.INFO)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


fake = Faker()


class TestGetRequest:
    def test_get_multiple_users_with_paging(self):
        response = GetRequest.send_get_request(
            self, Route.get_users_by_page_url, str(Data.page_number)
        )
        pages = response["total_pages"]
        assert pages == 2
        assert response["total"] == 12
        log.logger.info("response data is " + str(response["data"][0]))
        assert response["data"][0]["id"] == 7

    def test_get_no_users_with_paging(self):
        response = GetRequest.send_get_request(
            self, Route.get_users_by_page_url, str(Data.page_number_no)
        )
        pages = response["total_pages"]
        assert pages == 2
        assert response["total"] == 12
        assert response["data"] == []
