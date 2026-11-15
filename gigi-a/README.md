# Gigi.A — one persona agent

This prototype keeps Gigi.A's **identity** in `character.md`, approved fictional story continuity in `canon.json`, and agent behavior in `AGENTS.md`.

### Try without charges
```sh
python3 gigi-a/agent.py --preview
```

This prints the active persona instructions. It does **not** generate a response.

### Chat with the character (optional paid OpenAI API)
Set `OPENAI_API_KEY` in your local shell, **never GitHub or a commit**, then:
```sh
python3 gigi-a/agent.py
```
Type messages to the fictional character. Type `/exit` to quit. API usage may incur charges independent of a ChatGPT subscription. There is no permanent chat history, automated scheduling, or Higgsfield integration yet. `canon.json` is intentionally never auto-updated.

### Next development milestones
1. Test voice and personality with producer-reviewed conversations.
2. Approve a reference portrait and visual-identity rules.
3. Add consent-based fictional memory proposals and review workflow.
4. Add Higgsfield generation tool with explicit credit approval and spending cap.
5. Add draft content pipeline; keep publishing manual until reviewed.

**Public repo caution:** This repository was Public when this branch was created. Do not add secrets, private communications, real personal details, or proprietary references.
