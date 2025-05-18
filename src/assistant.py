from livekit.agents import Agent

from src.shared.constants import ASSISTANT_INSTRUCTIONS


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=ASSISTANT_INSTRUCTIONS)
