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
          M1-enteros-v1.json              # versión parcial conservada
          M1-enteros-v2.json              # versión activa completa
        lectura/
          L0-diagnostico-lector-v1.json
          L1-localizar-integrar-v1.json   # versión parcial conservada
          L1-localizar-integrar-v2.json   # versión activa completa
        mail/
          A0-ciudadania-digital-v1.json
          A1-autores-audiencias-atencion-v1.json
demo/
  lecciones-demo.html
tools/
  validate_content.py
```

Antes de publicar una unidad, ejecuta `python tools/validate_content.py`. El validador comprueba IDs, respuestas, rangos, estructura de interacciones y que los pesos de dominio de cada lección sumen 1.

## Estado actual

Las seis unidades activas están completas y listas para el motor: 48 microlecciones y 576 pantallas en total.

- M0 — Diagnóstico y puente desde primaria: 8 de 8.
- M1 — Enteros, orden y divisibilidad: 8 de 8, versión activa 2.0.0.
- L0 — Diagnóstico lector y propósito: 8 de 8.
- L1 — Localizar e integrar información: 8 de 8, versión activa 2.0.0.
- A0 — Ciudadanía digital, identidad y agencia: 8 de 8.
- A1 — Autores, audiencias y economía de la atención: 8 de 8.

Cada microlección tiene 12 pantallas: meta, diagnóstico breve, tres explicaciones o modelos, dos prácticas guiadas, cuatro evidencias independientes y cierre. Los pesos de dominio suman 1 por lección. El diagnóstico orienta apoyos; no etiqueta al estudiante ni bloquea el aprendizaje.

M0 recupera sentido numérico, cálculo, proporciones, patrones, medición, geometría, datos y azar. M1 desarrolla interpretación, orden, operaciones y argumentación con enteros y divisibilidad. L0 recupera propósito, fluidez, navegación, comprensión y evaluación inicial. L1 avanza desde palabras clave hasta integración entre fuentes y respuesta con evidencia. A0 trabaja identidad, huella, consentimiento, convivencia y agencia. A1 analiza procedencia, audiencias, propósitos, modelos de negocio, patrocinio, diseño de atención, emoción y decisiones informadas.

Los 64 estímulos activos de Lectura y MAIL son originales de Prepaso. Las simulaciones de MAIL usan únicamente perfiles, servicios y datos ficticios; no requieren cuentas, ubicación, contactos, fotografías ni experiencias personales del estudiante.

Estas secuencias son organizaciones editoriales de Prepaso alineadas al CNEB. MAIL también se alinea al primer borrador preliminar del marco PISA 2029 publicado por la OCDE en enero de 2026 y, como referencia complementaria, al marco de alfabetización en IA para educación escolar publicado por la OCDE y la Comisión Europea en junio de 2026. La alineación debe volver a versionarse cuando la OCDE publique una versión posterior del marco MAIL.

## Unidad 1 de Matemática

1. M1.01 Números con dirección.
2. M1.02 Orden y valor absoluto.
3. M1.03 Suma de enteros.
4. M1.04 Resta de enteros.
5. M1.05 Multiplicación y división.
6. M1.06 Operaciones combinadas.
7. M1.07 Múltiplos y divisores.
8. M1.08 Argumentar propiedades.

La versión parcial `M1-enteros-v1.json` se conserva para no romper enlaces ya publicados. El manifiesto apunta a `M1-enteros-v2.json`.

## Unidad 1 de Lectura

1. L1.01 Palabras clave.
2. L1.02 Dato relevante.
3. L1.03 Datos dispersos.
4. L1.04 Referentes.
5. L1.05 Secuencia temporal.
6. L1.06 Causa explícita.
7. L1.07 Lectura intertextual inicial.
8. L1.08 Respuesta con evidencia.

La versión parcial `L1-localizar-integrar-v1.json` se conserva para no romper enlaces ya publicados. El manifiesto apunta a `L1-localizar-integrar-v2.json`.

## Unidad 1 de MAIL

1. A1.01 ¿Quién habla?
2. A1.02 ¿Para quién?
3. A1.03 Propósitos.
4. A1.04 Modelos de negocio.
5. A1.05 Contenido patrocinado.
6. A1.06 Diseño para captar atención.
7. A1.07 Emoción y viralidad.
8. A1.08 Decisión informada.
