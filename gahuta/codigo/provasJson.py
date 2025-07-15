import json, re
from pathlib import Path

IMG_RE = re.compile(r"[A-Za-z]:\\.*?\.(?:png|jpe?g)", re.IGNORECASE)

def simplify_enem_json(src: str | Path, dst: str | Path) -> None:
    with open(src, encoding="utf-8") as f:
        obj = json.load(f)

    questions = obj.get("data") or obj.get("questions") or obj

    seen = set()                #  ← track numbers we’ve already added
    out  = []

    for q in questions:
        number = q["number"]
        if number in seen:          # duplicate → skip
            continue
        seen.add(number)

        # join fragments without gluing words
        parts = []
        for frag in q["content"]:
            txt = frag["content"]
            if parts and parts[-1][-1].isalnum() and txt[:1].isalnum():
                parts.append(" ")
            parts.append(txt)
        full = "".join(parts)

        has_img = int(bool(IMG_RE.search(full)))
        clean   = IMG_RE.sub("", full).strip()

        out.append({"number": number, "text": clean, "has_img": has_img})

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)




IN_DIR  = Path("dados/provas_json/provas")
OUT_DIR = Path("dados/provas_json/provas_concat")
OUT_DIR.mkdir(parents=True, exist_ok=True)

json_files = list(IN_DIR.glob("*.json"))            # or .rglob("*.json") for subdirs
print(f"Found {len(json_files)} files to simplify")

for src in json_files:
    dst = OUT_DIR / src.name                        # same filename
    simplify_enem_json(src, dst)
    print(f"✔  {src.name} → {dst.relative_to(OUT_DIR.parent)}")

print("All done!")
