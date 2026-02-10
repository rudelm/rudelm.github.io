#!/usr/bin/env python3
"""Shift all ATX-style markdown headers one level down (# -> ##, ## -> ###, etc.)."""
import re
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent / "content" / "posts"

# Match ATX headers: optional leading space, 1-6 #, required space, rest of line
HEADER_RE = re.compile(r"^(\s*)(#{1,6})(\s+)(.*)$")


def shift_header_line(line: str) -> str:
    m = HEADER_RE.match(line)
    if m:
        indent, hashes, space, rest = m.groups()
        # Add one more # (max 6 in spec; 7th will render as literal in some parsers)
        return f"{indent}{hashes}#{space}{rest}"
    return line


def shift_headers_in_content(content: str) -> str:
    lines = content.split("\n")
    result = []
    in_fenced_block = False
    fence_char = None
    for line in lines:
        # Track fenced code blocks (``` or ~~~)
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            if not in_fenced_block:
                in_fenced_block = True
                fence_char = line.strip()[:3]
            elif line.strip().startswith(fence_char):
                in_fenced_block = False
                fence_char = None
        if in_fenced_block:
            result.append(line)
        else:
            result.append(shift_header_line(line))
    return "\n".join(result)


def main() -> None:
    md_files = list(POSTS_DIR.rglob("*.md"))
    for path in sorted(md_files):
        text = path.read_text(encoding="utf-8")
        new_text = shift_headers_in_content(text)
        if text != new_text:
            path.write_text(new_text, encoding="utf-8")
            print(path.relative_to(POSTS_DIR))


if __name__ == "__main__":
    main()
