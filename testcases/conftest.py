import os
import time
import pytest
import pytest_html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="class", autouse=True)  # @pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == "chrome" or "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "edge" or "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        print("enter valid browser")
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    # driver.save_screenshot('report\\screen.png')
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


#
# # @pytest.hookimpl(hookwrapper=True)
# @pytest.hookimpl(optionalhook=True)
# def pytest_runtest_make_report(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         xfail = hasattr(report, "wasxfail")
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://www.yatra.com/"))
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             # file_name = str (int(round(time.time()*1000)))+ ".png"
#             file_name = report.nodeid.replaced("::", "_") + ".png"
#             destination_File = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destination_File)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def pytest_html_report(report):
#     report.title = " my very own title"
