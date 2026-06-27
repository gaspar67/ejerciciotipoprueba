items = {
    "MAGOOI":["Agonía de Escarcha", "Arma", "Legendaria", "Hielo"],
    "MAG002":["Anillo de Sauron", "Accesorio", "Epica", "Magia"],
    "MAG003":["Poción Curativa", "Consumible", "Comun", "Vida"],
    "MAG004":["Corona Nemesis ", "Armadura", "Legendaria", "Dragon"],
    "MAG005":["Baston Lunar de Lileath", "Arma", "Epica", "Hechizo"],
    "MAG006":["Cristal de Hielo", "Material", "Rara", "Hielo"],
}
inventario = {
    "MAGOOI": [5000,3],
    "MAG002": [2500,8],
    "MAG003": [100,50],
    "MAG004": [10000, 1],
    "MAG005": [3500,4],
    "MAG006": [800,0],
}

def stock_categoria(categoria):

    encontrado = False
    for codigo, datos in items.items():
        if datos[1].lower() == categoria.lower():
            print(f"{datos[0]} - stock: {inventario[codigo][1]}")
            encontrado = True
    if not encontrado:
        print("no encontrado")

def busqueda_precio(p_min,p_max):
    try:
        p_min = False
        p_max = False
        if p_min > 0:
            p_min = True
        if p_max > 0:
            p_max = True
    except ValueError:
        print("Debe ingresar valores enteros!!")
    

        

   

    
















while True:
    print("===ALDRIC EL COMERCIANTE ARCANO===")
    print("-"*20)
    print("1. Stock por categoria")
    print("2. Busqueda por precio")
    print("3. Actualizar precio")
    print("4. salir")
    
    try:
        op = int(input("ingrese opcion: "))
        if op > 4 or op < 1:
            print("ERROR, ingrese opcion valida")
    except ValueError:
        print("ERROR, ingrese opcion valida")
    if op == 1:
        categoria = input("ingrese categoria: ")
        stock_categoria(categoria)
    elif op == 2:
            p_min = int(input("ingrese precio minimo: "))
            p_max = int(input("ingrese precio maximo: ")) 
       

