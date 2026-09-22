# A Look at the Present and Future of Robotics

English rebuild of the 2023 AJE Cádiz robotics talk. 54 slides, ~35–40 minutes.

```
robotics-2026.html     the deck — open it in any browser, double-click works
image-prompts.md       the 17 prompts the illustrations came from
img/                   the 18 animated illustrations — keep this folder next to the HTML
poster/                the still frames (already embedded in the HTML; kept as a source set)
video/                 drop local copies of the clips here (optional)
```

**Running it.** `←` `→` or click to move, `f` for fullscreen, click anywhere in the left
quarter of the screen to go back. The deck scales to whatever screen it lands on.

**Videos.** Eight clips, each behind a play button. `v` or a click plays the one on screen,
full screen; `space` pauses, `←` `→` seek ten seconds, `Esc` stops and returns to the slide.
All eight are in `video/` as local 720p files, so they play *inside the deck, offline*, with no
YouTube chrome and no buffering in front of an audience. The BBC piece is trimmed to its first
2:52, which is where Asimov says the line on the slide. Names, in slide order:
`01-asimov-1967` · `02-gemini-robotics` · `03-figure-helix` · `04-unitree-h2` ·
`05-atlas-hands-on` · `06-1x-neo` · `07-bmw-figure` · `08-amazon-robots`.

If a file is missing the deck falls back on its own: served over http(s) it embeds the YouTube
player and takes it full screen; opened as a `file://` it opens the clip on YouTube in a new tab,
because browsers block the embedded player from `file://` origins. Every video ID was checked
against YouTube's API — all eight resolve to the official channel named on the slide.

**Logos.** CDP and Headspring sit on the cover, divided by a hairline; Headspring repeats small
in the footer of every slide, on an ivory chip where the slide is dark. Both are embedded in the
HTML — nothing to install.

**Illustrations — how the animation is handled.** The 18 pieces are six-second loops, 38 MB in
total, which is far too much to open a deck with. So the deck carries a still frame of each one
embedded in the HTML, loads the animated file the moment you reach that slide plus the next one,
and then quietly fetches the remaining loops one by one in the background. On a normal connection
the whole deck is animated within a minute of opening it; on a bad one, each slide still draws
instantly and its loop starts as soon as the file lands. The motion is deliberately subtle — a
slow six-second breathe, not a GIF — and the robot arm (slide on industrial robots) barely moves
by design of the original artwork.

That means **`robotics-2026.html` and the `img/` folder travel together.** Keep them side by side
and it animates. Send the HTML on its own and it still works perfectly — you just get the stills
instead of the loops, with nothing broken and no empty boxes. Worth knowing before you email it
to anyone.

**Presenting from someone else's computer — the public URL.** The deck is live on GitHub Pages:

    https://jfuentesibanez.github.io/robotics-2026/

Open that on any machine, press `f`, and present. Illustrations animate and the eight clips play
full screen from the same host, so the only thing you depend on is the room's internet — and the
clips stream progressively, so they start within a second or two. If you want zero dependence on
the venue wifi, clone or download the repository (https://github.com/jfuentesibanez/robotics-2026) and open
`robotics-2026.html` from disk: everything, videos included, is in the folder.

To publish a change: edit `build/slides.py` or `build/build.py`, run `python3 build.py` in
`build/`, commit and push to `main`. Pages redeploys in about a minute.

The repository is public, as free GitHub Pages requires. The clips in `video/` are copies of the
official YouTube uploads; that is fine for the talk, but keep it in mind before pointing anyone
else at the repository itself.

There is also an older private copy on claude.ai. It does not carry `img/` or `video/`, so it
shows stills and opens YouTube in a new tab — use the GitHub URL instead.

**Illustrations.** The deck ships with rough placeholder drawings so it is presentable as-is.
Generate the real ones from `image-prompts.md`, save them into `img/` under the filenames given
there, and they replace the placeholders automatically — no editing of the HTML.

**Printing to PDF.** Cmd-P → Save as PDF, landscape, margins none, background graphics on.
Video slides print as the play button and the caption.

## What changed from the 2023 version

The arc is the one you built: ancient longing → the word → industrial revolutions → what a robot
is → unmet expectations → AI meets robotics → business impact. Kept, translated, and extended.

Added:
- **The Golem**, alongside Talos and Pandora — Meyrink's 1915 novel, and the callback at the
  close: it never disobeys, which is exactly the problem.
- **A 15-slide block on 2023–2026** that did not exist before: RT-2 to Helix 2.5, skills
  transferring between bodies, the Unitree price collapse, why small models still matter, and
  the counter-evidence (89.4% in simulation against 12.4% on real household tasks).
- **Evidence and failure side by side** — Figure at BMW with real numbers, and Blue Jay,
  Optimus, and the three-year Amazon pilot in the next slide.
- **Three uncomfortable conclusions and four Monday actions**, which the old deck ended without.
- Updated figures throughout: IFR 2024 data, Spain's 5,160 installations, the 2025 labour
  meta-analysis that complicates the Acemoglu–Restrepo story, and the 20 January 2027 Machinery
  Regulation date.

Every number on a slide carries its source in the footer line. Two are worth knowing about
before you are challenged from the floor:

- **Figure's 56% in 30 homes** is company-reported and has not been independently replicated.
  It is on the slide as a reliability number as much as a capability one.
- **China's robot density** is 166 per 10,000, not the 470 that circulated in 2024 — IFR restated
  it downward in April 2026 after China revised its manufacturing employment base. If anyone
  quotes the old figure, that is why.
