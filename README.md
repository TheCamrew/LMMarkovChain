# LMMarkovChain

### En qué consiste?

El uso de las cadenas de Markov en la generación de lenguaje se basan en los *n-grams*, puesto que, una vez conozemos que palabras suelen estar cerca de otras en un texto, podemos crear un modelo estadístico, y predecir de esta forma, qué palabras pueden aparecer a continuación.

Pueden existir de distintos órdenes según el número anterior de palabras que se tienen en cuenta para la predicción. Primer orden tendría en cuenta una palabra, segundo orden dos...

### Ventajas e Inconvenientes

#### Ventajas:

- Implementación simple ya que son fáciles de entender a la hora de generar texto.

- Requieren menos recursos computacionales en comparación a otros modelos más complejos.

- La velocidad de generación de texto es rápida.

- No requiere datos etiquetados para entrenar al modelo ya que se basa en la frecuencia  de aparición de la secuencia de palabras 

#### Desventajas:

- Falta de coherencia en el texto generado ya que el modelo no tiene comprensión del contenido.

- Es común que el texto sea repetitivo y carezca de variedad, ya que se fija en los datos con los que se ha entrenado.

- Para obtener un buen resultado hace falta un texto de tamaño considerable.

- Puede generar texto que no siga las reglas gramaticales correctas.

### Aplicaciones (viables)

- Sistemas de corrección de textos.

- Sugerencias en editores de textos (ejemplo práctico en teléfonos móviles).

- Análisis y simulación de secuencias de caracteres en criptografía.

# Instalación

```console
conda create -n markovify python=3.10
conda activate markovify
python install markovify
```

# Uso

```console
conda activate markovify
python *script a usar*
```
