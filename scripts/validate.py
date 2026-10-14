"""Check the distributable package without image generation or dependencies."""

from pathlib import Path
import re
import struct
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"paper-relief-art-text", "paper-relief-art-no-text"}
REFERENCES = {
    "art-direction.md", "prompt-guide.md", "title-writing.md",
    "text-mode.md", "no-text-mode.md",
}
GALLERY = {
    "pine-court-source.png", "mountain-lake-source.png",
    "pine-court-text.png", "pine-court-no-text.png",
    "mountain-lake-text.png", "mountain-lake-no-text.png",
}


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def check_link(origin, target):
    url = urlsplit(target)
    if url.scheme or url.netloc or not url.path:
        return
    path = (origin.parent / unquote(url.path)).resolve()
    require(path.is_relative_to(ROOT), f"Link leaves package: {origin.name}: {target}")
    require(path.exists(), f"Broken local link: {origin.relative_to(ROOT)}: {target}")


def main():
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    require(actual == SKILLS, f"Expected exactly two skill folders, found {sorted(actual)}")
    for name in sorted(SKILLS):
        skill = ROOT / "skills" / name
        entry = (skill / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
        require(frontmatter is not None, f"Missing frontmatter: {name}")
        require(re.search(rf"^name:\s*{re.escape(name)}\s*$", frontmatter[1], re.M),
                f"Skill name and folder disagree: {name}")
        require(re.search(r"^description:\s*\S.+$", frontmatter[1], re.M),
                f"Missing description: {name}")
        metadata = (skill / "agents" / "openai.yaml").read_text(encoding="utf-8")
        require(f"${name}" in metadata, f"Invocation missing from UI metadata: {name}")
        for ref in REFERENCES:
            require((skill / "references" / ref).is_file(), f"Missing reference: {name}/{ref}")
        for target in re.findall(r"\]\(([^\s)]+)\)", entry):
            url = urlsplit(target)
            if not url.scheme and url.path:
                resolved = (skill / unquote(url.path)).resolve()
                require(resolved.is_relative_to(skill), f"Skill is not standalone: {name}/{target}")

    first, second = sorted(SKILLS)
    for ref in REFERENCES:
        left = ROOT / "skills" / first / "references" / ref
        right = ROOT / "skills" / second / "references" / ref
        require(left.read_bytes() == right.read_bytes(), f"Shared guidance differs: {ref}")

    links = 0
    private_paths = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|codex-clipboard|AppData|generated_images|BaiduSyncdisk")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        require(path.suffix not in {".zip", ".log", ".pyc"}, f"Unexpected artifact: {path}")
        if path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        require("\ufffd" not in text, f"Invalid decoded text: {path}")
        require(not private_paths.search(text), f"Local machine path in public text: {path}")
        require("skills/paper-relief-art/" not in text, f"Removed router referenced: {path}")
        targets = re.findall(r"\]\(([^\s)]+)\)", text)
        targets += re.findall(r'(?:src|href)="([^"]+)"', text)
        for target in targets:
            check_link(path, target)
            links += 1

    directory = ROOT / "assets" / "examples"
    require({p.name for p in directory.glob("*.png")} == GALLERY,
            "Gallery must contain only the six approved source/example images")
    for name in sorted(GALLERY):
        image = directory / name
        raw = image.read_bytes()
        require(raw[:8] == b"\x89PNG\r\n\x1a\n" and raw[12:16] == b"IHDR", f"Invalid PNG: {name}")
        width, height = struct.unpack(">II", raw[16:24])
        require(width > 0 and height > 0, f"Invalid image dimensions: {name}")
        if not name.endswith("-source.png"):
            require(width * 4 == height * 3, f"Artwork is not 3:4: {name}")

    for name in ["README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md"]:
        require((ROOT / name).is_file(), f"Missing public document: {name}")
    require("MIT License" in (ROOT / "LICENSE").read_text(encoding="utf-8"), "Missing MIT license")
    print(f"PASS: 2 standalone skills, shared references, 6 PNG assets, {links} link targets, UTF-8 and portable public text.")
    print("Package checks do not evaluate visual taste or guarantee image output.")


if __name__ == "__main__":
    main()
