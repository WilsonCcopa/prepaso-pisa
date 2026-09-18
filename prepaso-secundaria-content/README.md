# Prepaso Secundaria — contenido curricular

Contenido declarativo para el motor HTML de Prepaso en Creator24.

## Regla de arquitectura

- Existe un único motor HTML para toda la aplicación.
- Cada unidad se publica como un archivo JSON versionado.
- Las lecciones contienen datos y reglas de interacción; nunca JavaScript ejecutable.
- Los identificadores son estables y no deben reutilizarse para otra habilidad.
- Una unidad publicada conserva su URL. Las correcciones crean una versión nueva.

## Estructura

```text
content/
  manifest.json
  pe/
    secundaria/
      1/
        matematica/
          M0-diagnostico-puente-v1.json
          M1-enteros-v1.json
        lectura/
          L0-diagnostico-lector-v1.json
          L1-localizar-integrar-v1.json
        mail/
          A0-ciudadania-digital-v1.json
demo/
  lecciones-demo.html
tools/
  validate_content.py
```

Antes de publicar una unidad, ejecuta `python tools/validate_content.py`. El validador comprueba IDs, respuestas, rangos, estructura de interacciones y que los pesos de dominio de cada lección sumen 1.

## Estado actual

Las tres unidades iniciales están completas y listas para el motor: 24 microlecciones y 288 pantallas en total.

- M0 — Diagnóstico y puente desde primaria: 8 de 8.
- L0 — Diagnóstico lector y propósito: 8 de 8.
- A0 — Ciudadanía digital, identidad y agencia: 8 de 8.

Cada microlección tiene 12 pantallas: meta, diagnóstico breve, tres explicaciones o modelos, dos prácticas guiadas, cuatro evidencias independientes y cierre. Los pesos de dominio suman 1 por lección. El diagnóstico orienta apoyos; no etiqueta al estudiante ni bloquea el aprendizaje.

M0 recupera sentido numérico, cálculo, proporciones, patrones, medición, geometría, datos y azar. L0 recupera propósito, fluidez, navegación, información explícita, inferencia, idea principal, voz y evaluación inicial. A0 usa únicamente casos y perfiles ficticios para trabajar entorno digital, identidad, huella, audiencias, consentimiento, normas, pausa y bienestar.

Estas secuencias son organizaciones editoriales de Prepaso alineadas al CNEB. MAIL también se alinea al primer borrador oficial del marco PISA 2029 publicado por la OCDE; como ese documento está sujeto a revisión, la alineación debe versionarse cuando aparezca un marco posterior.

La unidad M1 tiene listas para desarrollo las primeras cinco de ocho microlecciones:

1. M1.01 Números con dirección.
2. M1.02 Orden y valor absoluto.
3. M1.03 Suma de enteros.
4. M1.04 Resta de enteros.
5. M1.05 Multiplicación y división.

M1.06–M1.08 permanecen declaradas como pendientes en el manifiesto. La secuencia es una organización editorial de Prepaso alineada a la competencia del CNEB «Resuelve problemas de cantidad»; no se presenta como un índice oficial obligatorio de MINEDU.

La unidad L1 de Lectura tiene listas sus primeras cinco de ocho microlecciones:

1. L1.01 Palabras clave.
2. L1.02 Dato relevante.
3. L1.03 Datos dispersos.
4. L1.04 Referentes.
5. L1.05 Secuencia temporal.

L1.06–L1.08 permanecen declaradas como pendientes. Lectura es una ruta especializada dentro del área oficial de Comunicación, alineada a la competencia «Lee diversos tipos de textos escritos en su lengua materna». Todos los estímulos de esta versión son textos originales de Prepaso.
