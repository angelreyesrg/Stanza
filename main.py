#pip install stanza     Primero se instala la libreria desarrollada para python

import stanza
#stanza.install_corenlp() #Despues instalamos CoreNLP junto con los modelos predeterminados. Debemos tener tambien Java.

nlp = stanza.Pipeline('es') # Descarga del modelo Español. / Hay varios idiomas. Ej. 'es', 'en', 'fr'

doc = nlp("Estamos haciendo una prueba para la clase de Adquisicion y Tratamiento de informacion") # Ejecutar anotaciones sobre la oracion.

print(doc)