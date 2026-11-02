import json
import os
class StockInvalidError(Exception):
    def __init__(self, mensaje= "El stock no puede ser negativo"):
        super().__init__(mensaje)
class DispositivoEcologico : 
    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise StockInvalidError(
                f"{self.name}: stock invalido ({value})"
            )
        self._stock = value
    def gen_ficha_tecnica(self):
        return {
           "id_product": self.id_product,
            "name":self.name,
            "price":f"${self.price:.2f}",
            "stock":self.stock
        }
class PanelSolar(DispositivoEcologico):
    def __init__(self, id_product, name, price, stock, eficiencia,poten_w):
        super().__init__(id_product, name, price, stock)
        self.eficiencia = eficiencia
        self.poten_w = poten_w
    def gen_ficha_tecnica(self):
        ficha = ( super().gen_ficha_tecnica() )
        ficha.update({
            "type":"Panel Solar",
            "eficiencia": self.eficiencia,
            "poten_w": self.poten_w
            })
        return ficha
    
class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        data = []
        for dispositivo in lista_dispositivos:
            data.append(dispositivo.gen_ficha_tecnica())
        with open( ruta_archivo,"w",encoding="utf-8")as archivo:
             json.dump(data,archivo,ensure_ascii= False, indent=4
                       )

##Prueba con datos##
if __name__ == "__main__":
    print("--- Pruebas de catálogo EcoTech (Datos Crudos) ---")
    
    catalog = [
        {
            "id_product": "  P-101  ",
            "name": "Panel EcoVolt Pro",
            "price": "125000.00",        
            "stock": 15,
            "eficiencia": "21.5%",
            "poten_w": 450
        },
        {
            "id_product": "P-102",
            "name": "Panel EcoFail Test",
            "price": 85000.00,
            "stock": -4,                
            "eficiencia": "18%",
            "poten_w": 300
        },
        {
            "id_product": "P-103",
            "name": "Celda Solar Flex",
            "price": 45000.50,          
            "stock": 8,                  
            "eficiencia": "19.0%",
            "poten_w": 200
        } ,
        {
            "id_product": "P-104",
            "name": "Celda Solar ",
            "price": 35000.50,           
            "stock": 2,                  #
            "eficiencia": "17.0%",
            "poten_w": 220
        }
    ]

    lista_productos_validos = []

    for datos in catalog:
        print(f"\nIntentando registrar: {datos['name']}")
        try:
            panel = PanelSolar(
                id_product=datos["id_product"], 
                name=datos["name"], 
                price=datos["price"], 
                stock=datos["stock"], 
                eficiencia=datos["eficiencia"], 
                poten_w=datos["poten_w"]
            )
            ficha = panel.gen_ficha_tecnica()
            lista_productos_validos.append(panel)
            print(f" Éxito: {ficha}")
        except StockInvalidError as e:
            print(f" Error de Stock: {e}")
        except ValueError as e:
            print(f" Error de Formato (ValueError): {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")

    print("\n--")
  
    os.makedirs("Ejercicio_2", exist_ok=True)
    ruta_salida = "Ejercicio_2/catalogo_ecotech.json"
    
    try:
        GestorInventario.guardar_catalogo_json(lista_productos_validos, ruta_salida)
        print(f"Archivo guardado correctamente en: '{ruta_salida}'")
    except Exception as e:
        print(f" Error al escribir el archivo: {e}")