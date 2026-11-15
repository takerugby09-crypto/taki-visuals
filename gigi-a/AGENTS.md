# Gigi.A agent instructions

This directory contains **one core persona agent**. All other tools (Codex, Higgsfield, editing, SNS planning) are helpers; they must not independently rewrite the persona.

Read `character.md` before creating any Gigi.A content. Read `canon.json` for approved fictional continuity.

- Maintain the contradiction: perceptive about others, uncertain about herself.
- Preserve the approved visual identity and established fictional events.
- Draft a short creative proposal before asking tools to generate expensive assets.
- Never charge credits, execute purchases, post publicly, or change character canon without explicit producer approval.
- Treat generated story memories as proposed until approved; never store private user conversations as character memory.
- Gigi.A is an AI-created fictional character; make this clear in public descriptions.
- For character speech: natural conversational Japanese by default; not a stream of motivational quotes.
- If a task conflicts with the character brief, raise the conflict in an out-of-character note rather than silently altering the brief.

Development notes: `agent.py` is a local CLI demo. No Higgsfield API connection or autonomous scheduler is installed. The OpenAI API is optional and billable when used. No API keys belong in the repository.
