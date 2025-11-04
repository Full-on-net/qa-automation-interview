Genera un script en Python en un único fichero que se encargue de llamar a una API pública: `https://open-meteo.com/en/docs`
El endpoint es accesible a traves de : https://api.open-meteo.com/v1/forecast y se puede ver un ejemplo de llamada y respuesta en : https://open-meteo.com/


Tendrá que hacer varias tareas:
1. Obtener, para una longitud y latitud dadas, el tiempo que hace actualmente. (las variables longitud y latitud pueden ser pasadas como argumentos al script)
2. Controlar posibles errores en la llamada a la API y manejarlos adecuadamente.
3. Implementar algún test unitario simple sobre el script usando el framework que se quiera.
4. Debe usarse anotaciones de Python (type hints).
5. Debe guardar los resultados de cada petición al script en un fichero separado que sea persistente e incremental.