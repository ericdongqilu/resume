# Filling in the content

Everything renders from the **`RESUME`** object at the top of `index.html`.

## Content status (2026-07-02)
The content is **mostly real**, consolidated from earlier portfolio material:

| Section | Status |
|---|---|
| Name 卢东奇 / Eric Lou, seal 卢 | ✅ real |
| Education — Monash ×2 (BCom Econometrics & Business Statistics · Master of IT) | ✅ real |
| Experience — Crystal Jade Group Melbourne (App Developer / Data Analyst) | ✅ real org+titles · **FILL-ME: exact dates + 1-2 concrete outcome bullets** |
| Experience — Sensus AI lab (current) | ✅ real systems |
| 旧卷 old-scroll projects (MA backtester · hot-spot tracker · SARIMA · R portfolio) | ✅ real work, rebuilt as the in-page live demos |
| 新卷 new-scroll projects | ✅ real running systems |
| Skills (econometrics, classical ML incl. the audio/XGBoost pipeline, R/Shiny, LLM…) | ✅ grounded in real past work |
| Contact email ericdongqilu@gmail.com | ✅ real (public-safe) |
| `writing` notes | stylized — replace at will |
| Dates marked `FILL-ME` (Monash years, Crystal Jade years) | ❗ the only guesses left |

## Private edition data (`private.json`, A100 host only — never in git)
Real values are deployed there: WeChat `Eric__Lou`, LinkedIn `Eric-Dongqi-Lu`,
the AU phone (update if changed), plus `cv_url` / `references` when ready.

## Publishing changes
```bash
git add index.html && git commit -m "content: ..." && git push   # GitHub Pages redeploys
bash ops/deploy-a100.sh                                          # or rebuild resume-showcase
```
