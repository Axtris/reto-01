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

walk_generator = os.walk(Fldr)
dir_entry = next(walk_generator)

dir_entry[1] + dir_entry[2]
[os.path.join(dir_entry[0], item) for item in dir_entry[1]+dir_entry[2]]
for entry in walk_generator:
    print(entry)

