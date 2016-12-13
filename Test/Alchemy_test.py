from Logic.Utils.Polarity import Bluemix
import json


print("Alchemy TEST")

bluemix = Bluemix()
text= "Não deixe para amanhã o que pode ser feito hoje."
c = bluemix.polarity(text)
c = json.loads(c)
print(c)