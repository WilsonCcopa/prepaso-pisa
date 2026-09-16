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
          M1-enteros-v1.json
tools/
  validate_content.py
```

Antes de publicar una unidad, ejecuta `python tools/validate_content.py`. El validador comprueba IDs, respuestas, rangos, estructura de interacciones y que los pesos de dominio de cada lección sumen 1.

## Estado actual

La unidad M1 tiene listas para desarrollo las primeras cinco de ocho microlecciones:

1. M1.01 Números con dirección.
2. M1.02 Orden y valor absoluto.
3. M1.03 Suma de enteros.
4. M1.04 Resta de enteros.
5. M1.05 Multiplicación y división.

M1.06–M1.08 permanecen declaradas como pendientes en el manifiesto. La secuencia es una organización editorial de Prepaso alineada a la competencia del CNEB «Resuelve problemas de cantidad»; no se presenta como un índice oficial obligatorio de MINEDU.
