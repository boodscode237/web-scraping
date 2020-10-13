import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

links = soup.select(".storylink")
links2 = soup2.select(".storylink")

subtext = soup.select(".subtext")
subtext2 = soup2.select(".subtext")


mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        # getting the title from HackerNews
        title = links[idx].getText()
        # getting links of articles
        href = links[idx].get("href", None)
        # get the votes and display those with more than 99
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


res = create_custom_hn(mega_links, mega_subtext)
pprint.pprint(res)