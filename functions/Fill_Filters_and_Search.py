import time

from pageobjects.Quick_Search_PO import Quick_Search_PO


class Fill_Filters_and_Search:

    def __init__(self):
        pass

    def fill_Filters_and_Search(self, browser, type, location, straal, koopprijsVan, koopprijsTot):

        quick_Search = Quick_Search_PO()

        quick_Search.clickLink(type, browser)
        time.sleep(2)
        if location != "Nederland":
            quick_Search.editlocationTextField(location, browser)
        time.sleep(2)
        quick_Search.selectStraal(straal, browser)
        if (type == "Koop"):
            quick_Search.selectKoopprijsVan(koopprijsVan, browser)
            quick_Search.selectKoopprijsTot(koopprijsTot, browser)
        if (type == "Huur"):
            quick_Search.selectHuurprijsVan(koopprijsVan, browser)
            quick_Search.selectHuurprijsTot(koopprijsTot, browser)
        #if type == "Recreatie":
            #time.sleep(2)
        time.sleep(2)
        quick_Search.clickSearchButton(browser)