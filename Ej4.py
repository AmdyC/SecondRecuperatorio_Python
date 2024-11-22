countries = ["Argentina","Brasil","China","Dinamarca","España",
            "Francia","Grecia","Honduras","India","Jamaica"]
newcountries=["Alemania","Bélgica","Cánada"]
countries[:3] = newcountries
del countries[-3:]
half = len(countries) // 2
countries[half:half] = ["Japón","Korea del Sur","Mongolia"]
print(countries)