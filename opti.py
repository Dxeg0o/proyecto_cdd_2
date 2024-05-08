import gurobipy as gp

# Crear un modelo
m = gp.Model("ejemplo")

# Crear variables
x = m.addVar(lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS, name="x")
y = m.addVar(lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS, name="y")

# Agregar una restricción
m.addConstr(x + 2*y >= 1, "c0")

# Establecer la función objetivo
m.setObjective(x + y, gp.GRB.MAXIMIZE)

# Resolver el modelo
m.optimize()

# Imprimir resultado
if m.status == gp.GRB.OPTIMAL:
    print('Valor óptimo:', m.objVal)
    print('Valor de x:', x.x)
    print('Valor de y:', y.x)
else:
    print('El modelo no tiene solución óptima.')


    print('hola mundo')