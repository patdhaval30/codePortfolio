# codePortfolio
# Project name: Youtube video summary creator with Gen AI Llama 2
>Readme for CS50 - Introduction to python final project.

## Concept
- Enter a youtube video url and get its summary. <br/>
- This entire project is made with open source components.<br/>
- After youtube video url is entered in python, we first get its transscript with youtube-transcript-api. Alternatively youtube API can be used but it has a daily limit. Youtube_dll can also be used but it downloads the videos and then gives the details. <br/>
- After that we use requests to get the youtube video web page. This webpage is converted to text format and passed to beautiful soup which helps to find the video title.<br/>
- After getting the video title and transcript, they are passed as a prompt to llama model. Content window size is set to 10000 after testing.<br/>
- Llama 2 7Billion model is chosen for this project. This decision has been made due to following CPU constraints as it is run locally. There are 13 Billion and 70 Billion models available as well.<br/>
- Another way to run llama 2 is on replicate using their server and GPUs but after ~75 requests it will start charging for each request, so it was decided to run Lama Gen AI locally.<br/>
- We are using quantized LLMs so that they can be run locally on laptop CPU free of cost.<br/>
- The model has to be run twice or more on a same youtube video to get the best summary.<br/>

## Function description
- **get_youtube_video_transcripts(url)**: This function takes youtube video url entered by user an an argument and returns transcript of the video. To get the transcript it must be ensured that captions are enabled for the video. To get the transcript python package [YouTubeTranscriptApi](https://pypi.org/project/youtube-transcript-api/) is used.
- **get_youtube_video_title(url)**: This function takes youtube video url entered by user an an argument and returns title of the video. To get the title first we get the youtube video web page's html code in text form with package [requests](https://pypi.org/project/requests/). This html code is passed to package [beautiful soup](https://pypi.org/project/beautifulsoup4/). This module scrapes the entire html code and finds the title tag from which the video title is read and returned by the function.
- **connect_to_llama(transcript, title)**: This function takes the transcript and title returned by above 2 functions as arguments and prints the summary of the video. To get the summary the title and the transcript are passed to Llama2 7B model with the prompt.<br/>
  >f"Title of the document is {title}. Document contains following text: {transcript}. What are the important points from the document?".<br/>
- This model is downloaded from [hugging face](https://huggingface.co/TheBloke/Llama-2-7B-GGUF) and run with python package [llama-cpp](https://pypi.org/project/llama-cpp-python/). For optimization we need to set the context size of the model with n_ctx parameter in Llama function (read the llama cpp package documentation for details and   more fine tuning options). This controls length of the prompt.

## Limits:
- Based on context window size and CPU capacity of the laptop we can get summary of max 45 min video.
- Only english videos can be summarised.
