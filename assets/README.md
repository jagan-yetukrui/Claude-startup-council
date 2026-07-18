# assets/

Put `demo.gif` here — a short recording of a real `/council` run — then uncomment the `<img>` line
near the top of the main [`README.md`](../README.md).

## How to make a good demo GIF

Keep it **15–30 seconds** and show the payoff: typing `/council`, then the verdict scrolling. Nobody
watches a two-minute agent run; cut to the good part.

**Easiest tools (macOS):**
- **[Kap](https://getkap.co)** — free, records a screen region straight to GIF or mp4.
- **[LICEcap](https://www.cockos.com/licecap/)** — free, tiny, records a region directly to `.gif`.
- Built-in **QuickTime** screen recording → convert with `ffmpeg` or [gifski](https://gif.ski):
  ```bash
  # record with QuickTime to demo.mov, then:
  ffmpeg -i demo.mov -vf "fps=12,scale=820:-1:flags=lanczos" -c:v pam -f image2pipe - | \
    gifski --fps 12 -o assets/demo.gif -
  ```

**Keep it small.** GitHub renders GIFs inline but big ones load slowly. Aim for **under ~8 MB**.
Shrink an oversized one at [ezgif.com/optimize](https://ezgif.com/optimize) or with:
```bash
gifsicle -O3 --lossy=80 --colors 128 assets/demo.gif -o assets/demo.gif
```

**Then wire it up:**
```bash
# from the repo root
git add assets/demo.gif
# uncomment the <img ... demo.gif> line in README.md
git commit -m "Add demo GIF"
git push
```

Tip: a real recording beats a scripted one here — the honest, unedited verdict is the selling point.
