import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# The grader provides a writable /output, but make sure the directory exists
# so the program never fails on a missing folder.
os.makedirs(output_dir, exist_ok=True)

joke = "I asked my coding agent to fix one bug. It fixed it, introduced three new ones, then billed me for 'refactoring the codebase's emotional state.'"

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(joke)
