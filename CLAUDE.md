# Robotics keynote — CDP / Headspring

A 53-slide HTML deck, in English, delivered by Javier Fuentes (NCompany) for CDP
through Headspring. September 2026. Rebuilt and extended from a 2023 Spanish deck.

## The one rule

**Never hand-edit `robotics-2026.html`.** It is generated, and it contains ~800 KB of
base64. Slide content lives in `build/slides.py`, layout and behaviour in
`build/build.py`. Change those, run the build, done:

```bash
cd build && python3 build.py      # stdlib only, no dependencies
```

It writes `../robotics-2026.html`. Takes about a second.

## Layout

```
robotics-2026.html   generated — the deck
index.html           generated — redirects to the deck, so the Pages URL needs no file name
img/                 17 animated illustrations (~46 MB) — must sit beside the HTML
video/               the eight clips, 720p H.264 mp4 (~300 MB) — play inside the deck
build/
  slides.py          all slide content, in order. This is the file you usually want
  build.py           renderer: CSS, JS, slide templates
  poster/            still frames, embedded into the HTML at build time
  logos/             cdp.png, headspring.png (embedded at build time)
  prepare-media.py   re-derives img/ and poster/ from the original artwork
README.md            presenter-facing notes: how to run it, what changed since 2023
```

## How the illustrations work — read before touching them

Each of the 17 pieces is a ~150-frame animated WebP loop. All 17 come to 46 MB, far too
much to embed or to load up front. So each ships twice:

- the **still first frame** is embedded in the HTML as a data URI (494 KB for all 17)
- the **animated loop** stays in `img/` and is fetched when its slide comes up, with the
  next slide's loop prefetched (`animate()` in build.py); `prefetchAll()` then walks the rest
  of the deck one file at a time so every loop is cached before it is needed

So the deck opens instantly, every slide draws the moment it appears, and the loop starts
a beat later. Send the HTML without `img/` and it still works — you get the stills, no
broken boxes.

**Pillow's `convert('RGB')` silently keeps only the first frame of an animated WebP.**
This already destroyed the animations once. `prepare-media.py` iterates frames properly;
use it rather than writing new resize code.

Regenerate artwork only when the artwork itself changes:

```bash
cd build && python3 prepare-media.py ~/Desktop/"Headspring Robots"/robotica-17-webp/img
python3 build.py
```

It resizes, recompresses, drops each file's background onto the deck's exact paper colour
(#F7F4EE — the originals arrive in slightly different off-whites and you can otherwise see
the edge of every image), and writes the posters. Needs `pip3 install Pillow`.

## Slide conventions

From the `deck-una-idea` house style. Worth keeping:

- One idea per slide. If it needs an "and also", it is another slide.
- Four bullets maximum, ~12 words each, lower case after the first word.
- Illustration on the right, roughly 41% of the width. Never on anchor or data slides.
- Anchor slides (`kind="anchor"`) are one big sentence, no illustration. Dark ones alternate.
- Every figure carries its source in the `src` field, set in small grey type under the bullets.
- Bullets are a short brass dash (14 px, 2 px thick), pure CSS — it echoes the rule under each title.

Slide kinds in `slides.py`: `cover · quote · bullets · anchor · data · video · close`.
Long slides shrink to fit automatically (`fitSlide()`), so a fifth bullet will not overflow —
but it will look cramped, which is the style telling you to split the slide.

## Videos

Eight clips. `v` or a click plays the one on screen, full screen; `space` pauses, arrows seek,
`Esc` stops. Three paths, picked automatically:

1. a local file at `video/<slug>.mp4` or `.webm` → plays inside the deck, full screen, offline.
   All eight are checked in. Downloaded with yt-dlp (`-f "bv*[height<=720][vcodec^=avc1]+ba"`),
   remuxed with `-movflags +faststart`. The BBC Asimov piece is 47 minutes; the file is the
   first 2:52, which contains the quoted line (at 2:22).
2. served over http(s) with no local file → embedded YouTube player, taken full screen
3. opened as a `file://` with no local file → opens YouTube in a new tab, because browsers
   block the embedded player from `file://` origins

Slugs are in `slides.py` (`01-asimov-1967` … `08-amazon-robots`). Every video ID was checked
against YouTube's oEmbed API and resolves to the official channel named on the slide.

GitHub's hard limit is 100 MiB per file; the Amazon clip is 95.6 MiB. Do not re-download it at
a higher setting.

## Facts

Every figure on a slide is sourced, and the source is on the slide. If you change a number,
change its source line with it. Two are worth flagging under questioning:

- **Figure's 56% across 30 unseen homes** is company-reported, not independently replicated.
  It sits on the slide as a reliability number as much as a capability one.
- **China's robot density is 166 per 10,000**, not the 470 that circulated in 2024. IFR
  restated it downward in April 2026 after China revised its manufacturing employment base.
  The old figure is still all over the web.

## Deploying

Live at **https://jfuentesibanez.github.io/robotics-2026/** — GitHub Pages, from the `main`
branch of https://github.com/jfuentesibanez/robotics-2026, root folder. Push to `main` and it
redeploys in about a minute. Over https the local clips stream in place and, if one were ever
missing, the YouTube embed plays in place too.

The repo is public (free Pages needs that) and contains the video copies — see the README note.
The old private copy on claude.ai has no `img/` or `video/` and is superseded.
