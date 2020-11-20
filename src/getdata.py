import json
import pandas as pd
from bs4 import BeautifulSoup

bf_reports = []

with open("./data/bigfoot_first100records.json") as f:
    for i in f:
        bf_reports.append(json.loads(i))

bf_soup = BeautifulSoup(bf_reports[0]["html"], "html.parser")
bf_tables = bf_soup
bf_csv = []
print(bf_soup)
for table in bf_soup.find_all("table"):
    # print(table)
    pass
# ufo_reports = []

# with open("./data/ufo_first100records.json") as f:
#     for i in f:
#         ufo_reports.append(json.loads(i))
