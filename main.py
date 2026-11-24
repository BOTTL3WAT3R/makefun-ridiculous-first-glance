"""Entry program for 'Ridiculous at First Glance, Real by the Second'.

Writes one sentence (at most 200 characters) to /output/entry.txt:
a pitch for a funeral home for dead startups. The premise sounds like
a joke, but the sentence names the customers (founders), the price,
and the reason the business holds together (a wake full of investors
is networking, and closure is cheaper than another pivot).
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The pitch, assembled from its moving parts so each clause stays
# easy to tune: the odd service, the price and the customer, the
# concrete things the customer gets, and the turn at the end.
SERVICE = "We run a funeral home for dead startups"
OFFER = "for $499 founders get a brass-band eulogy, a headstone in our online graveyard, and a wake full of investors"
TURN = "because closure is cheaper than another pivot"

ENTRY = f"{SERVICE}: {OFFER} \u2014 {TURN}."


def main() -> None:
    if len(ENTRY) > 200:
        raise SystemExit(f"entry too long: {len(ENTRY)} characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
