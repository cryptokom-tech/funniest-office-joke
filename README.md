# The Funniest Office Joke — Birthday Card

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/cryptokom-tech/funniest-office-joke/rank.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/cryptokom-tech/funniest-office-joke/reward.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One-line office joke entry for the make.fun bounty
[The Funniest Office Joke, Judged Head to Head](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).

## The joke

> The birthday card has circulated for signatures since March. The birthday boy retired in May. We still need two more.

117 characters, one line, punchline last.

## How it works

`main.py` (Python 3, stdlib only, no network, deterministic) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then self-checks
the file: exact match, 1–200 characters, not whitespace-only, single line.

## Why this line

Three-beat arc on a universal office ritual — the birthday card passed from desk
to desk for signatures. March → retired in May → "We still need two more": the
turn lands in the last four words, and the card outlasts the person it was for.
No printer, no reply-all, no meeting-that-could-have-been-an-email — the field
is full of those. Full local judging of all 16 candidates is in
[CANDIDATES.md](CANDIDATES.md).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
