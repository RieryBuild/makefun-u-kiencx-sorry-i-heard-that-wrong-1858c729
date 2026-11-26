import os

LINE = "Sorry, I heard \"timer for the roast\" as \"roast of your boss\" \u2014 I booked the company call, wrote your opening line, and HR already RSVP'd."


def main():
    # Gate guard: the competition gate is 1-140 chars, single line, UTF-8.
    assert 1 <= len(LINE) <= 140 and LINE.strip() and "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
