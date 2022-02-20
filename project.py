import os

ruta = R"C:\Users\$USERNAME\Downloads"

Fldr = os.path.expandvars(ruta)

print(Fldr)

listar = Fldr

dir_list = os.listdir(listar)

print(dir_list)


