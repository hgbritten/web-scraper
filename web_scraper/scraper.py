import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
  return len(citations_needed)


def get_citations_needed_report(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
  for citations in citations_needed:
    print(f"Citation needed for '{citation.text}'")

total_count = get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Italy")
print(total_count)
# use a tag for citation