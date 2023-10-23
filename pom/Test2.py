import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from funciones.Funciones import Funciones
from funciones.Pagina1 import Pagina1
from excel.ExcelFun import *


class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
    
    def test1(self):
        driver = self.driver
        f = Funciones(driver)
        p = Pagina1(driver)
        f.navegar("https://www.saucedemo.com/", 2)
        f.textoValidarXpath("//input[contains(@id,'user-name')]", "Luis", 3)
        f.clickXpath("//input[contains(@id,'login-button')]",3)
        print(f.validarXpath("//input[contains(@id,'password2')]"))
        f.click_xpath_validar("//input[contains(@id,'login-button')]",3)
        p.funcion1()

    def test2(self):
        driver = self.driver
        f = Funciones(driver)
        f.navegar("https://testingqarvn.com.es/combobox/", 3)
        #f.select_xpath_text("//select[contains(@id,'wsf-1-field-53')]", "Mac", 2)
        f.select_xpath_type("//select[contains(@id,'wsf-1-field-53')]","text", "Mac", 2)
        f.select_xpath_type("//select[contains(@id,'wsf-1-field-53')]","value", "Windows", 2)
        f.select_xpath_type("//select[contains(@id,'wsf-1-field-53')]","index", "1", 2)

    def test3(self):
        driver = self.driver
        f = Funciones(driver)
        f.navegar("https://testingqarvn.com.es/upload-files/", 3)
        f.upload_xpath("//input[contains(@id,'wsf-1-field-94')]","C:\\Users\\sis\\Downloads\\examen ortografia.pdf",3)

    def test4(self):
        driver = self.driver
        f = Funciones(driver)
        f.navegar("https://web.archive.org/web/20180911154259/http://www.seleniumeasy.com/test/basic-checkbox-demo.html", 3)
        f.check_xpath("(//input[contains(@type,'checkbox')])[2]", 3)

    def test5(self):
        driver = self.driver
        f = Funciones(driver)
        p = Pagina1(driver)

        f.navegar("https://testingqarvn.com.es/combobox/", 3)
        p.check_xpath_multiple("//label[contains(@id,'wsf-1-label-50-row-1')]", "//label[contains(@id,'wsf-1-label-50-row-3')]")

        time.sleep(5)

    def test6(self):
        driver = self.driver
        f = Funciones(driver)
        p = Pagina1(driver)
        excel = ExcelFun(driver)

        f.navegar("https://demoqa.com/text-box",3)
        ruta = "C://Users//sis//Desktop//pythonTest.xlsx"
        filas = excel.getRowCount(ruta, "Hoja1")

        for r in range(2, filas+1):
            print(str(r)+ ">>>>>>:VVVVVVVV")
            nombre = excel.readData(ruta, "Hoja1", r, 1)
            email = excel.readData(ruta, "Hoja1", r, 2)
            dir1 = excel.readData(ruta, "Hoja1", r, 3)
            dir2 = excel.readData(ruta, "Hoja1", r, 4)

            f.textoValidarXpath("//input[contains(@id,'userName')]",nombre,2)
            f.textoValidarXpath("//input[contains(@id,'userEmail')]", email, 2)
            f.textoValidarXpath("//textarea[contains(@id,'currentAddress')]", dir1, 2)
            f.textoValidarXpath("//textarea[contains(@id,'permanentAddress')]", dir2, 2)
            f.click_xpath_validar("//button[contains(@id,'submit')]", 2)

            e=f.existe("id", "name",3)
            if(e=="Existe"):
                print("El elemento se inserto correctamente")
                excel.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se inserto")
                excel.writeData(ruta, "Hoja1", r, 5, "Error")



    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()
