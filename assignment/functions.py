#def greet(lang,name):
  #  if lang == "en":

   #     print(f"Hello {name}")

    #elif lang == "fr":

     #   print(f"Bonjour{name}")

    #else:

     #   print(f"Hola {name}")


#greet("en","prashanth")

data= [{
    "name":"prashanth",
    "age":25},
    {"name":"pras",
     "age":20}
]
def extract_age(details):
        age_1=(details[0]["age"])
        age_2=(details[1]["age"])
        return [age_1 , age_2]

ages=(extract_age(data))
print(ages)
