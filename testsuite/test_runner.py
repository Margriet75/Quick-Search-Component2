import logging
import time

import pytest
from selenium import webdriver

from functions.StandardTests import StandardTests
from pageobjects.Quick_Search_PO import Quick_Search_PO

type = "Koop"
lokatie = "Nederland"
straal = "+ 0 km"
prijsVan = "€ 0"
prijsTot = "Geen maximum"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()

    driver.get('https://www.funda.nl')
    logging.info("Browser wordt geopend")
    yield driver
    driver.quit()

#flow testen zoeken: Indien ik zoek met bepaalde filters, wil ik dat het juiste resultaat getoond wordt

# koop met default filters: Indien ik geen filters wijzig, verwacht ik het totale aanbod in heel nederland

def test_koop(browser):

    test = StandardTests()

    test.filterCheck(browser, type, lokatie, straal, prijsVan, prijsTot)

#flow koop met  filters: Indien ik filters vul/wijzig, verwacht ik dat ik bij het zoekresultaat zie welke filters gebruikt zijn
def test_koop_filters(browser):

    test = StandardTests()

    type = "Koop"
    lokatie = "Ranonkelkade, Amsterdam"
    straal = "+ 1 km"
    prijsVan = "€ 50.000"
    prijsTot = "€ 500.000"

    test.filterCheck(browser, type, lokatie, straal, prijsVan, prijsTot)

#flow huur met  filters:Indien ik filters vul/wijzig, verwacht ik dat ik bij het zoekresultaat zie welke filters gebruikt zijn
def test_huur_filters(browser):

    test = StandardTests()

    type = "Huur"
    lokatie = "Amsterdam"
    prijsVan = "€ 500"
    prijsTot = "€ 600"

    test.filterCheck(browser, type, lokatie, straal, prijsVan, prijsTot)

#recreatiewoning met filters: Indien ik filters vul/wijzig, verwacht ik dat ik bij het zoekresultaat zie welke filters gebruikt zijn

def test_recreatie_filters(browser):

    test = StandardTests()

    type = "Recreatie"
    lokatie = "Amsterdam"
    straal = "+ 15 km"

    test.filterCheck(browser, type, lokatie, straal, prijsVan, prijsTot)

#flow europa belgie: Indien ik filters vul/wijzig, verwacht ik dat ik bij het zoekresultaat zie welke filters gebruikt zijn

def test_europa_filters(browser):

    type = "Europa"
    land = "België"
    pagina = Quick_Search_PO()

    pagina.clickLink(type, browser)
    pagina.selectLocationLand(browser,land)

    pagina.clickSearchButton(browser)

    locationOption = pagina.toVerifyLand(browser)
    assert locationOption == land, "verwachte tekst is \"%s\", gevonden is \"%s\"" % (land, locationOption)
#-------------------------------------------------------------------------------------------------
# flow laatste zoekopdrachttest: Wanneer ik een zoekopdracht doe met filters en na het zien van het resultaat op de home-button druk,
#  verwacht ik dat mijn laaste zoekopdracht zichtbaar is in een link en dat, wanneer ik op deze link druk, het verwachte zoekresultaat verschijnt.

# scenario met veel filters
def test_laatste_zoekopdracht_meer_Filter(browser):
    location = "Ranonkelkade, Amsterdam"
    straal = "+ 5 km"
    prijsVan = "€ 100.000"
    prijsTot = "€ 300.000"
    test = StandardTests()

    test.lastSearchResult(browser, type, location, straal, prijsVan, prijsTot)

# scenario met 1 filter
def test_laatste_zoekopdracht_1_Filter(browser):
    location = "Alfred Nobellaan, De Bilt"
    test = StandardTests()

    test.lastSearchResult(browser, type, location, straal, prijsVan, prijsTot)


#----------------------------------------------------------------------------------
#semantische test:
# Ik verwacht dat het mogelijk is om te zoeken op postcode en het juiste resultaat te krijgen
def test_postcode_filters(browser):

    test = StandardTests()

    lokatie = "Postcode 1035VJ"
    straal = "+ 1 km"

    test.filterCheck(browser, type, lokatie, straal, prijsVan, prijsTot)

# bij zoeken op een incorrecte postcodeverwacht ik een foutboodschap, wanneer ik op de "zoeken button druk": Ai.....boodschap

def test_postcodefout_filters(browser):

    lokatie = "1035vjk"

    pagina = Quick_Search_PO()

    pagina.clickLink(type,browser)
    time.sleep(2)
    foutboodschap = pagina.toVerify_location_does_not_exist(lokatie, browser)
    foutboodschap_exp = "Ai! Deze locatie kunnen we helaas niet vinden."

    assert foutboodschap == foutboodschap_exp, "verwachte tekst is \"%s\", gevonden is \"%s\"" % (foutboodschap_exp, foutboodschap, )

#nog te doen:

# Indien ik een spelfout maak bij invoeren lokatie verwacht ik suggesties, beginnend met boedschap: bedoel je soms....

# Wanneer ik handmatig een bedrag intoets bij koopsomvan en koopsomtot verwacht ik dit bedrag terug in het filter.
# Ik verwacht dat het niet mogelijk is om een negatieve waarde in te voeren bij koopsomvan en koopsomtot
# Ik verwacht dat ik een getal met punten in kan voeren (omdat de bedragen ook zo getoond worden) bij koopsomvan en koopsomtot
# => handmatig getest, niet volgens verwachting

# Ik verwacht een fotmelding indien koopsomTot lager is dan koopsomVan => Handmatig getest, is niet het geval, koopsomTot wordt wel rood
# Indien ik bij koopsomTot kies voor 200.000 verwacht ik geen resultaat van 200.000 +> handmatig getest, tot is eigenlijk tot en met
#----------------------------------------------------------------------------------------








