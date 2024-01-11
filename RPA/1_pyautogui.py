import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1.5)

pyautogui.click(x=-1235, y=45)
pyautogui.write("jornada-python2023@hashtagprog.com.br")
pyautogui.press("tab")
pyautogui.write("minha_senha")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("C://Users/Thiago/Jornada-Python/RPA/produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=-1243, y=-68)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(3000)
