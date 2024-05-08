from gurobipy import *

# Crear un modelo
m = Model("ejemplo")

# Crear variables
x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
y = m.addVar(vtype=GRB.CONTINUOUS, name="y")
z = m.addVar(vtype=GRB.CONTINUOUS, name="z")


# Establecer la función objetivo
m.setObjective(x + 2*y + 3*z, GRB.MAXIMIZE)


# Agregar restricciones
m.addConstr(x + y + z <= 4)
m.addConstr(2*x + y <= 3)
m.addConstr(x + 2*z <= 1)

m.write("ejemplo.lp")
m.display()

# Resolver el modelo
m.optimize()
m.ObjVal
m.getVars()
