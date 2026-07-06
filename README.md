# P-009 · Resume — 水墨 × 京

A single-page resume for **Eric Lu · Data + AI Scientist**, in two editions:

| Edition | Where | Holds |
|---|---|---|
| **Public** | GitHub Pages (this repo, `index.html`) | the full resume, public-safe contact |
| **Private (login)** | A100 showcase `/showcase/resume` | + phone / WeChat / LinkedIn / CV PDF / references via `private.json` (never in git) |

**Design** — 墨分五色 "ink has five colors": skill mastery is drawn as brushstrokes whose ink *density*
is the meter (no percentage bars). Washi-paper day mode / ink-stone night mode (gold kintsugi rules wake
only at night). Vertical-writing chapter rail (序 技 歴 作 学 信) like a Tang handscroll; one vermillion seal.
Typography: Zen Old Mincho (display) over IBM Plex Sans/Mono (body/data). Zero build step — one hand-written
HTML file, reduced-motion respected, keyboard-focus visible, responsive to mobile.

**Templating** — all content renders from the `RESUME` object at the top of `index.html`.
Placeholder (made-up) parts are marked `FILL-ME`; the projects are real, running systems.
See [`FILLING.md`](FILLING.md).

```
index.html                  the page (public edition = exactly this file)
FILLING.md                  how to swap the made-up content for the real one
private/app.py              the login edition (Flask: session login + serves private.json)
private/Dockerfile          container for the A100
private/private.sample.json shape of the private contact file (real one lives only on the host)
ops/deploy-a100.sh          build + run + Traefik route on the A100
```

## Run the login edition locally
```bash
cd P-009-resume
OWNER_PW=pw1 REVIEWER_PW=pw2 python3 private/app.py    # http://localhost:8202/showcase/resume
```

