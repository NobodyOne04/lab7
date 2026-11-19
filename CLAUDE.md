# lab7

A 2020 console business game (parking-meter rental) in one Python file.

## Commands
- `python3 model.py` (standard library only). No tests.

## Layout
- `model.py`: constants, the `Model` class (budget, meters, staff), two background threads
  (clients every `RENT_TICK`, months every `MONTH`) and the input loop.
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- Prompts and messages are Russian; keep them that way.
- Archived lab: docs or small fixes only unless asked.
