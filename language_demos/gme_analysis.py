from statistics import mean, median, stdev

prices = []

with open("gme_price.txt", "r") as price_file:

    for price in price_file:
        prices.append(float(price))


print(f"Max: {max(prices)}")
print(f"Min: {min(prices)}")
print(f"Mean: {mean(prices)}")
print(f"Median: {median(prices)}")
print(f"StDev: {stdev(prices)}")
