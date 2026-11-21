# Republic of Sulara — Passport Page of a Country That Isn't There

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/rizalagustin448-bit/passport-page-20261121-bot-v1/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/rizalagustin448-bit/passport-page-20261121-bot-v1/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

An invented passport spread for the **Republic of Sulara**, a salt-flat
republic whose only road crosses the flats and closes in flood season.

- **Data page:** portrait of Mara Ilin Voss, salt harvester, born Salmar;
  bilingual labels; document No. SR 2024 018837; issued 12 MAR 2024,
  expires 12 MAR 2034; machine-readable zone with valid ICAO check digits.
- **Visa page:** departure/arrival stamps from neighbouring Almara
  (Jun 2025) and Tevrin (Feb 2026) — every stamp after the issue date,
  trips that open and close in the right order.
- **The telling detail:** a red SALT HARVEST PERMIT (season 2026/27,
  salt tax 12 kg) and a VISA CONDITION box — entry by salt road only,
  road closed in flood season (Nov–Mar), holder must carry 2 L water.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024) to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image is
drawn offline with Pillow; the sandbox installs nothing, so the entrypoint
imports nothing beyond `os`, `shutil`, `pathlib`.

## License

MIT — see LICENSE.
