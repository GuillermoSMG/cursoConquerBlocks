DOLAR = 1.2;
DOLAR_SING = "$";
EURO_SIGN = "€";

euros = input("Cantidad de Euros que desea introducir: ")

dolar_conversion = round(float(euros) * DOLAR, 2);

tasa_management = round(dolar_conversion * 0.1, 2);

final_dolars_amount = round(dolar_conversion - tasa_management, 2);

print(f"Monto recibido: {EURO_SIGN}{euros},\nCambio en dolares: {DOLAR_SING}{dolar_conversion},\nLa tasa de gestión (10%) es de: {DOLAR_SING}{tasa_management},\nCantidad de dolares final: {DOLAR_SING}{final_dolars_amount}.")