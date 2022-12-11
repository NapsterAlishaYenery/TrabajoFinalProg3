from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pytest import mark

@mark.parametrize("username,psw", [("AbreuHD", "Ismaelabreu27/"), ("falke", "fake")])
def test_login01(username, psw):
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@id="user-dashboard"]//ul/li[1]/a').click()
    driver.find_element(By.ID, 'username').send_keys(username);
    driver.find_element(By.ID, 'password').send_keys(psw);
    driver.find_element(By.ID, 'btnLogin').click()
    time.sleep(5)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/login/img{now}.png")
    assert driver.current_url == 'https://club.pokemon.com/us/pokemon-trainer-club/edit-profile/';

def test_busqueda02():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="searchInput"]').send_keys('Pikachu')
    driver.find_element(By.XPATH, '//*[@id="search"]').click()
    time.sleep(3)
    pokemon = driver.find_element(By.XPATH, '/html/body/div[4]/section[5]/ul/li/div/h5').text
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/busqueda/img{now}.png")
    assert pokemon == 'Pikachu'

def test_infoPokemon03():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[4]/section[5]/ul/li[1]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/infopokemon/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/pokedex/bulbasaur'

def test_descripcionpokemon04():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/bulbasaur")
    driver.maximize_window()
    time.sleep(5)
    info = driver.find_element(By.XPATH, '/html/body/div[4]/section[3]/div[2]/div/div[1]/p[2]').text
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/descripcion/img{now}.png")
    assert len(info) != 0

def test_aplicacionbtn05():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    driver.find_element(By.XPATH, '//li[@class="watch"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/aplicacionbtn/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/app'

def test_noticias06():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/ul/li[7]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/noticias/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/noticias-pokemon'

def test_sorprendeme07():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, 'shuffle').click()
    firsPoke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[1]/div/h5').text
    secondPoke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[2]/div/h5').text
    thirdPoke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[3]/div/h5').text
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/sorprendeme/img{now}.png")
    assert firsPoke != 'Bulbasaur' or secondPoke != 'Ivysaur' or thirdPoke != 'Venusaur'

def test_filtroSup08():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]').click()
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]//li[2]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/filtro/img{now}.png")
    time.sleep(4)
    poke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[1]/div/h5').text
    assert poke == 'Enamorus'

def test_filtroInferior09():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]').click()
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]//li[1]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/filtroInferior/img{now}.png")
    time.sleep(4)
    poke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[1]/div/h5').text
    assert poke == 'Bulbasaur'

def test_filtroAZ10():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]').click()
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]//li[3]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/filtroAZ/img{now}.png")
    time.sleep(4)
    poke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[1]/div/h5').text
    assert poke == 'Abomasnow'

def test_filtroZA11():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]').click()
    driver.find_element(By.XPATH, '//div[@class="flex"]//div[@class="custom-select-menu"]//li[4]').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/filtroZA/img{now}.png")
    time.sleep(4)
    poke = driver.find_element(By.XPATH, '//ul[@class="results"]/li[1]/div/h5').text
    assert poke == 'Zygarde'

def test_btnInicio12():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/pokedex/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//li[@class="home"]/a').click()
    time.sleep(3)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/inicio/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el'

def test_btnPokedex13():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(4)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH, '//li[@class="explore"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/btnPokedex/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/pokedex'

def test_btnCartas14():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH, '//li[@class="play"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/btnCartas/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/jcc-pokemon'

def test_btnTvPokemon15():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH, '//li[@class="attend"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/btnTv/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/episodios-pokemon'

def test_btnPlayPokemon16():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH, '//li[@class="trade"]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/playPokemon/img{now}.png")
    assert driver.current_url == 'https://www.pokemon.com/el/play-pokemon'

def test_QuienesSomos17():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="gus-wrapper"]/div/div[1]/div/ul/li[2]/a/img').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/quienessomos/img{now}.png")
    assert driver.current_url == 'https://corporate.pokemon.com/es-mx/'

def test_tempestadTemplada18():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="gus-wrapper"]/div/div[1]/div/ul/span/li[1]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/tempestadtemplada/img{now}.png")
    assert driver.current_url == 'https://tcg.pokemon.com/es-mx/'

def test_scarletViolet19():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="gus-wrapper"]/div/div[1]/div/ul/span/li[2]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/scarletviolet/img{now}.png")
    assert driver.current_url == 'https://scarletviolet.pokemon.com/es-mx/'

def test_united20():
    driver = webdriver.Chrome()
    driver.get("https://www.pokemon.com/el/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="gus-wrapper"]/div/div[1]/div/ul/span/li[3]/a').click()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./img/united/img{now}.png")
    assert driver.current_url == 'https://unite.pokemon.com/es-mx/'
