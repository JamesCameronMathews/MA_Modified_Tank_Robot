import pyaudio
import numpy as np
from pydub import AudioSegment
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import audio
AudioClassifier = mp.tasks.audio.AudioClassifier
AudioClassifierOptions = mp.tasks.audio.AudioClassifierOptions
AudioRunningMode = mp.tasks.audio.RunningMode
BaseOptions = mp.tasks.BaseOptions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.framework.formats import classification_pb2
from mediapipe.tasks.python.components import containers
from mediapipe.tasks.python import audio
from scipy.io import wavfile

# Set the audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 80000  # You can adjust the sample rate as needed
CHUNK = 100024  # Size of each audio chunk to process in milliseconds

AudioData = mp.tasks.components.containers.AudioData

##### TESTING
# # Customize and associate model for Classifier
# base_options = python.BaseOptions(model_asset_path='C:\\Users\\James\\CodeProjects\CatBot\\yamnet.tflite')
# options = AudioClassifierOptions(
#     base_options=base_options, max_results=4)

# # Load the audio file
# audio = AudioSegment.from_file("cat-meow5.wav")

# # Convert to PCM format
# pcm_audio = audio.set_frame_rate(44100).set_sample_width(2).set_channels(1)

# # Export the PCM audio
# pcm_audio.export("cat-meow5_pcm.wav", format="wav")

# # Create classifier, segment audio clips, and classify
# with AudioClassifier.create_from_options(options) as classifier:
#   #sample_rate, wav_data = wavfile.read("C:\\Users\\James\\CodeProjects\\CatBot\\cat-meow5_pcm.wav")
#   sample_rate, wav_data = wavfile.read("C:\\Users\\James\\Downloads\\baby-crying-01.wav")
#   audio_clip = containers.AudioData.create_from_array(
#       wav_data.astype(float) / np.iinfo(np.int16).max, sample_rate)
#   classification_result_list = classifier.classify(audio_clip)
#   print(classification_result_list)

# # Initialize variables to store whether "cat" and "meow" are in the top three scores
# cat_in_top_three = False
# baby_in_top_three = False

# # Iterate through clips to display classifications
# for idx, classification_result in enumerate(classification_result_list):
#     # Get the top three categories
#     top_categories = classification_result.classifications[0].categories[:3]

#     # Iterate over the top three categories
#     for rank, category in enumerate(top_categories, start=1):
#         print(f'{rank} Most likely source of sound: {category.category_name} ({category.score*100:.2f}%)')
#         # Check if "cat" or "meow" are in the top three categories
#         if category.category_name.lower() == "cat":
#             cat_in_top_three = True
#         elif category.category_name.lower() == "meow":
#             cat_in_top_three = True
#         if category.category_name.lower() == "baby":
#             baby_in_top_three = True

# # Check if "cat" or "meow" are in the top three scores
# if cat_in_top_three:
#     print("Cat detected. Activating patrol mode.")
# if baby_in_top_three:
#     print("Baby detected. Going dark.")

# # Define a callback function to process audio classification results
# def result_callback(results):
#     if isinstance(results, classification_pb2.ClassificationList):
#         for result in results.classification:
#             print("Class:", result.label, "Score:", result.score)
########

#### Streaming mode #####
# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream for audio input
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Customize and associate model for Classifier
base_options = python.BaseOptions(model_asset_path='C:\\Users\\James\\CodeProjects\CatBot\\yamnet.tflite')
options = AudioClassifierOptions(
    base_options=base_options, max_results=4, running_mode=AudioRunningMode.AUDIO_CLIPS
    #, result_callback=result_callback
    )

with AudioClassifier.create_from_options(options) as classifier:
    # Start audio classification
    try:
        while True:
            # Read audio data from the stream
            audio_data = stream.read(CHUNK)
            # Create an AudioData object from the audio data
            audio_data_obj = AudioData.create_from_array(np.frombuffer(audio_data, dtype=np.int16) / np.iinfo(np.int16).max, RATE)
            # Send audio data to the classifier
            classification_result_list = classifier.classify(audio_data_obj)
            #print(classification_result_list)
            # Iterate through clips to display classifications
            for idx, classification_result in enumerate(classification_result_list):
                # Get the top three categories
                top_categories = classification_result.classifications[0].categories[:3]
                # Iterate over the top three categories
                for rank, category in enumerate(top_categories, start=1):
                    print(f'{rank} Most likely source of sound: {category.category_name} ({category.score*100:.2f}%)')
                    # Check if "cat" or "meow" are in the top three categories
                    if category.category_name.lower() == "cat":
                        cat_in_top_three = True
                    elif category.category_name.lower() == "meow":
                        cat_in_top_three = True
                    if category.category_name.lower() == "animal":
                        cat_in_top_three = True
    except KeyboardInterrupt:
        pass

    