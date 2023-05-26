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
    git clone https://github.com/username/repository.git
    ```
    Replace `username` and `repository` with your GitHub username and repository name.

2. Navigate into the project directory:
    ```
    cd repository
    ```
    Replace `repository` with your repository name.

3. Install the necessary packages:
    ```
    pip install -r requirements.txt
    ```
    Note: It's recommended to do this in a virtual environment to avoid installing packages globally.

#### Usage

1. Replace `"placeholder"` in the following lines of code with your own OpenAI API credentials:
    ```python
    openai.organization = "placeholder"
    openai.api_key = 'placeholder'  # Replace with your OpenAI key
    ```

2. Run the script:
    ```
    python main.py
    ```
    Note: Replace `main.py` with your script name if different.

3. Interact with the application GUI to start and end voice recording.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---

## Setting up a Git Repository

Here are the basic steps to set up a git repository for your project:

1. First, navigate to the project's directory using the command line.

2. Then, initialize a new git repository with this command:
    ```
    git init
    ```

3. Now, you can add all project files to the repository using:
    ```
    git add .
    ```
    Note: The `.` adds all files in the current directory to the staging area.

4. Commit these changes with a message using:
    ```
    git commit -m "Initial commit"
    ```

5. If you plan to push your code to GitHub, create a new repository on GitHub.

6. Link the local repository to the remote repository on GitHub with:
    ```
    git remote add origin https://github.com/username/repository.git
    ```
    Replace `username` and `repository` with your GitHub username and repository name.

7. Finally, push your local commits to the remote repository with:
    ```
    git push -u origin master
    ```

Congratulations, your project is now on GitHub! Make sure to update the README.md file as needed when making changes to your project.
