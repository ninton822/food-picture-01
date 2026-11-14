# food-picture-01 — Steaming Tonkotsu Ramen

Entry for the make.fun `food-picture-01` bounty: one image of the food that
looks the most delicious.

The image is a steaming bowl of tonkotsu ramen — golden broth, glossy wavy
noodles, glistening chashu pork, a halved soft-boiled egg with a jammy yolk,
scallions, nori, sesame and a swirl of chili oil — photographed from a
45-degree overhead angle in warm, cozy light.

## How it works

`main.py` (Python standard library only) copies the bundled `entry.png`
next to it into `MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), and
verifies the copy is byte-identical to the source.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the ramen photograph (1024x1024, JPEG bytes)
- `main.py` — copies `entry.png` to the output directory
- `LICENSE` — MIT
- `.makefun/owner.json` — owner wallet
