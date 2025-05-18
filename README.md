# Audocare: AI Voice Agent for Symptom Assessment

Welcome to the **Audocare AI Voice Agent** project — an intelligent, speech-driven assistant that engages users in real-time conversations to detect and assess symptoms of illness. Built using advanced AI models and real-time voice streaming technology, this agent is capable of empathetic, multi-turn health conversations using speech input/output.

## 🧠 Project Summary

Audocare utilizes **AI voice communication** to interact with users, gather health-related symptoms, and assist in preliminary assessment. It supports two execution modes — pipeline and real-time — both powered by OpenAI models, with options to integrate ElevenLabs for high-quality voice output.

Key features include:

- Symptom-aware conversational AI via LLMs
- Real-time voice interaction using LiveKit
- Dual-mode operation for flexibility and speed
- Integration with ElevenLabs, OpenAI, and Silero
- Runs locally with minimal setup

## 🧪 Use Case: Intelligent Health Conversation

Audocare is designed for scenarios like:

- Preliminary health triage
- Elderly assistance
- Voice-first patient intake
- Accessible health interaction for visually impaired users

It actively listens to symptoms and responds with contextual, follow-up questions to understand the user's condition.

## 📁 Project Structure

| File / Folder                   | Description                                                        |
| ------------------------------ | ------------------------------------------------------------------ |
| 📁 `src/shared/`               | Shared logic and configurations.                                   |
| ├── `constants.py`             | Global constants including modes, models, and voice IDs.           |
| ├── `assistant.py`             | Custom agent built using LiveKit’s Agent API.                      |
| ├── `pipeline_model.py`        | Implements pipeline-based architecture with OpenAI + ElevenLabs.   |
| ├── `realtime_model.py`        | Implements real-time voice interaction using OpenAI's realtime API.|
| 📄 `.env`                      | Environment variables.                                             |
| 📄 `main.py`                   | Entrypoint for CLI commands and LiveKit agent startup.             |
| 📄 `pyproject.toml`            | Project dependencies and metadata.                                 |
| 📄 `uv.lock`                   | Lockfile for reproducible environments.                            |
| 📄 `README.md`                 | This file.                                                         |

## 🚀 How It Works

Audocare supports two voice interaction modes:

### 🔹 Pipeline Mode

Uses OpenAI for STT and LLM, ElevenLabs for TTS, and Silero VAD.

### 🔹 Real-Time Mode

Uses OpenAI’s unified real-time model for STT, LLM, and TTS.

## 🧑‍💻 Setup Instructions

### 1. Install and Start LiveKit (locally)

Follow the official LiveKit documentation to install and run a local LiveKit server instance.

### 2. Clone the Repository

```bash
git clone <>
cd audocare-ai-agent
```

### 3. Set Up Environment Variables

Create a .env file in the root with relevant API keys and environment configs.

### 4. Download Required Files

```bash
uv run main.py download-files
```

### 5. Run the Livekit Server

```bash
livekit-server --dev
```

### 6. Run the Agent

#### Start the voice agent

```bash
uv run main.py start
```

#### Run in development mode

```bash
uv run main.py dev
```

#### Use the console mode

```bash
uv run main.py console
```

## 📦 Dependencies

All dependencies are Python 3.12+ compatible.

- livekit-agents[openai, elevenlabs, silero, turn-detector]
- livekit-plugins-noise-cancellation
- openai
- dotenv
- python-dotenv

## 🎯 Outcome

This project showcases how to build an intelligent, voice-based healthcare assistant that can interpret symptoms conversationally. Audocare merges modern LLMs, real-time voice streaming, and intelligent turn detection for a natural, voice-first user experience in healthcare tech.

Thank you for exploring Audocare!
Feel free to fork, enhance, or contribute 🤖
