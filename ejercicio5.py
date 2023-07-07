"""
Mostrar por pantalla el nombre de las personas con más de $50 en esta tabla: https://the-internet.herokuapp.com/tables
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/tables"
MIN = 50


def get_dollars(d, fila):
    celda = d.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child(4)")
    texto_celda = celda.text
    return int(texto_celda.split(".")[0].lstrip("$"))

def get_persona (d, fila):
    celda = d.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child(2)")
    return celda.text

driver = webdriver.Chrome()
try:
    driver.get(URL)

    dollars = [
        get_dollars(driver, 1),
        get_dollars(driver, 2),
        get_dollars(driver, 3),
        get_dollars(driver, 4)
    ]

    filas_con_mas_de_50 = []
    for i in range(4):
        if dollars[i] > 50:
            filas_con_mas_de_50.append(i)

    personas =[
        get_persona(driver, 1),
        get_persona(driver, 2),
        get_persona(driver, 3),
        get_persona(driver, 4)
    ]

finally:
    driver.quit()

for fila in filas_con_mas_de_50:
    print(personas[fila])