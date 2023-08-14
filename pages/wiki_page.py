from delayed_assert import delayed_assert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from data.table import Table
from data.table_row import TableRow
from locators.locators import WikiPageLocators


class WikiPage:
    locators = WikiPageLocators()
    table: Table

    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_table_presence(self):
        self.element_is_visible(self.locators.TABLE_NAME)

    def collect_row_data(self):
        table_list = []
        element_table = self.driver.find_element(*self.locators.TABLE_NAME)
        rows_list = element_table.find_elements(*self.locators.ROWS)
        for row in rows_list:
            table_list.append(TableRow(
                row.find_element(*self.locators.WEBSITE).text,
                row.find_element(*self.locators.POPULARITY).text,
                row.find_element(*self.locators.FRONT_END).text,
                row.find_element(*self.locators.BACK_END).text,
                row.find_element(*self.locators.DATABASE).text,
                row.find_element(*self.locators.NOTES).text
            ))
        self.table = Table(tuple(table_list))

    def popularity_check(self, popularity):
        work_table = self.table.get_table()
        for table_row in work_table:
            delayed_assert.expect(table_row.get_popularity() >= popularity,
                                  f"{table_row.get_website()}"
                                  + f" (Frontend:{table_row.get_front_end()}|Backend:{table_row.get_back_end()})"
                                  + f" has {str(table_row.get_popularity())}"
                                  + f" unique visitors per month. (Expected more than {popularity})")
        delayed_assert.assert_expectations()
