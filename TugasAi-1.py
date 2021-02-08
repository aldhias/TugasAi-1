from sklearn import datasets

house_prices = datasets.load_boston()

print("xxxxxxxxxxxxxxxxxxxxxxx")
print("Output of Home Prices Data")
print("xxxxxxxxxxxxxxxxxxxxxxx")
print(house_prices.data)

print("xxxxxxxxxxxxxxxxxxxxxxx")
print("Output of Predicted Home Prices")
print("xxxxxxxxxxxxxxxxxxxxxxx")
print(house_prices.target)

digits = datasets.load_digits()

print("xxxxxxxxxxxxxxxxxxxxxxx")
print("Output of scikit-learn Array of Images")
print("xxxxxxxxxxxxxxxxxxxxxxx")
print(digits.images[4])