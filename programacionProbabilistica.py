from stochasticdp import StochasticDP

# Número de etapas + 1
number_of_stages = 4
# Lista de estados
states = [0, 1]
# Lista de decisiones
decisions = [0, 1, 2, 3, 4, 5]

# Inicializar el programa dinámico probabilístico
dp = StochasticDP(number_of_stages, states, decisions, minimize=True)

# Probabilidades de transición y contribuciones del estado n = 0
for t in range(number_of_stages - 1):
    for x in decisions:
        # donde dp.probability[m, n, t, x] es la probabilidad de pasar del estado n al estado m en la etapa t bajo la decisión x
        dp.probability[1, 0, t, x] = 0
        # donde dp.contribution[m, n, t, x] es la contribución inmediata resultante de pasar del estado n al estado m en la etapa t bajo la decisión x
        dp.contribution[1, 0, t, x] = 0
        dp.probability[0, 0, t, x] = 1
        dp.contribution[0, 0, t, x] = 0

# Probabilidades de transición y contribuciones del estado n = 0
for t in range(number_of_stages - 1):
    for x in decisions:
        if x > 0:
            K = 3
        else:
            K = 0
        dp.probability[0, 1, t, x] = 1 - (1/2)**x
        dp.contribution[0, 1, t, x] = K + x
        dp.probability[1, 1, t, x] = (1/2)**x
        dp.contribution[1, 1, t, x] = K + x
# Condiciones de contorno
# donde dp.boundary[n] es la condición límite para la función value-to-go en el estado n
dp.boundary[0] = 0
dp.boundary[1] = 16
# Resolver el programa dinámico
value, policy = dp.solve()
# value es un diccionario: value[t, n] es la función value-to-go en la etapa t y el estado n
print("Solucion de la etapa 0 para el estado 1: ",value[0,1])
