"""Build Gigi.A still/video prompt drafts without API access or charges.

Usage:
  python3 gigi-a/prompt_builder.py --scene "Tokyo cafe" --look everyday
  python3 gigi-a/prompt_builder.py --scene "Taxi at dusk" --look burgundy --mode video

This only prints a draft; it cannot generate media or publish.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOOKS = {
    "burgundy": "a burgundy ruffled blouse and charcoal tailored blazer, dark tights, subtle jewelry",
    "cream": "an elegant but natural cream silk dress with restrained gold accessories",
    "camel": "a camel trench coat, relaxed ivory blouse and trousers, practical dark boots",
    "everyday": "a relaxed grey knit or white shirt with a black tailored blazer",
    "statement": "a structured red jacket with a subtle green accent and tailored dark trousers",
}
GESTURES = {
    "curiosity": "A tiny shift of focus to someone just off-camera, a short pause and a few degrees of head tilt.",
    "playfulness": "A half-finished smile appears unexpectedly and turns into a short, natural laugh.",
    "uncertainty": "She briefly looks away and her lips part as if reconsidering what to say.",
    "quiet": "She blinks naturally, breathes, shifts her weight subtly, and remains unposed.",
}

def build(scene, look, emotion, mode):
    preamble = (
        "Create a naturalistic live-action " + ("5-second vertical video" if mode == "video" else "vertical portrait") +
        " featuring the fictional AI character Gigi.A. Use the PRODUCER-APPROVED identity reference image "
        "(not yet attached here) as the mandatory face and body reference; do not substitute a new face. "
        "Keep recognizable facial proportions, natural blonde waves, green-blue eyes, gentle freckles, "
        "natural asymmetry, and believable skin texture. "
    )
    content = (
        "Situation: " + scene + ". Outfit: " + LOOKS[look] +
        ". Inner state: a perceptive woman who is curious about others but not fully sure of herself. "
        "Performance: " + GESTURES[emotion] +
        " The gesture follows the emotional context rather than being a decorative pose. "
    )
    camera = (
        "Camera: eye-level, natural conversational distance, restrained handheld feel, "
        "subtle environmental light, believable perspective and no aggressive beauty filtering. "
    )
    negative = (
        "Avoid perfect symmetry, fixed beauty poses, constant smiling, hyper-detailed macro pores, "
        "plastic skin, unnatural blinking, facial drift, body distortion, floating props, "
        "erratic hair, excessive gestures or abrupt transitions. "
    )
    return preamble + content + camera + negative

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scene", required=True)
    p.add_argument("--look", choices=LOOKS, default="everyday")
    p.add_argument("--emotion", choices=GESTURES, default="curiosity")
    p.add_argument("--mode", choices=["image", "video"], default="image")
    args = p.parse_args()
    print(json.dumps({"mode": args.mode, "approved_reference_required": True,
        "generation_submitted": False, "prompt": build(args.scene, args.look, args.emotion, args.mode)},
        ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
