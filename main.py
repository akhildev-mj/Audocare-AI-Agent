from dotenv import load_dotenv
from livekit import agents

from src.pipeline_model import pipeline_entrypoint
from src.realtime_model import realtime_entrypoint
from src.shared.constants import PIPELINE_MODE, REALTIME_MODE

load_dotenv()


MODE = PIPELINE_MODE
entrypoint_fnc = pipeline_entrypoint if MODE == PIPELINE_MODE else realtime_entrypoint

if __name__ == "__main__":
    print(f"\nAvailable modes: {PIPELINE_MODE}, {REALTIME_MODE}")
    print(f"\nRunning in {MODE} mode\n")
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint_fnc))
