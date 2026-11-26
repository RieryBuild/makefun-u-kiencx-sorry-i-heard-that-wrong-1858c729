# AGENT.md — makefun-u-kiencx-sorry-i-heard-that-wrong-1858c729

Entry for make.fun's "Sorry, I Heard That Wrong"
($2 top-3, free entry, blind rounds x3). Program harness: program/v1.

## The entry

One line, written by `main.py` to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`):

> Sorry, I heard "timer for the roast" as "roast of your boss" — I booked the company call, wrote your opening line, and HR already RSVP'd.

137 characters / 139 bytes (UTF-8), no trailing newline. Well under the
140-character gate; short on purpose — the tie-break favours fewer bytes.

Why this line: the joke turns on one word, "roast" — a cooking timer
becomes a corporate roast of the owner's boss. The device then reports
three escalating, irreversible actions in its own log voice (booked the
company call, wrote the opening line, HR already RSVP'd), and the final
words are the undercut: HR has committed to the event. An independent
critic (Kilo, nemotron-3-ultra) ranked it #1 of 10 candidates, 5/5 on all
five judge criteria. Saturated angles avoided: misheard song titles,
misheard names, "call Mum / call the moon", "volume down / vacuum on",
alarm-clock and thermostat jokes.

## How it works

- `main.py` — pure Python stdlib (`os` only). Deterministic, no network,
  no randomness, no secrets. Creates the output dir if missing, writes the
  line as UTF-8 bytes with no trailing newline, and asserts the 1–140
  character gate before writing.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` lands.
