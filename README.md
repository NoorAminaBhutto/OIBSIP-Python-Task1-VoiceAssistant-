# Python Voice Assistant — OIBSIP Task 1

**Track:** Python Programming  
**Task:** Task 1 — Voice Assistant  
**Level:** Beginner implementation with selected advanced extensions  
**Runtime:** Google Colab (browser microphone)  
**Language:** Python

## Project overview

This project is a Python voice assistant that captures speech through the browser microphone in Google Colab, converts speech to text, responds to common commands, announces the current date and time, opens web searches, and supports timed reminders. It includes error handling and a small local knowledge base for simple questions.

> **Important:** This version is designed for Google Colab because the microphone capture uses browser JavaScript. It is not a standalone desktop app without adaptation.

## Features

### Beginner checklist
- [x] Capture voice input using the browser microphone in Colab.
- [x] Respond to greetings such as “hello”.
- [x] Tell the current time and date.
- [x] Open a web search for a spoken topic.
- [x] Handle empty, unclear, and recognition errors gracefully.
- [x] Speak responses using the Colab runtime's `espeak` tool (audio output availability may vary); also prints every response as text.

### Additional features
- [x] Basic natural-language intent handling (phrases such as “what time is it?”).
- [x] Timed reminders, for example “remind me in 10 seconds to stretch”.
- [x] Local knowledge-base answers for a few general questions.
- [x] Custom commands can be added in the `CUSTOM_COMMANDS` dictionary.
- [x] Privacy notes and setup instructions.

### Optional advanced extensions not enabled by default
- Weather API and email sending are intentionally not enabled in the starter project because they require API credentials or email account configuration. Never put API keys, passwords, or app passwords in a public repository. If you add these features, load secrets from environment variables or Colab Secrets.

## Run the project

1. Open [Google Colab](https://colab.research.google.com/).
2. Select **File → Upload notebook** and upload `voice_assistant.ipynb`, or open the notebook after uploading it to GitHub.
3. Run the setup cell.
4. Run the assistant cell.
5. Allow microphone access if the browser asks.
6. Click **Start recording**, speak one command, and click **Stop recording**.
7. Try commands listed below. Run the assistant cell again if you stop it.

## Example commands

- `Hello`
- `What time is it?`
- `What's today's date?`
- `Search for Python tutorials`
- `Remind me in 10 seconds to take a break`
- `What is Python?`
- `Stop assistant`

Speech recognition uses Google's online recognition service through the `SpeechRecognition` library, so internet access is needed for transcription. Recognition accuracy depends on microphone quality, noise, language, and network connectivity.

## Repository contents

```text
Python-L1-Task1-VoiceAssistant/
├── README.md
├── voice_assistant.ipynb
├── voice_assistant.py
├── requirements.txt
├── .gitignore
├── DEMO_VIDEO_GUIDE.md
├── LINKEDIN_POST.md
├── outputs/
│   └── test_checklist.md
└── screenshots/
    └── README.md
```

## Dependencies

The Colab notebook installs system audio tools (`espeak` and `ffmpeg`) in its setup cell, then installs the Python packages. See `requirements.txt`.

## Privacy and safety

- The microphone is accessed only after the user clicks the recording control and grants browser permission.
- Speech is sent to Google's online speech-recognition service for transcription.
- The program prints recognized commands and responses in the notebook output.
- Do not speak or enter passwords, private messages, financial details, or other sensitive information.
- The project does not send email or call a weather API in its current version.
- The public repository must not contain credentials, API keys, tokens, or personal data.

## Testing checklist

Use `outputs/test_checklist.md` to record actual test results. Do not claim a test passed unless you have run it on your own device.

## Demo video

Follow `DEMO_VIDEO_GUIDE.md`. At the start of the recording, display a clear 2-second title card with:
1. Your full name
2. Your assigned track: Python Programming
3. Task title: Task 1 — Voice Assistant

Then demonstrate the running assistant end-to-end, not only screenshots.

## Submission workflow

The internship guide specifies one shared repository named exactly `OIBSIP`. If you have already created a separate repository named `Python-Voice-Assistant`, follow your mentor's instruction before creating another repository. Ideally, place this folder inside the required repository using this path:

`OIBSIP/Python-L1-Task1-VoiceAssistant/`

Commit the source code, README, and genuine screenshots/output evidence. Then record the demo video and publish the video or its link in a LinkedIn post. The guide also asks interns to tag **Oasis Infobyte**, include `#oasisinfobyte`, and use relevant hashtags such as `#python` and `#internship`.

## License

Educational internship project. Add a license if your program or mentor requires one.
