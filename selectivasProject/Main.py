#simple
a = 33
b = 200

if b > a:
    print(b,"es mayor que",a)

#doble
y = 200
z = 333

if y > z:
    print(y,"es mayor que",z)
else:
    print(y,"no es mayor que",z)

#multiples
l = 200
j =  207
if a > b:
    print(l,"es mayor que",j)
elif l < j:
    print(l,"es menor que",j)
else:
    print(l,"es igual que",j)
#enlazados
x = 28
if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por emcima de 20")
#parametros end y sep
print("Estudiar los sabados ", end="")
print("es genial")

#print("Estudiar los sabados", end="")
#print("es genial")

print("Daniela","Luis","Carlos","Camila")#agrega espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#agrega una coma

print("Daniela","Luis","Carlos","Camila",sep="_", end="_curso_python")#implementacion end y sep



