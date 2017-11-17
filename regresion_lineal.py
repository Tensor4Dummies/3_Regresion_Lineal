'''
Ejemplo de regresión linial usando la libreria de TensorFlow

Autor: Jonathan Martinez Martinez
Projecto: https://github.com/Tensor4Dummies
Universidad de León (España)
'''


import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
rng = np.random

# Parametros
gradiente_aprendizaje = 0.1
iteraciones= 100
display_step = 1
meses = 6

######EJEMPLO MULTIPLES DATOS########
#np.random.seed(42)
#train_X = np.random.randint(low=1,high=49, size=500)
#np.random.seed(42)
#train_Y = np.random.randint(low=200,high=700, size=500)

#Definir los datos de entrenamiento (train)
train_X = np.asarray([1,2,3,4,5,6])
train_Y = np.asarray([7000,9000,5000,11000,10000,13000])
n_samples = train_X.shape[0] #tamaño del array


#Visualización de los datos
plt.plot(train_X, train_Y, "gx") #gx =verde x
#Para el ejemplo de ventas
#plt.xlabel("Mes") 
#plt.ylabel("Ventas")
#Para el ejemplo de aleatorio
plt.xlabel("Valor fijo")
plt.ylabel("Valares tomados")

plt.show()

#Creamos los Placeholders para actualizar  el gradiente
X = tf.placeholder("float", name="Mes")
Y = tf.placeholder("float", name="Ventas")

# Creamos las variables de entreno
W = tf.Variable(rng.randn(), name="peso")
b = tf.Variable(rng.randn(), name="parciales")

# Construimos el modelo lineal
pred = tf.add(tf.multiply(X, W), b)

# Calculamos la media del error cuadrado
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)

#  Calculamos el descenso de gradiente
optimizer = tf.train.GradientDescentOptimizer(gradiente_aprendizaje).minimize(cost)

# Inicializamos las variables
init = tf.global_variables_initializer()

# Comenzamos el entrenamiento
with tf.Session() as sess:

    # ejecutamos el inicializador
    sess.run(init)

    # Ajustamos datos de entrenamiento
    for epoch in range(iteraciones):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Mostramos en pantalla los registros por cada paso (log)
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimización finalizada!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

    # Mostramos resultados
    plt.plot(train_X, train_Y, 'ro', label='Datos Originales')
    
    #Para el ejemplo de ventas
    plt.xlabel("Mes")
    plt.ylabel("Ventas")

    #Para el ejemplo de aleatorio
    #plt.xlabel("Valor fijo")
    #plt.ylabel("Valares tomados")

    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Recta de regresion')
    plt.legend()
    plt.show()