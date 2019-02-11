from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

class Quick_Search_PO:

    def __init__(self):
        pass

    #Funda logo button
    def clickHome(self,browser):
        wait = WebDriverWait(browser, 10)
        home = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo")))
        home.click()

    # click link with name Koop, Huur, Nieuwbouw, Recreatie or Europa
    def clickLink(self, name, browser):
        wait = WebDriverWait(browser, 10)
        link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))
        link.click()

    #edit location and choose first (and best) suggestion
    def editlocationTextField(self, text, browser):
        wait = WebDriverWait(browser, 10)
        textField = wait.until(EC.visibility_of_element_located((By.ID, "autocomplete-input")))
        textField.click()
        textField.send_keys(text)
        time.sleep(1)
        list = browser.find_elements_by_xpath("//*[@id='autocomplete-list']/li")
        list[0].click()

    # return webelement to check in test
    def toVerifylocation(self,browser):
        wait = WebDriverWait(browser, 10)
        textField = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='autocomplete-input']")))
        return textField

    # return webelement to check in test
    def toVerifyLand(self, browser):
        wait = WebDriverWait(browser, 10)
        option = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.selected-option')))
        country = option.text
        return country

    # return message when there is no suggestion and location doesn't excist
    def toVerify_location_does_not_exist(self, text, browser):
        wait = WebDriverWait(browser, 10)
        textField = wait.until(EC.visibility_of_element_located((By.ID, "autocomplete-input")))
        textField.click()
        textField.send_keys(text)
        time.sleep(3)
        self.clickSearchButton(browser)
        time.sleep(1)
        message = browser.find_element_by_css_selector('h4.autocomplete-no-suggestion-message')
        return message.text

    #when type of search is europe, then the location must be choosen by a list
    def selectLocationLand(self, browser, country, ):
        wait = WebDriverWait(browser, 10)
        landenDropDown = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.selected-option')))
        landenDropDown.click()
        time.sleep(1)
        list = browser.find_elements_by_xpath("//*[@class='selectbox-list is-open']/li")
        for option in list:
            if option.get_attribute("id") == "Land-belgie":
                option.click()
                break

    # Straal can be "+ 0 km", "+ 1 km", "+ 2 km", "+ 5 km", "+ 10 km" of "+ 15 km" zijn. Nog enum maken
    def selectStraal(self, straal, browser):
        straalDropDown = Select(browser.find_element_by_id("Straal"))
        straalDropDown.select_by_visible_text(straal)

    # return webelement to check in test
    def toVerifyStraal(self, browser):
        straalDropDown = browser.find_element_by_id("Straal")
        return straalDropDown

    # koopprijsvan is  "Anders ""€ 0", "€ 50.000" dan steeds 25.000 omhoog tot "€ 400.000", dan steeds 50.000 omhoog tot
    def selectKoopprijsVan(self, prijsvan, browser):
        wait = WebDriverWait(browser, 10)
        koopprijsVanDropDown = wait.until(
            EC.visibility_of_element_located((By.ID, 'range-filter-selector-select-filter_koopprijsvan')))
        for option in koopprijsVanDropDown.find_elements_by_tag_name('option'):
            if option.text == prijsvan:
                option.click()
                break

    def selectHuurprijsVan(self, prijsvan, browser):
        wait = WebDriverWait(browser, 10)
        huurprijsVanDropDown = wait.until(
            EC.visibility_of_element_located((By.ID, 'range-filter-selector-select-filter_huurprijsvan')))
        for option in huurprijsVanDropDown.find_elements_by_tag_name('option'):
            if option.text == prijsvan:
                option.click()
                break

    # prijs 0-99999999 zonder puntjes
    def editKoopprijsVan(self, prijs, browser):
        editField = browser.find_element_by_css_selector('input.input-number-field[name="filter_KoopprijsVan"]')
        editField.send_keys(prijs)

    # koopprijsvan is  "Anders "€ 50.000" dan steeds 25.000 omhoog tot "€ 400.000", dan steeds 50.000 omhoog tot.. default geen maximum
    def selectKoopprijsTot(self, prijsTot, browser):
        wait = WebDriverWait(browser, 10)
        koopprijsTotDropDown = wait.until(
            EC.visibility_of_element_located((By.ID, 'range-filter-selector-select-filter_koopprijstot')))
        for option in koopprijsTotDropDown.find_elements_by_tag_name('option'):
            if option.text == prijsTot:
                option.click()
                break

    def selectHuurprijsTot(self, prijsTot, browser):
        wait = WebDriverWait(browser, 10)
        huurprijsTotDropDown = wait.until(
            EC.visibility_of_element_located((By.ID, 'range-filter-selector-select-filter_huurprijstot')))
        for option in huurprijsTotDropDown.find_elements_by_tag_name('option'):
            if option.text == prijsTot:
                option.click()
                break

    # prijs 0-99999999 zonder puntjes
    def editKoopprijsTot(self, prijs, browser):
        editField = browser.find_element_by_css_selector('input.input-number-field[name="filter_KoopprijsTot"]')
        editField.send_keys(prijs)

    # button with "Zoeken". Activates database search
    def clickSearchButton(self, browser):
        wait = WebDriverWait(browser, 10)
        buttonzoek = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button-primary-alternative[type="submit"]')))
        time.sleep(1)
        buttonzoek.click()

    #link when clicked the last search will be repeated
    def clickLaasteZoekOpdrachtLink(self, browser):
        time.sleep(4)
        link = browser.find_element_by_css_selector('a.link-alternative')
        link.click()

    #returns text of last search
    def toVerifyLaasteZoekOpdrachtLink(self, browser):
        wait = WebDriverWait(self, browser, 10)
        link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.link-alternative')))
        return link.text

    #check if filter button excists after filtering on price
    def toVerifyFilter(self, browser):
        present = self.check_exists_by_css(browser, 'button.button-applied-filter')
        if present == True:
            filter = browser.find_element_by_css_selector('button.button-applied-filter')
        else:
            filter = "empty"
        return filter

    #check if element excists
    def check_exists_by_css(self, browser, css):
        try:
            time.sleep(4)
            browser.find_element_by_css_selector(css)
        except NoSuchElementException:
            return False
        return True
