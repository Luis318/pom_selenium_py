import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones():
    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url, tiempo):
        self.driver.get(url)
        print("Página abierta: "+ str(url))
        self.driver.maximize_window()

        t = time.sleep(tiempo)
        return t

    def tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t
    
    def textXpath(self, xpath, texto, tiempo):
        val = self.driver.find_element(By.XPATH, xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(tiempo)
        return t
    
    def textID(self, id, texto, tiempo):
        val = self.driver.find_element(By.ID, id)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(tiempo)
        return t
    
    #valida y busca el elemento usando su xpath
    def textoValidarXpath(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} ".format(xpath, texto))
            t = time.sleep(tiempo)
            return t            

        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible")
    
    #devuelve un True si encuentra el elemento, False si no lo encuentra
    def validarXpath(self, xpath):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            result = val.is_displayed()
            return result
        
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento")
            
            return False
    
    def clickXpath(self, xpath, tiempo):
        if(self.validarXpath(xpath)):
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
        else:
            print("Elemento no encontrado")

        t = time.sleep(tiempo)
        return t
    
    def click_xpath_validar(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Clic en {}" .format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento")
            
    
    def select_xpath_text(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            val.select_by_visible_text(texto)
            print("El campo seleccionado es {} ".format(texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)
            
    
    #utiliza cualquier metodo para enviar datos a un select
    def select_xpath_type(self, xpath, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)

            tipo.lower()
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)

            print("El campo seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)
              
    
    def upload_xpath(self, xpath, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)

            print("Se carga la imagen {}" .format(ruta))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)
            
        
    def check_xpath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()

            print("Click en el elemento: {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento "+ xpath)

    def existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento "+ selector)
                return "No existe"
        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No encontro el elemento " + selector)
                return "No existe"
            

def existeCl(self,tipo,elemento, tiempo=0): 
        """
        Esta funcion retona el  strinf "existe" y "no existe"
        Este metodo permite clickear un elemento especificando su tipo de indicador y indicador unico
            tipo: xpath,id,css
            elemento: el identificador único del elemento segun el tipo seleccionado
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.XPATH, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"
        elif(tipo.lower()=="id"):
            """
            Este metodo pide el id del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.ID, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"
        elif(tipo.lower()=="css"):
            """
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"
            
