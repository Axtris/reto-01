import os

# Especifico la ruta para el usuario que este usando

ruta = R"C:\Users\$USERNAME\Downloads"

# Tendria que hacer un control para que determine el sistema operativo
# y que de ahi elija la variable a usar.

# Con os.path.expandvars reemplazo $USERNAME por el username correspondiente

Fldr = os.path.expandvars(ruta)

print(Fldr)

# Usando la variable anterior, inserto una variable que me permita listar lo que haya 
# en el directorio anterior. 

dir_list = os.listdir(Fldr)

print(dir_list)

print(Fldr)

