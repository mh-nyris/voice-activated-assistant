import os
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import openai
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import time

class RecordThread(QThread):
    data_ready = pyqtSignal(np.ndarray)

    def __init__(self, samplerate=16000, chunk_size=10):  # Increase chunk_size to 1 second
        super().__init__()
        self.samplerate = samplerate
        self.chunk_size = chunk_size
        self.record = False
        self.chunks = []  # List to store chunks of audio data

    def run(self):
        self.record = True
        self.chunks = []
        while self.record:
            mydata_chunk = sd.rec(int(self.samplerate * self.chunk_size), samplerate=self.samplerate, channels=1, blocking=True)
            self.chunks.append(mydata_chunk)

        self.mydata = np.concatenate(self.chunks)  # Concatenate the chunks after recording
        self.data_ready.emit(self.mydata)

    def stop(self):
        self.record = False
        sd.stop()



class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.recording_thread = RecordThread()
        self.recording_thread.data_ready.connect(self.save_data)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.start_button = QPushButton('Start Recording', self)
        self.start_button.clicked.connect(self.start_recording)

        self.end_button = QPushButton('End Recording', self)
        self.end_button.clicked.connect(self.end_recording)

        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)

        self.setLayout(vbox)
        self.setWindowTitle('Voice Recorder')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_recording(self):
        self.start_button.setEnabled(False)
        self.end_button.setEnabled(True)
        self.recording_thread.start()

    def end_recording(self):
        self.start_button.setEnabled(True)
        self.end_button.setEnabled(False)
        self.recording_thread.stop()

    def save_data(self, data):
        start_time = time.time()
        
        write('user_input_voice_recording.wav', self.recording_thread.samplerate, data)
        write_time = time.time()
        print("Time taken for writing audio file: {:.2f} seconds".format(write_time - start_time))

        # Remaining processing code
        openai.organization = "placefolder"
        openai.api_key = 'placeholder'  # Replace with your OpenAI key
        
        start_time = time.time()
        audio_file = open("user_input_voice_recording.wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        transcribe_time = time.time()
        print(transcript["text"])
        print("Time taken for transcription: {:.2f} seconds".format(transcribe_time - start_time))

        start_time = time.time()
        gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcript["text"]},
        ]
        )
        api_time = time.time()
        print("Time taken for API call: {:.2f} seconds".format(api_time - start_time))

        start_time = time.time()
        gpt_res_text = gpt_response['choices'][0]['message']['content']
        print(gpt_res_text)  # Print text response of ChatGPT

        # Create a gTTS object with the text to be converted
        gpt_res_t2s = gTTS(gpt_res_text)

        # Save the audio file
        gpt_res_t2s.save("gpt-response-text-to-speech.mp3")
        tts_time = time.time()
        print("Time taken for text-to-speech: {:.2f} seconds".format(tts_time - start_time))
        
        # Get the directory of the current file (__file__)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the path to the mp3 file
        audio_file_path = os.path.join(current_dir, "gpt-response-text-to-speech.mp3")

        # Load the audio file
        audio = AudioSegment.from_mp3(audio_file_path)

        # Play the audio file
        play(audio)
        self.close()

           


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())