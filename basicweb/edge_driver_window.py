from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeServices
from finding_elements.env_file_path import edge_driver_path


class RunEdgeTestes():
    def test(self):
        edgeservice = EdgeServices(
            executable_path=edge_driver_path)
        driver = webdriver.Edge(service=edgeservice)

        driver.get("https://www.letskodeit.com")


runtests = RunEdgeTestes()
runtests.test()

