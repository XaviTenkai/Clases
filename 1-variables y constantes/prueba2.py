
objetos = {
    "escudo de doran" : {

        "valor" : 200

    },

    "espada de doran" :{

        "valor" : 100

    },

    "espada de granizo" : {

        "valor" : 140

    },

    "cuchilla de ascuas" : {

        "valor" : 350

    },

    "preferencia" : {

        "valor" : 50

    },

    "anillo de doran" : {

        "valor" : 350

    },

    "sello oscuro" : {

        "valor" : 250

    },

       

}

campeon="Lee sin"

print(f"Hola {campeon}, dispongo de los siguientes objetos: ", end="" )

print(str(objetos.keys()).replace("{","").replace("}", "").replace("'", "").replace("[","").replace("]","").replace("dict_keys","").replace("(","").replace(")",""))

x = input(str("\n¿Qué deseas comprar?\n"))