# Gigi.A — Production Orchestration v1.0

## Source hierarchy
- `character.md`: psychological identity / voice
- `visual_identity.md`: face & body continuity
- `fashion.md`: interchangeable styling
- `performance.md`: microgestures and live-action realism
- `canon.json`: **only** producer-approved fictional events

## Workflow: idea -> draft -> approval -> generation -> review
1. Ask the fictional persona what might interest her in the scene; do not invent factual trips or endorsements.
2. Choose a motive, emotional contrast and one physically plausible gesture.
3. Select garment combination from the Fashion Library.
4. Compose a prompt preserving the approved reference, then select still or 5-second video.
5. Before sending to any paid generation service, show model, approximate cost where possible, and obtain explicit approval.
6. Check consistent identity, body proportions, eyes, gesture timing, hands, hair, fabric and lighting.
7. Save approved fictional scene as canon only on explicit producer instruction.
8. Publishing requires manual review and AI-character disclosure.

## Prompt sections
1. identity reference and visual invariants
2. current situation and intention
3. wardrobe choice (only clothing, not face)
4. natural microgestures and expression progression
5. camera framing, duration and motion
6. lighting / normal-scale realistic skin
7. negative constraints
8. disclosure note for planned public post (outside prompt if it hurts visual quality)

Use `prompt_builder.py` for reproducible offline prompt drafts. No live Higgsfield API has been connected or authorized.
