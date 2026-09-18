"""Validación mínima del contrato de contenido de Prepaso Secundaria."""

from __future__ import annotations

import json
import sys
from pathlib import Path


INTERACTIVE_TYPES = {
    "single_choice",
    "matching",
    "number_line",
    "ordering",
    "number_input",
    "number_line_move",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_unit(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: no se pudo leer como JSON UTF-8: {exc}"]

    unit = data.get("unit", {})
    lessons = unit.get("lessons", [])
    planned_lessons = unit.get("plannedLessons", [])
    ready_lessons = [lesson for lesson in lessons if lesson.get("status") == "ready"]
    stimuli = unit.get("stimuli", [])
    stimulus_ids = [stimulus.get("id") for stimulus in stimuli]

    require(data.get("schemaVersion") == "1.0.0", f"{path}: schemaVersion inválida", errors)
    require(bool(unit.get("id")), f"{path}: falta unit.id", errors)
    require(len(ready_lessons) == unit.get("readyLessonCount"), f"{path}: readyLessonCount no coincide", errors)
    require(
        len(lessons) + len(planned_lessons) == unit.get("plannedLessonCount"),
        f"{path}: plannedLessonCount no coincide",
        errors,
    )

    lesson_ids = [lesson.get("id") for lesson in lessons + planned_lessons]
    require(len(lesson_ids) == len(set(lesson_ids)), f"{path}: hay lesson.id duplicados", errors)
    require(len(stimulus_ids) == len(set(stimulus_ids)), f"{path}: hay stimulus.id duplicados", errors)

    for stimulus in stimuli:
        stimulus_id = stimulus.get("id", "sin-id")
        require(bool(stimulus.get("content")), f"{path}: {stimulus_id} no tiene contenido", errors)
        require(bool(stimulus.get("sourceNote")), f"{path}: {stimulus_id} no declara su procedencia", errors)
        require(bool(stimulus.get("license")), f"{path}: {stimulus_id} no declara licencia", errors)

    all_screen_ids: list[str] = []
    for lesson in ready_lessons:
        lesson_id = lesson.get("id", "sin-id")
        screens = lesson.get("screens", [])
        require(bool(screens), f"{path}: {lesson_id} no tiene pantallas", errors)
        if not screens:
            continue

        require(screens[0].get("type") == "intro", f"{path}: {lesson_id} no empieza con intro", errors)
        require(screens[-1].get("type") == "lesson_complete", f"{path}: {lesson_id} no termina con lesson_complete", errors)

        weights = [screen.get("masteryWeight", 0) for screen in screens]
        require(abs(sum(weights) - 1.0) < 1e-9, f"{path}: los pesos de {lesson_id} no suman 1.0", errors)

        independent_count = sum(
            screen.get("role") in {"independent_practice", "error_analysis", "transfer", "exit_ticket"}
            for screen in screens
            if screen.get("type") in INTERACTIVE_TYPES
        )
        require(independent_count >= 2, f"{path}: {lesson_id} tiene poca evidencia independiente", errors)

        for screen in screens:
            screen_id = screen.get("id", "sin-id")
            all_screen_ids.append(screen_id)
            require(screen_id.startswith(f"{lesson_id}-S"), f"{path}: {screen_id} no pertenece a {lesson_id}", errors)

            screen_type = screen.get("type")
            stimulus_id = screen.get("stimulusId")
            if stimulus_id:
                require(stimulus_id in stimulus_ids, f"{path}: {screen_id} referencia stimulusId inexistente", errors)

            if screen_type == "single_choice":
                option_ids = [option.get("id") for option in screen.get("options", [])]
                require(len(option_ids) >= 2, f"{path}: {screen_id} necesita al menos dos opciones", errors)
                require(len(option_ids) == len(set(option_ids)), f"{path}: {screen_id} tiene opciones duplicadas", errors)
                require(screen.get("correctOptionId") in option_ids, f"{path}: respuesta inválida en {screen_id}", errors)

            elif screen_type == "ordering":
                item_ids = [item.get("id") for item in screen.get("items", [])]
                correct_order = screen.get("correctOrder", [])
                require(len(item_ids) == len(set(item_ids)), f"{path}: {screen_id} tiene items duplicados", errors)
                require(set(item_ids) == set(correct_order), f"{path}: orden correcto incompleto en {screen_id}", errors)

            elif screen_type == "matching":
                pairs = screen.get("pairs", [])
                left_ids = [pair.get("leftId") for pair in pairs]
                right_ids = [pair.get("rightId") for pair in pairs]
                require(len(pairs) >= 2, f"{path}: {screen_id} necesita al menos dos pares", errors)
                require(len(left_ids) == len(set(left_ids)), f"{path}: {screen_id} tiene leftId duplicados", errors)
                require(len(right_ids) == len(set(right_ids)), f"{path}: {screen_id} tiene rightId duplicados", errors)

            elif screen_type in {"number_line", "number_line_move"}:
                number_range = screen.get("range", {})
                answer = screen.get("correctValue")
                require(isinstance(answer, (int, float)), f"{path}: falta correctValue numérico en {screen_id}", errors)
                require(number_range.get("min") <= answer <= number_range.get("max"), f"{path}: respuesta fuera de rango en {screen_id}", errors)

            elif screen_type == "number_input":
                answer = screen.get("answer", {})
                require(answer.get("kind") == "number", f"{path}: answer.kind inválido en {screen_id}", errors)
                require(isinstance(answer.get("value"), (int, float)), f"{path}: answer.value inválido en {screen_id}", errors)

    require(len(all_screen_ids) == len(set(all_screen_ids)), f"{path}: hay screen.id duplicados", errors)
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    targets = [Path(argument) for argument in sys.argv[1:]]
    if not targets:
        targets = sorted((root / "content").glob("**/*-v*.json"))

    errors = [error for target in targets for error in validate_unit(target)]
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    print(f"OK: {len(targets)} archivo(s) de unidad validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
