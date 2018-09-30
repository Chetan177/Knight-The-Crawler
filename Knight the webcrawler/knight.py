from urllib.request import urlopen
from seeker import LinkFinder
from domain import *
from common import *


class Knight:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Knight.project_name = project_name
        Knight.base_url = base_url
        Knight.domain_name = domain_name
        Knight.queue_file = Knight.project_name + '/queue.txt'
        Knight.crawled_file = Knight.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Knight.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_web_dir(Knight.project_name)
        create_webdata_files(Knight.project_name, Knight.base_url)
        Knight.queue = to_set(Knight.queue_file)
        Knight.crawled = to_set(Knight.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Knight.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Knight.queue)) + ' | Crawled  ' + str(len(Knight.crawled)))
            Knight.add_links_to_queue(Knight.gather_links(page_url))
            Knight.queue.remove(page_url)
            Knight.crawled.add(page_url)
            Knight.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Knight.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Knight.queue) or (url in Knight.crawled):
                continue
            if Knight.domain_name != get_domain_name(url):
                continue
            Knight.queue.add(url)

    @staticmethod
    def update_files():
        to_file(Knight.queue, Knight.queue_file)
        to_file(Knight.crawled, Knight.crawled_file)
