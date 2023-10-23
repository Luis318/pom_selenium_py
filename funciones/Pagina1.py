import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Pagina1():
    def __init__(self, driver):
        self.driver = driver

    def funcion1(self):
        print("Uno dos tres :v")

    def check_xpath_multiple(self, *args):
        for num in args:
            try:
                
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("Click en el elemento {}".format(num))
                #t = time.sleep(tiempo)
                print(num)
                #return t
            except TimeoutException as ex:
                
                print(ex.msg)
                print("No se puede encontrar el elemento" + num)

    def texto_mixto(self, tipo, selector, texto, tiempo):
        if(tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento "+ selector)
                
        elif(tipo == "id"):
            try:
                val = val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.ID, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento "+ selector)


            


