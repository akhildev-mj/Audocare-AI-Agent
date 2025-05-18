from livekit import agents
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import elevenlabs, noise_cancellation, openai, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from src.assistant import Assistant
from src.shared.constants import PIPELINE_ELEVENLABS_VOICE_ID, PIPELINE_LLM_MODEL


async def pipeline_entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=openai.STT(),
        llm=openai.LLM(model=PIPELINE_LLM_MODEL),
        tts=elevenlabs.TTS(voice_id=PIPELINE_ELEVENLABS_VOICE_ID),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )

    await ctx.connect()
