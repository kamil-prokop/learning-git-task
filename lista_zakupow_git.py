lista_zakupow = dict
lista_zakupow = { 
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for shop, product in lista_zakupow.items():
    print("Idę do", shop.capitalize(), "i kupuję tam", product.title())

counting = 0
for shop, product in lista_zakupow.items():
    for i in product:
        counting = counting + 1

print("W sumie kupuję", counting, "produktów.")