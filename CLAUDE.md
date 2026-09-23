# Robotics keynote — CDP / Headspring

A 59-slide HTML deck, in English, delivered by Javier Fuentes (NCompany) for CDP
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
img/                 19 animated illustrations (~35 MB) — must sit beside the HTML
video/               the ten clips, H.264 mp4 (~355 MB) — play inside the deck
build/
  slides.py          all slide content, in order. This is the file you usually want
  build.py           renderer: CSS, JS, slide templates
  poster/            still frames, embedded into the HTML at build time
  logos/             cdp.png, headspring.png (embedded at build time)
  prepare-media.py   re-derives img/ and poster/ from the original artwork
README.md            presenter-facing notes: how to run it, what changed since 2023
```

## How the illustrations work — read before touching them

Each of the 19 pieces is a ~150-frame animated WebP loop. All 19 come to 35 MB, far too
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

It resizes, recompresses, keeps each file's own per-frame timing (all 17 are 6-second loops,
but the automaton runs 80–560 ms a frame, so a fixed frame rate would play it 2.5× too fast),
drops each file's background onto the deck's exact paper colour
(#F7F4EE — the originals arrive in slightly different off-whites and you can otherwise see
the edge of every image), and writes the posters. The current originals are the September 2026
revision: eight pieces (08, 10–16) were re-animated by the illustrator. Needs `pip3 install Pillow`.

## Slide conventions

From the `deck-una-idea` house style. Worth keeping:

- One idea per slide. If it needs an "and also", it is another slide.
- Four bullets maximum, ~12 words each, lower case after the first word.
- Illustration on the right, roughly 41% of the width. Never on anchor slides; a data slide may
  carry a country outline (`map=`) instead, drawn as a line, never a picture.
- Anchor slides (`kind="anchor"`) are one big sentence, no illustration. Dark ones alternate.
  `wide=True` sets one sentence per line without wrapping, for the rare three-line anchor.
- Every figure carries its source in the `src` field, set in small grey type under the bullets.
- Bullets are a small hollow brass ring (9 px, 2 px stroke), pure CSS.

Slide kinds in `slides.py`: `cover · agenda · quote · bullets · anchor · data · compare · chart · video · breath · close`.
A `compare` slide puts two figures side by side with a rule between them and three notes under
each: use it whenever the two numbers are not the same thing measured twice (different robots,
different benchmarks), so an arrow never implies a like-for-like change.
The `agenda` slide and the act rail at the top of every slide are built automatically from the
`act` field, in order of first appearance (`ACTS` in build.py); `Close` is left out. Clicking an
act in either jumps to its first slide.
A bullets slide may carry `polaroids=[...]` instead of `art=`: real photos from `build/photos/`
(square-cropped, embedded at build time) drop in as polaroids, one per click or →, and settle into
a loose pile; ← takes the last one back, and the deck only moves on once all are down (`PILE` in build.py holds the resting positions, up to seven). The credits line is
built from `photos/credits.json`; every photo is CC BY, CC BY-SA or CC0/public domain from
Wikimedia Commons. Keep it that way — never a photo without a licence that allows reuse.
A quote slide may carry `art=` (slide 3 uses the animated Asimov, piece 19), or `portrait=` and
`credit=`: a transparent cut-out from
`build/photos/<name>.webp` stands on the footer rule on the right, fading at the bottom. The
Asimov master is `photos/asimov.png` (Phillip Leonian's portrait, public domain, Library of
Congress), cut out with the macOS Vision subject mask.
An illustrated bullets slide may also carry `pin=` (`talos-1963`, `pandora-krater`): one polaroid pinned over the
lower-left corner of the illustration, landing a second after the slide appears. The Talos still
is the one exception to the free-licence rule: a frame from Columbia's *Jason and the Argonauts*
(1963), from the official Movieclips upload, quoted small and credited on the slide.
The Pandora pin is the Niobid Painter's calyx krater (British Museum, c. 460 BC), photo by
ArchaiOptix, CC BY-SA 4.0: Pandora is shown frontally, which Greek vase painters kept for the
dead, the possessed and the not-quite-human. Each pin's credit line lives in `credits.json`.
A `breath` slide is the illustration alone, no text: a pause after a heavy run, used once after
the three uncomfortable conclusions.
A `chart` slide is a static SVG line chart drawn by `chart_svg()` in build.py from the numbers
in `slides.py`: one highlighted series in rust, the rest in grey with labels at the line end.
Long slides shrink to fit automatically (`fitSlide()`), so a fifth bullet will not overflow —
but it will look cramped, which is the style telling you to split the slide.

## Videos

Ten clips. `v` or a click plays the one on screen, full screen; `space` pauses, arrows seek,
`Esc` stops. Three paths, picked automatically:

1. a local file at `video/<slug>.mp4` or `.webm` → plays inside the deck, full screen, offline.
   All eight are checked in. Downloaded with yt-dlp (`-f "bv*[height<=720][vcodec^=avc1]+ba"`),
   remuxed with `-movflags +faststart`. The BBC Asimov piece is 47 minutes; the file is the
   first 2:52, which contains the quoted line (at 2:22).
2. served over http(s) with no local file → embedded YouTube player, taken full screen
3. opened as a `file://` with no local file → opens YouTube in a new tab, because browsers
   block the embedded player from `file://` origins

