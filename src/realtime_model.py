from livekit import agents
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import noise_cancellation, openai

from src.assistant import Assistant
from src.shared.constants import REALTIME_LLM_MODEL, REALTIME_MODEL_VOICE


async def realtime_entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            model=REALTIME_LLM_MODEL, voice=REALTIME_MODEL_VOICE
        )
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )

    await ctx.connect()
