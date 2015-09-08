# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Karel Barak"
__date__ = "$8.9.2015 12:13:46$"

import json
import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.dumps(eval(l))

if __name__ == "__main__":
    f = open("output.txt", 'a')
    number = 0
    for l in parse("reviews_Grocery_and_Gourmet_Food.json.gz"):
        data = json.loads(l)
        if (number < 500):
            if (data["overall"] == 5.0):
                f.write(str(int(data["overall"])) + '\t' + data["reviewText"] + '\n')
                number += 1
        else:
            break