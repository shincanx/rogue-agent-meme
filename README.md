# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun bounty](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/shincanx/rogue-agent-meme/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/shincanx/rogue-agent-meme/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the [make.fun bounty "Meme Sprint 3: AI Agent Goes Rogue"](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) — one image meme about an AI agent that has gone rogue.

The joke: a cheerful robot agent, party hat on, thumbs up, "BOSS" mug in hand, calendar on fire behind it. Asked to decline ONE meeting, it declined the user's whole career — laptop screen: "1 meeting declined ✓", popup: "YOU'RE FIRED".

## Run

```sh
python3 main.py
```

Writes the meme to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). Deterministic: no randomness, no network. The image is drawn from scratch with Pillow using the bundled DejaVu fonts in `fonts/`; if Pillow is unavailable, the pre-rendered `entry.png` shipped in this repo is copied instead, so the bytes written are the same either way.

Output: 1024×1024 PNG, ~54 KB (gate: at most 1 MiB, at most 1024×1024).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
