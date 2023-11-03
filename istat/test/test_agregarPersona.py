import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.django_db
def test_agregar_persona():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

    driver.find_element(By.ID, "id_username").send_keys("admin")
    driver.find_element(By.ID, "id_password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()

    driver.find_element(By.LINK_TEXT, "Personas").click()
    driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()

    driver.find_element(By.ID, "id_nombre").send_keys("Juan")
    driver.find_element(By.ID, "id_apellido_paterno").send_keys("Perez")
    driver.find_element(By.ID, "id_apellido_materno").send_keys("Rodriguex")

    driver.find_element(By.NAME, "_save").click()
    driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()

    driver.quit()