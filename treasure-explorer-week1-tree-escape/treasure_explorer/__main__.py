import argparse
import json

from .runner import run
from .viewer import TerminalViewer

parser = argparse.ArgumentParser(description="Run a Treasure Explorer bot")
parser.add_argument("--map", required=True)
parser.add_argument("--agent", required=True)
parser.add_argument("--seed", type=int, default=0, help="reserved for deterministic hidden evaluation")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--view", action="store_true", help="show the map and agent state after every turn")
parser.add_argument("--delay", type=float, default=0.15, help="viewer delay in seconds")
args = parser.parse_args()
viewer = TerminalViewer(args.delay) if args.view else None
print(json.dumps(run(args.map, args.agent, args.verbose, viewer), ensure_ascii=False, sort_keys=True))
