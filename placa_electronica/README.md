# Placa electrónica

Esta carpeta contiene los códigos de programación necesarios para crear el sistema, además de las conexiones para fabricar el circuito electrónico.

Vamos a encontrar las siguientes carpetas:

- **Arduino code**: Esta carpeta contiene los códigos de programación que se deben colocar en Arduino NANO usando el Arduino IDE. El código se hace utilizando la metodología de creaciones de clases de C++
  - Mindwave.ino: Este programa se va a encargar de procesar la informacion del sensor cerebral y comunicarle a la raspberry en que momento se detecto un doble pestañeo intencional del usuario
  - códigos_auxiliares_ejemplo: Aquí se encuentran códigos de programación que nos ayudaron a desarrollar el código *mindwave.ino*
- **PCB Ojo de Van Gogh**: Esta carpeta contiene los archivos de KiCAD del PCB junto a su esquemático, además cuentan con una carpeta de *huellas* con las dependencias que necesita
- **Raspberry code**: Esta carpeta contiene los códigos de programación que deben ser cargar en la Raspberry Pi Zero:
  - main.py: es el código que debe ser cargado y ejecutado en la raspberry. Se encarga de recibir la orden del Arduino NANO y generar la acción que el usuario elije previamente
  - clases: Aquí se encuentran las clases que se llaman en el main.py ya que usamos OOP
  - códigos_auxiliares_ejemplo: Aquí se encuentran códigos de programación que nos ayudaron a desarrollar el código *main.py y sus clases*

**WARNING**: Hay un .gitignore que tiene seteado que no debe subir al repositorio las **credenciales de Google Vision API** ya que es información sensible y cada uno debe colocar la credencial correspondiente al clonar el repositorio. **Si no se agrega esta credencial el main.py fallará**