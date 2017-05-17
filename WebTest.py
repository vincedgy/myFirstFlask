"""

"""
import unittest
import os
#import time
import psutil
from selenium import webdriver
#from subprocess import Popen

BASEDIR=os.getcwd()
CHROMEDRIVER='chromedriver'

def killProcByName(name):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if pinfo['name'] == CHROMEDRIVER:
                psutil.Process(pid=pinfo['pid']).terminate()
        except psutil.NoSuchProcess:
            pass

class WebTest(unittest.TestCase):

    driver = None
    p = None

    @classmethod
    def setUpClass(self):
        print('Setup Class')
        # Kill old chromedriver process
        killProcByName(CHROMEDRIVER)
        #self.p = Popen([os.path.join(BASEDIR,CHROMEDRIVER)])
        self.driver = webdriver.Chrome(os.path.join(BASEDIR,CHROMEDRIVER))

    @classmethod
    def tearDownClass(self):
        print('Teardown Class')
        self.driver.quit()
        #self.p.terminate()

    def setUp(self):
        print('Setup test')

    def tearDown(self):
        print('Tear down')

    # ------------------------------------

    def test_PollsHomePage(self):
        print('testPollsHomePage')
        self.driver.get('http://localhost:8000/polls/')
        element = self.driver.find_element_by_css_selector('body > h4')
        self.assertEquals(element.text, 'List questions')

    def test_ColoredLogs(self):
        print('testColoredLogs')
        self.driver.get('https://pypi.python.org/pypi/coloredlogs')
        element = self.driver.find_element_by_css_selector('#content > div.section > h1')
        self.assertEquals(element.text, 'coloredlogs 6.1')




if __name__ == '__main__':
    unittest.main()
