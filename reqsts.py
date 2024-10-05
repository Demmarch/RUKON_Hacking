import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# urls = ['https://python.ru/post/1245/', 'https://mode.com/93', 'https://python.ru/post/95/', "https://www.odin.study/ru/s/"]
#
# keyword = 'h3'
#
# for url in urls:
#     response = requests.get(url)
#
#     if response.status_code==200:
#         if keyword in response.text:
#             print(f"Ключевое слово {keyword} найдено на старнице {url}, status code = {response.status_code}")
#         else:
#             print(f"Ключевое слово {keyword} не найдено на старнице {url}, status code = {response.status_code}")
#
#     else:
#         print(f"Не удалось получить доступ к странице {url}, status code = {response.status_code}")
#
int_url = set()
ext_url = set()

def valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def website_links(url):
    urls = set()
    # извлекаем доменное имя из URL
    domain_name = urlparse(url).netloc
    # скачиваем HTML-контент вэб-страницы
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href пустой тег
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # удалить параметры URL GET, фрагменты URL и т. д.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not valid_url(href):
            # недействительный URL
            continue
        if href in int_url:
            # уже в наборе
            continue
        if domain_name not in href:
            # внешняя ссылка
            if href not in ext_url:
                print(f"[!] External link: {href}, code {requests.get(href).status_code}")
                ext_url.add(href)
            continue
        print(f"[*] Internal link: {href}, code {requests.get(href).status_code}")
        urls.add(href)
        int_url.add(href)
    return urls

visited_urls = 0
def crawl(url, max_urls=15):
    # max_urls (int): количество макс. URL для сканирования
    global visited_urls
    visited_urls += 1
    links = website_links(url)
    for link in links:
        if visited_urls > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    crawl("https://newtechaudit.ru")
    print("[+] Total External links:", len(ext_url))
    print("[+] Total Internal links:", len(int_url))
    print("[+] Total:", len(ext_url) + len(int_url))