def generate_band_name():
    print("Oy! So you need a band name, eh? Let's get started!")
    city=input("tell me the name of the city you're from: ")
    pet=input("what's the name of your first pet? ")
    band_name = city + " " + pet
    print("Your band name could be: " + band_name)
generate_band_name()