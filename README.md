# lab7

A 2020 console business game in Python: run a parking-meter rental company and stay above the
debt limit.

## Run

```sh
python3 model.py
```

Python 3, standard library only. Prompts are in Russian: `1` buy parking meters, `2` hire
staff, then a quantity; `q` quits.

## Rules (from `model.py`)

| Constant | Value | Meaning |
|---|---|---|
| start budget | 500,000 | money you begin with |
| `PARKOMAT_PRICE` | 50,000 | price of one parking meter |
| rent price | 700 | income per rented meter per month |
| `SALARY` | 50 | monthly cost per employee |
| `MAX_DEBT` | -90,000 | the game ends below this budget |
| `RENT_TICK` / `MONTH` | 20 s / 60 s | how often clients come / months pass (real time) |

- Every 20 s a random number of clients rents some of your free meters.
- Every 60 s a month passes: income (rented × price) minus upkeep (0.5 per free meter,
  0.8 per rented one) and salaries goes into the budget.
- You need one employee per 10 meters to buy more.

Decisions: [docs/adr](docs/adr/README.md).
