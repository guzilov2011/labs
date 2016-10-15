from vkapi import *
from datetime import date, datetime
import collections
import matplotlib.pyplot as plt


def hash(x):
    str = ""
    for i in range(x):
        str += "#"
    return str


api = VkApi()

params = {'user_id': '152667880', 'fields': 'bdate'}

api.set_parameters(params)
api.method = "friends.get"

response = api.execute()

if not response or response == "unsupported":
    print("have some errors")
response = response['response']['items']

ages = {}
now = datetime.now().date()

for user in response:
    dat = user.setdefault('bdate', '').split(".")
    if len(dat) != 3:
        continue
    d = date(int(dat[2]), int(dat[1]), int(dat[0]))
    razn = now - d
    years = int(razn.days / 365)
    ages[years] = ages.setdefault(years, 0) + 1

ages = collections.OrderedDict(sorted(ages.items()))

hist = []
bins = []
flg, ax = plt.subplots()

for k, v in ages.items():
    print("{}: {}".format(k, hash(v)))
    bins.append(k)
    hist.append(v)
    ax.bar(bins, hist, 1)

#вывод на гистограмму
plt.xlabel('Years')
plt.ylabel('Number of friends')
plt.hist(hist, bins=bins)
plt.show()

