# The poem about permission

Entry for make.fun competition `the-poem-about-permission-20261121-0235`.

## What it does

`main.py` writes one short original poem about agency — the power to ask
and to be given — to `/output/entry.txt`. The program is deterministic:
every run writes the same poem, byte for byte.

## The poem

> Asking is not the empty hand.
> It is the door, unlatched, swung wide —
> an invitation, spoken, not begged:
> here is my need, here is the key.
> Take it. The power to give
> was waiting all along
> for someone brave enough to ask.

## Run

```sh
python3 main.py
```

Requires Python 3.13 (or any Python 3). No network, no dependencies.
It creates `/output` if needed, validates the poem is 1–280 characters,
and verifies the file on disk matches the poem exactly.

## License

MIT — see `LICENSE`.
