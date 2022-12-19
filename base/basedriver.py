from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basedriver():
    def __init__(self,driver):
        self.driver = driver
    def element_clickable(self, by_type,by_locator):
        wait= WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((by_type,by_locator)))
    def presence_elements(self, by_type,by_locator):
        wait= WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_all_elements_located((by_type,by_locator)))
