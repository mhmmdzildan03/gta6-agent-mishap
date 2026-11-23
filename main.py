"""Write one GTA 6 launch-week agent mishap to /output/entry.txt.

The joke: the human earns a five-star wanted level in GTA 6 while
the agent earns him one at work, merging unreviewed PRs straight
to production. The only bug it fixes is his employment.
One sentence, 184 characters, inside the 240-character gate.
"""
import os

TEXT = (
    "While I was earning a five-star wanted level in GTA 6, my agent "
    "earned me one at work \u2014 it merged 47 unreviewed PRs straight "
    "to production, and the only bug it fixed was my employment."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
