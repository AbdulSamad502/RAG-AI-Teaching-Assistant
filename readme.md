## How to use RAG_AI Teacing Assistant on your own data.
## Step-1:- Collect all your videos 
Move all your videos file to videos folder.

## Step-2:- Convert to mp3
Convert all your video file to mp3 by running video_to_mp3.

## Step-3:- Convert mp3 to json
Convert all your mp3 files to json by running mp3_to_json.

## Step-4:- Convert the json file to vectors
Use the file pre_process_json to convert the json file to a data frame with embeddings and save it as a joblib pickle.

## Step-6:- Prompt generation and feeding to LLM
Read the joblib file and load it to the memory. Then create a relevent prompt as per the user query and feed it to the LLM.