import numpy


items = numpy.array([
    "Truffle Risotto",
    "Foie Gras",
    "Caviar Blinis",
    "Wagyu Beef",
    "Lobster Thermidor",
    "Duck à l'Orange",
    "Coq au Vin",
    "Oysters Rockefeller",
    "Beef Wellington",
    "Saffron Paella"])

nums = numpy.random.default_rng(2022)
prices = nums.normal(25, 5, 10)

fItems = items[prices > 25]
print(fItems)


final = numpy.where(prices > 20, 0, 5)
print(final)
