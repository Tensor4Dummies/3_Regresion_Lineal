# 3_REGRESIÓN_LINEAL

- [Introducción](#introducción)
- [Tipos de Modelos de Regresión Lineal](#tipos-de-modelos-de-regresión-lineal)
	- [Regresión Lineal Simple](#regresión-lineal-simple)
	- [Regresión Lineal Múltiple](#regresión-lineal-múltiple)

## Introducción
La regresión lineal es una técnica estadística utilizada para medir la relación entre variables. Su interés radica en que el algoritmo que lo implementa no es complejo conceptualmente, y además se adapta a una amplia variedad de situaciones.  
Es un modelo matemático usado para aproximar la relación de dependencia entre una variable dependiente Y, las variables independientes Xi y un término aleatorio ε. Este modelo puede ser expresado como:
 ![formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/604ec4765565e5860d9642d5a1c83c21b2975fbe)  
Donde:  
![Y](https://wikimedia.org/api/rest_v1/media/math/render/svg/95734a78eb8407939c3496cbfd92763ced1e41e1): variable dependiente, explicada o regresando.  
![X](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7e2161077a4f6cdeb1efde7cc35f2ad56e1b271): variables explicativas, independientes o regresores.  
![B](https://wikimedia.org/api/rest_v1/media/math/render/svg/08d3571eb3197b3945aac52c103d9d93f3c1584b):  parámetros, miden la influencia que las variables explicativas tienen sobre el regrediendo.  
Donde ![B0](https://wikimedia.org/api/rest_v1/media/math/render/svg/40b42f71f244103a8fca3c76885c7580a92831c8) es la intersección o término "constante", las ![Bi](https://wikimedia.org/api/rest_v1/media/math/render/svg/6bcab0261faa0348dba736336a165863628b79a8) son los parámetros respectivos a cada variable independiente, y p es el número de parámetros independientes a tener en cuenta en la regresión.  

La regresión lineal se usa para hacer predicción de variables cuantitativas, principalmente, y, aunque pueda parecer una técnica simple, sigue estando vigente pues se puede aplicar de forma sencilla a multitud de problemas. Además, sirve como punto de entrada para definir técnicas más complejas y sofisticadas dentro del análisis de regresión.
## Tipos de modelos de Regresión Lineal
### Regresión Lineal Simple
![formula1](http://www.monografias.com/trabajos82/agresividad-infantil-ecuador/image004.jpg)
* Permite determinar cuales son los coeficientes b0 y b1 que relacionan linealmente la variable de entrada (X) con la variable de salida (Y).  
* El coeficiente b0 o constante es el valor que toma la variable de salida (Y) cuand la variable de entrada (X) vale 0.  
* El coeficiente b1 multiplica a la variable de entrada (X) y por tanto va a determinar la inclinación de la recta. A mayor b1 la recta tendrá una mayor inclinación y por tanto pequeños cambios en la variable de entrada (X) generan cambios grandes en la variable de salida (Y).  
  
![grafica1](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/350px-Linear_regression.svg.png) 
* Hay infinitas posibles rectas por lo que se necesita encontrar aquella que minimice las distancias entre los valores observados y los predichos por la ecuación.  
* Esta recta se obtiene mediante un proceso matemático conocido como mínimos cuadrados.  
  
### Regresión Lineal Múltiple  

* Sigue el mismo modelo que la regresión lineal simple solo que ampliamos la ecuación, en vez de tener una variable de entrada o predictora, tenemos multiples.  
* Esto nos va a ofrecer la ventaja de utilizar más información en la construcción del modelo y, consecuentemente, realizar estimaciones más precisas.

![RLMF](https://mnshankar.files.wordpress.com/2011/05/equation.gif)  
* En definitiva, y al igual que en regresión lineal simple, vamos a considerar que los valores de la variable dependiente Y han sido generados por una combinación lineal de los valores de una o más variables explicativas y un término aleatorio.  
* Los coeficientes son elegidos de forma que la suma de cuadrados entre los valores observados y los pronosticados sea mínima, es decir, que se va a minimizar la varianza residual.  
* Esta ecuación recibe el nombre de hiperplano, pues cuando tenemos dos variables explicativas, en vez de recta de regresión tenemos un plano.  
* Con tres variables explicativas tendríamos un espacio de tres dimensiones, y así sucesivamente.  
  
![RLMG](https://dlegorreta.files.wordpress.com/2015/09/regression_lineal.png)  



