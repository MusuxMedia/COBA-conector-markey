# Detalle desarrollo Centro de Ojos Buenos Aires

En este caso el desarrollo es un simple conector con Markey, en el cual le consultamos si el paciente tiene cita.

El conector no tiene mucha ciencia, lo único particular es que al endpoint de Markey hay que mandarle el sexo del paciente, por lo que por cada consulta que se hace desdel el totem
se hacen dos consultas al endpoint de Markey. Si una de las dos devuelve datos del paciente se mandan al totem, sino se devueve 400.