Slugs are in `slides.py` (`01-asimov-1967` … `11-xpeng-iron`). Every YouTube ID was checked
against the oEmbed API and resolves to the official channel named on the slide. `09-rt2-2023`
has no YouTube ID: it is DeepMind's demo montage from robotics-transformer2.github.io, so the
slide carries `link=` instead of `vid=` and the fallback opens that page.

`11-xpeng-iron` is a 100-second excerpt of XPENG's 5:43 official video (4i22XO_HJB8): its three
demo sections with their title cards, 0:15–1:00, 2:00–2:25 and 3:00–3:30, re-encoded; the
presenter's explanations are cut. The slide label says "excerpt".

There is no `02-*` clip: the Gemini Robotics 1.5 video was cut in September 2026 because it
repeated what RT-2 and Helix 2.5 already show.

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

- **Humanoid shipments, H1 2026.** The slide uses Counterpoint's numbers: 22,000+ units, up
  nearly 300%, 86% from Chinese vendors, Agibot and Unitree first and second (20 August 2026).
  A rival estimate from Smart Analytics Global (19,100, +272%, 97% Chinese) circulated via Forbes
  the same week; do not mix the two.
- **Tesla Optimus.** The slide quotes Musk on the Q4 2025 call, 28 January 2026: "It's not in
  usage in our factories in a material way. It's more so that the robot can learn." He also said
  "It's still in the R&D phase." (Motley Fool transcript.)
- **Epoch AI, "Where Autonomy Works", 10 February 2026.** It names a handful of systems with
  proven economic value in production (Amazon's Vulcan picker, Boston Dynamics' Stretch unloader,
  the Hydrus underwater vehicle), none humanoid; package sorting ~4× slower than an average
  worker; household tasks 2–10× slower, laundry 5×. It does not give a count of "five systems":
  the slide was reworded to match.
- **Hourly labour cost 2025** (Eurostat lc_lci_lev, whole economy, March 2026): EU €34.9,
  Germany €45.0, Italy €32.0, Spain €26.4. Agility's $8,500/month RaaS price and $25,000
  deployment fee are from its June 2026 SPAC investor deck as reported by The Robot Report.

## Deploying

Live at **https://jfuentesibanez.github.io/robotics-2026/** — GitHub Pages, from the `main`
branch of https://github.com/jfuentesibanez/robotics-2026, root folder. Push to `main` and it
redeploys in about a minute. Over https the local clips stream in place and, if one were ever
missing, the YouTube embed plays in place too.

The repo is public (free Pages needs that) and contains the video copies — see the README note.
The old private copy on claude.ai has no `img/` or `video/` and is superseded.
