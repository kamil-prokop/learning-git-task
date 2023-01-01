lista_zakupow = dict
lista_zakupow = { 
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for shop, product in lista_zakupow.items():
    print("Idę do", shop, "i kupuję tam", product)