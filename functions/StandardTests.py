import time

from functions.Fill_Filters_and_Search import Fill_Filters_and_Search
from pageobjects.Quick_Search_PO import Quick_Search_PO


class StandardTests:
    def __init__(self):
        pass

    # checken of filters behouden blijven na klikken op zoek-button
    def filterCheck(self,browser, type, location, straal, koopprijsVan, koopprijsTot):

        tester = Fill_Filters_and_Search()
        time.sleep(2)
        tester.fill_Filters_and_Search(browser, type, location, straal, koopprijsVan, koopprijsTot)
        time.sleep(2)

        self.assertFilters(browser, type, location, straal, koopprijsVan, koopprijsTot)


    #  checken of laatste zoekresultaat correct is, door erop te klikken en te checken of filters behouden zijn.
    def lastSearchResult(self,browser, type, location, straal, koopprijsVan, koopprijsTot):

        tester = Fill_Filters_and_Search()
        time.sleep(2)
        tester.fill_Filters_and_Search(browser, type, location, straal, koopprijsVan, koopprijsTot)
        time.sleep(2)
        home = Quick_Search_PO()
        home.clickHome(browser)
        home.clickLaasteZoekOpdrachtLink(browser)
        time.sleep(2)

        self.assertFilters(browser, type, location, straal, koopprijsVan, koopprijsTot)

    def assertFilters(self, browser, type, location, straal, koopprijsVan, koopprijsTot):

        pagina = Quick_Search_PO()

        filterLocation = pagina.toVerifylocation(browser)
        filterStraal = pagina.toVerifyStraal(browser)
        locationValue = filterLocation.get_attribute("value")

        assert locationValue == location, "verwachte tekst is \"%s\", gevonden is \"%s\"" % (location, locationValue)
        assert straal in filterStraal.text, "verwachte tekst is \"%s\", gevonden is \"%s\"" % (
        straal, filterStraal.text)

        if (type == "Koop") or (type == "Huur"):
            filterKoopprijs = pagina.toVerifyFilter(browser)

            if (koopprijsVan == "€ 0") and (koopprijsTot == "Geen maximum"):
                assert filterKoopprijs == "empty", "Filter op prijs, terwijl er niet gefilterd is"
            if (koopprijsVan != "€ 0") or (koopprijsTot != "Geen maximum"):
                assert filterKoopprijs != "empty", "Geen filter op prijs, terwijl er wel gefilterd is"