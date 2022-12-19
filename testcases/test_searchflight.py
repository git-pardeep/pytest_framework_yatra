import pytest
import softest
from utilities.Utils import utils
from ddt import ddt ,data,unpack,file_data
from pages.test_case2 import launchpage
@pytest.mark.usefixtures("setup")
@ddt
class TestYatra(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = launchpage(self.driver)
        # self.ut =utils()              # no need for log (log =utils.cutmer_logging() )is ok
    # @data(("Bangalore (BLR)","New York (NYC)","01/01/2023"),("Bangalore (BLR)","New York (NYC)","01/01/2023"))
    # @unpack
    # @file_data("..\\testdata\\testdata.Json")
    # @file_data("..\\testdata\\testdata.yaml")
    # @data(*utils.read_csv_data("C:\\pythonProject1\\project_pytest\\testdata\\testdata.csv"))
    # @unpack
    @data(*utils.read_excel_data("C:\\pythonProject1\\project_pytest\\testdata\\testdata.xlsx","Sheet1"))
    @unpack

    def test_yatra_trip(self, origin, depart, dat ):
        # YP  = launchpage(self.driver)
        self.lp.search_flight(origin, depart, dat)
        # self.lp.search_flight("Bangalore (BLR)","New York (NYC)","01/01/2023")



