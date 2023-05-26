# README.md

---

## Voice-Activated OpenAI GPT-4 Assistant

This project is a voice-activated assistant using OpenAI's GPT-4. It records the user's voice, transcribes it, feeds it to the GPT-4 model, and plays back the response using text-to-speech. It also measures the time taken for each step in the process.

### Setup and Usage

#### Prerequisites
- Python 3.8+
- OpenAI API key
- Required Python packages: `PyQt5`, `sounddevice`, `numpy`, `openai`, `gTTS`, `pydub`, `scipy`

#### Installation

1. Clone the repository:
    ```
    git clone https://github.com/mh-nyris/openAI.git
    ```

2. Navigate into the project directory:
    ```
    cd openAI
    ```

3. Install the necessary packages:
    ```
    pip install -r requirements.txt
    ```
    Note: It's recommended to do this in a virtual environment to avoid installing packages globally.

## Additional Installations

This project also depends on a few packages that need to be installed via Homebrew:
```
brew install ffmpeg
```
ffmpeg is required for pydub to work correctly.

#### Usage

1. Replace `"placeholder"` in the following lines of code with your own OpenAI API credentials:
    ```python
    openai.organization = "placeholder"
    openai.api_key = 'placeholder'  # Replace with your OpenAI key
    ```

2. Run the script:
    ```
    python voice-communication-gpt4.py
    ```

3. Interact with the application GUI to start and end voice recording.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details