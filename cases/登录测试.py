#!/usr/bin/env python
# coding=gbk

'''
Date: 2017-03-02 15:30
Author: johnny
'''

from selenium import webdriver
import unittest,time
from src.JzLogging import JzLogging
import ConfigParser

import sys
reload(sys)
sys.setdefaultencoding('GB18030')

class LoginTest_Error(unittest.TestCase):
    """ �豸�쳣��¼���ԣ������������ݵ�¼�Ϳ����ݵ�¼ """
    def setUp(self):
        self.logging = JzLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : ", time.strftime('%Y-%m-%d  %H:%M:%S  %A')
        #readerip =sys.argv[1]

        config = ConfigParser.ConfigParser()
        config.read("./config/readerConfig.ini")
        readerip = config.get("Device","ReaderIP")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get(readerip)
        self.logging.info("Opening browser 'Firefox' to base url : {}".format(readerip))
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ","Opening browser 'Firefox' to base url : {}".format(readerip)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.dataFalse = {
            "rfid": "Iis",
            "Rfid": "iis",
            "123": "456",
            u"����": "iis",
        }

        self.dataEmpty = ["","iis"]

    def testErrorFalse(self):
        ''' �������ݵ�¼ '''
        self.logging.info('Current Operation : Login Test Error False')
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",'Current Operation : Login Test Error False'
        for usernameF in self.dataFalse:
            self.inputData(usernameF,self.dataFalse[usernameF])
            messageF = self.message()
            if messageF == u"�û�����������������������룡":
                self.logging.info(u"username : '{}' password : '{}' {} ".format(usernameF,self.dataFalse[usernameF],messageF))
                self.logging.info("testErrorFalse Test OK")
                print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",u"username : '{}' password : '{}' {} ".format(usernameF,self.dataFalse[usernameF],messageF)
                print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ","testErrorFalse Test OK"
                self.driver.find_element_by_partial_link_text(u"ȷ��").click()
            else:
                raise ("testErrorFalse Test Faile!!!")

    def testErrorEmptyU(self):
        ''' �����ݵ�¼,�û���Ϊ�� '''
        self.logging.info('Current Operation : Login Test Error Empty with username')
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",'Current Operation : Login Test Error Empty with username'
        self.inputData(self.dataEmpty[0],self.dataEmpty[1])
        messageE = self.message()
        if messageE == u"�û��������벻��Ϊ��":
            self.logging.info(u"username : '{}' password : '{}' {} ".format(self.dataEmpty[0],self.dataEmpty[1], messageE))
            self.logging.info(u"testErrorEmpty Test OK")
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",u"username : '{}' password : '{}' {} ".format(self.dataEmpty[0],self.dataEmpty[1], messageE)
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ","testErrorEmpty Test OK"
            self.driver.find_element_by_partial_link_text(u"ȷ��").click()
        else:
            raise ("testErrorEmpty Test Faile!!!")

    def testErrorEmptyP(self):
        ''' �����ݵ�¼,����Ϊ�� '''
        self.logging.info('Current Operation : Login Test Error Empty with password')
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",'Current Operation : Login Test Error Empty with password'
        self.inputData(self.dataEmpty[1],self.dataEmpty[0])
        messageE = self.message()
        if messageE == u"�û��������벻��Ϊ��":
            self.logging.info(u"username : '{}' password : '{}' {} ".format(self.dataEmpty[1],self.dataEmpty[0], messageE))
            self.logging.info(u"testErrorEmpty Test OK")
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",u"username : '{}' password : '{}' {} ".format(self.dataEmpty[1],self.dataEmpty[0], messageE)
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ","testErrorEmpty Test OK"
            self.driver.find_element_by_partial_link_text(u"ȷ��").click()
        else:
            raise ("testErrorEmpty Test Faile!!!")

    def inputData(self,username,password):
        userName = self.driver.find_element_by_id('userName')
        userName.clear()
        userName.send_keys(username)
        time.sleep(1)
        passWord = self.driver.find_element_by_id('password')
        passWord.clear()
        passWord.send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('log_but').click()
        time.sleep(1)

    def message(self):
        messageE = self.driver.find_element_by_xpath("//div [@class='messager-body panel-body panel-body-noborder window-body']/div[2]").text
        return messageE

    def tearDown(self):
        self.driver.quit()
        self.logging.info("End time : {} ".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "***** End time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A'))
        self.logging.warning('#' * 70)

class LoginTest_Right(unittest.TestCase):
    """ �豸������¼���ԣ�������ͨ�û���¼�ͳ����û���¼ """
    def setUp(self):
        self.logging = JzLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A'))

        config = ConfigParser.ConfigParser()
        config.read("./config/readerConfig.ini")
        readerip = config.get("Device","ReaderIP")
        #readerip = "http://192.168.1.206"
        self.driver = webdriver.Firefox()
        self.logging.info("Opening browser 'Firefox' to base url : {}".format(readerip))
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ","Opening browser 'Firefox' to base url : {}".format(readerip)
        self.driver.implicitly_wait(5)
        self.driver.get(readerip)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.dataLogin = {
            "rfid": "iis",
            "superrfid": "debugiis",
                        }

    def testNormalLogin(self):
        ''' ��ͨ�û���¼ '''
        self.logging.info('Current Operation : Login Test Right Normal')
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",'Current Operation : Login Test Right Normal'
        try:
            self.opDevice("rfid","iis")
            self.logging.info(u"username : 'rfid' password : 'iis' ")
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ", "username : 'rfid' password : 'iis' "
            sur = self.driver.find_element_by_xpath("//*[@id='lef_but01']").text
            if sur == u"���ù���":
                self.logging.info("testNormalLogin Test OK")
                print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ", "testNormalLogin Test OK"
            else:
                self.logging.info("testNormaLogin Test Faile!!!")
                raise("testNormalLogin Test Faile!!!")
        except:
            raise("Current emvironment can't running NormalLogin")

    def testSuperLogin(self):
        """ �����û���¼ """
        self.logging.info('Current Operation : Login Test Right Super')
        print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ",'Current Operation : Login Test Right Super'
        try:
            self.opDevice("superrfid","debugiis")
            self.logging.info(u"username : 'superrfid' password : 'debugiis' ")
            print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ", "username : 'superrfid' password : 'debugiis'"
            sur = self.driver.find_element_by_xpath("//*[@id='lef_but01']").text
            if sur == u"���ù���":
                self.logging.info("testSuperLogin Test OK")
                print time.strftime('%Y-%m-%d  %H:%M:%S  %A') + " -  ", "testSuperLogin Test OK"
            else:
                self.logging.info("testSuperLogin Test Faile!!!")
                raise ("testSuperLogin Test Faile!!!")
        except:
            raise("Current emvironment can't running SuperLogin")

    def opDevice(self, username, password):
        ''' �����豸 '''
        userName = self.driver.find_element_by_id('userName')
        userName.clear()
        userName.send_keys(username)
        time.sleep(1)
        passWord = self.driver.find_element_by_id('password')
        passWord.clear()
        passWord.send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('log_but').click()
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()
        self.logging.info("End time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "***** End time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A'))
        self.logging.warning('#' * 70)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTest_Error("testErrorFalse"))
    suite.addTest(LoginTest_Error("testErrorEmptyP"))
    suite.addTest(LoginTest_Error("testErrorEmptyU"))
    suite.addTest(LoginTest_Right("testNormalLogin"))
    suite.addTest(LoginTest_Right("testSuperLogin"))
    unittest.TextTestRunner().run(suite)
