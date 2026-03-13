# RAG AI Teaching Assistant

An AI-powered **Retrieval-Augmented Generation (RAG) assistant** that converts video lectures into a searchable knowledge base and answers user questions using Large Language Models (LLMs).

This project processes video content through multiple stages: extracting audio, generating transcripts, creating embeddings, and retrieving relevant information to generate intelligent responses.

---

## 🚀 Project Workflow

The system follows a pipeline to convert raw video lectures into an AI-powered assistant.

### Step 1: Collect Video Files

Place all your lecture videos inside the `videos/` folder.

```
project/
 └── videos/
```

### Step 2: Convert Videos to Audio

Run the script:

```
python video_to_mp3.py
```

This converts video files into `.mp3` audio files.

### Step 3: Convert Audio to JSON

Run:

```
python mp3_to_json.py
```

This step performs **speech-to-text transcription** and stores the text in JSON format.

### Step 4: Generate Embeddings

```
python pre_process_json.py
```

This step:

* Reads JSON transcripts
* Creates embeddings
* Saves them as a **joblib file**

### Step 5: Retrieval & Prompt Generation

When a user asks a question:

1. Load the embeddings database
2. Retrieve relevant transcript chunks
3. Create a contextual prompt
4. Send the prompt to the LLM
5. Generate the final response

---

## 🧠 Tech Stack

* Python
* Speech-to-Text Processing
* Embeddings / Vector Search
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)

---

## 📂 Project Structure

```
RAG-AI-Assistant
│
├── videos/
├── audios/
├── jsons/
│
├── video_to_mp3.py
├── mp3_to_json.py
├── pre_process_json.py
├── process_incoming.py
│
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Abdul Samad**

GitHub: https://github.com/AbdulSamad502
