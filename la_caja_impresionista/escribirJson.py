import json

def escribir_Json (nombre_color):
        datos = {
            'color' : f'{nombre_color}'
        }

        json_str = json.dumps(datos)

        print(json_str)
