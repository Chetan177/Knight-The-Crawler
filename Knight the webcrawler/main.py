import threading
from queue import Queue
from knight import Knight
from domain import *
from common import *

def runcrawler(proj_name,url):
    PROJECT_NAME = proj_name
    HOMEPAGE = url
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 16
    queue = Queue()
    Knight(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

    # Create threads
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=work)
            t.daemon = True
            t.start()

    # Jobs
    def work():
        while True:
            url = queue.get()
            Knight.crawl_page(threading.current_thread().name, url)
            queue.task_done()

    # New jobs
    def create_jobs():
        for link in to_set(QUEUE_FILE):
            queue.put(link)
        queue.join()
        crawl()

    # Crawl links
    def crawl():
        queued_links = to_set(QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            create_jobs()

    create_workers()
    crawl()

