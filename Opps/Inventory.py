import json

class Inventory:   #Employee class
    def __init__(self, price_per_kg, name, weight, totalPriceOfWeight ): # constructor
        self.price_per_kg = price_per_kg               # instantiating object
        self.name = name
        self.weight = weight
        self.totalPriceOfWeight = totalPriceOfWeight

    def display(self):
        return self.price_per_kg, self.name, self.weight, self.totalPriceOfWeight

Details = [Inventory({'rice': [
		    {
			"price_per_kg": 60,
			"name": "basmati",
			"weight": 7,
			"totalPriceOfWeight": 420
		    },
		    {
			"price_per_kg": 100,
			"name": "basmati",
			"weight": 5,
			"totalPriceOfWeight": 500
		    }
	    ]),
          Inventory("pulses": [
		    {
			"price_per_kg": 65,
			"name": "greens",
			"weight": 3,
			"totalPriceOfWeight": 195
		    }
	        ]),
          Inventory("wheats": [
		{
			"price_per_kg": 45,
			"name": "chakki_fresh",
			"weight": 5,
			"totalPriceOfWeight": 225
		}
	    ])
    ]

with open("Inventory.json", "w") as outfile:
    json.dump(Details, outfile)
