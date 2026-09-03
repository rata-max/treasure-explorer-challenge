import argparse
import json
from pathlib import Path

from .runner import run
from .viewer import TerminalViewer


parser = argparse.ArgumentParser(description="Run a Treasure Explorer agent")
parser.add_argument("--map", required=True)
parser.add_argument("--agent", required=True)
parser.add_argument("--replay")
parser.add_argument("--view", action="store_true", help="animate the map after every action")
parser.add_argument("--delay", type=float, default=0.20, help="seconds between frames")
parser.add_argument("--no-clear", action="store_true", help="print every frame instead of animating in place")
args = parser.parse_args()

viewer = TerminalViewer(args.delay, clear=not args.no_clear) if args.view else None
result, history = run(args.map, args.agent, observer=viewer)

if args.replay:
    Path(args.replay).write_text(
        json.dumps({"result": result, "history": history}, indent=2),
        encoding="utf-8",
    )

print(json.dumps(result, ensure_ascii=False, sort_keys=True))

