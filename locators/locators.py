from selenium.webdriver.common.by import By


class WikiPageLocators:
    ARTICLE_NAME = (By.XPATH, "//span[text()='Programming languages used in most popular websites']")
    TABLE_NAME = (By.XPATH,
                  "//caption[contains(text(),'Programming languages used in most popular websites')]/ancestor::table")
    ROWS = (By.XPATH, "./tbody/tr")
    WEBSITE = (By.XPATH, "./td[1]")
    POPULARITY = (By.XPATH, "./td[2]")
    FRONT_END = (By.XPATH, "./td[3]")
    BACK_END = (By.XPATH, "./td[4]")
    DATABASE = (By.XPATH, "./td[5]")
    NOTES = (By.XPATH, "./td[6]")
