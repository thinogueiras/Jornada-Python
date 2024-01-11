from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import pandas

chrome_options = ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

driver.find_element(
    By.CSS_SELECTOR, 'input[id="email"]').send_keys("jornada-python2023@hashtagprog.com.br")
driver.find_element(
    By.CSS_SELECTOR, 'input[id="password"]').send_keys("minha_senha")

driver.find_element(By.CSS_SELECTOR, 'button[id="pgtpy-botao"]').click()

tabela = pandas.read_csv("C://Users/Thiago/Jornada-Python/RPA/produtos.csv")

for linha in tabela.index:
    driver.find_element(
        By.CSS_SELECTOR, 'input[id="codigo"]').send_keys(tabela.loc[linha, "codigo"])

    driver.find_element(
        By.CSS_SELECTOR, 'input[id="marca"]').send_keys(tabela.loc[linha, "marca"])

    driver.find_element(
        By.CSS_SELECTOR, 'input[id="tipo"]').send_keys(tabela.loc[linha, "tipo"])

    driver.find_element(
        By.CSS_SELECTOR, 'input[id="categoria"]').send_keys(str(tabela.loc[linha, "categoria"]))

    driver.find_element(
        By.CSS_SELECTOR, 'input[id="preco_unitario"]').send_keys(str(tabela.loc[linha, "preco_unitario"]))

    driver.find_element(
        By.CSS_SELECTOR, 'input[id="custo"]').send_keys(str(tabela.loc[linha, "custo"]))

    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
        driver.find_element(
            By.CSS_SELECTOR, 'input[id="obs"]').send_keys(obs)

    driver.find_element(
        By.CSS_SELECTOR, 'button[id="pgtpy-botao"]').click()

produtos_cadastrados = driver.find_elements(
    By.CSS_SELECTOR, '.pgtpy-container-tabela tbody tr')

qtde_produtos_cadastros = len(produtos_cadastrados)

print(
    f'\nQtde. de produtos de cadastrados nessa execução: {qtde_produtos_cadastros}')

driver.quit()
