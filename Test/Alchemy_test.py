from Logic.Utils.Polarity import Bluemix
import json


print("Alchemy TEST")

bluemix = Bluemix()
text = "El director de Medicina Legal, Carlos Valdés, entregó un nuevo reporte sobre la muerte de Fernando Merchán, el vigilante del edificio donde las autoridades encontraron el cuerpo de la menor de siete años Yuliana Samboní, asesinada y abusada sexualmente el domingo 4 de diciembre."
c = bluemix.polarity(text)
c = json.loads(c)
print(c)

print("Personality Insights TEST")

c = bluemix.personality()
c = json.loads(c)
print(json.dumps(c,indent=2))