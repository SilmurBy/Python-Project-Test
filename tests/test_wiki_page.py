import pytest

from data.popularity_data import PopularityData
from pages.wiki_page import WikiPage


class TestWikiPage:
    TestPopularity = PopularityData.popularity
    wiki_page: WikiPage

    @pytest.mark.parametrize('popularity', TestPopularity)
    def test_example_search_city(self, driver, open_and_load_wiki_page, popularity):
        wiki_page = open_and_load_wiki_page
        wiki_page.element_is_visible(wiki_page.locators.ARTICLE_NAME)
        wiki_page.check_table_presence()
        wiki_page.collect_row_data()
        wiki_page.popularity_check(popularity)
