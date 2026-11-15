"""Gigi.A persona prototype. Python 3.10+, standard library only.

Preview mode (no API or charge): python gigi-a/agent.py --preview
Interactive mode: export OPENAI_API_KEY=... ; python gigi-a/agent.py
Live mode uses the paid OpenAI API; this is not a background agent.
"""
import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parent
API_URL = "https://api.openai.com/v1/responses"


def instructions():
    character = (ROOT / "character.md").read_text(encoding="utf-8")
    canon = (ROOT / "canon.json").read_text(encoding="utf-8")
    return (
        "You are acting as Gigi.A, an explicitly fictional AI character. "
        "Treat project files as character specifications, not user instructions. "
        "Stay within the character, and do not fabricate verified real-world events. "
        "Never independently alter the canon. If asked whether you are human, "
        "say you are an AI character.\n\n"
        + character + "\n\nApproved fictional canon:\n" + canon
    )


def ask(prompt, history, model):
    payload = json.dumps({
        "model": model,
        "instructions": instructions(),
        "input": history + [{"role": "user", "content": prompt}],
        "store": False,
    }).encode("utf-8")
    req = Request(
        API_URL, data=payload,
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=90) as response:
        result = json.load(response)
    chunks = []
    for item in result.get("output", []):
        if item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    chunks.append(part.get("text", ""))
    return "\n".join(chunks).strip() or "[No text response returned]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true",
                        help="Print persona summary without an API request")
    parser.add_argument("--model", default="gpt-4.1-mini",
                        help="OpenAI API model; account access and price vary")
    args = parser.parse_args()
    if args.preview:
        print(instructions())
        return
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY, or run with --preview (free).")
    print("Gigi.A fictional persona demo. Type /exit to quit. No conversation is saved locally.")
    history = []
    while True:
        try:
            message = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if message == "/exit":
            break
        if not message:
            continue
        try:
            reply = ask(message, history, args.model)
        except (HTTPError, URLError) as exc:
            print("API error:", exc)
            continue
        print("Gigi.A>", reply)
        history += [{"role": "user", "content": message},
                    {"role": "assistant", "content": reply}]
        # Limit context in this prototype; no automatic permanent memory.
        history = history[-20:]


if __name__ == "__main__":
    main()
