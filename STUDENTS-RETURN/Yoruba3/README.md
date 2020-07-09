# AMMI_2020_SPEECH_RECOGNITION_PROJECT
This is a project that deals with the transcription of a local language named Yoruba from the South West, Nigeria, Africa generated in .txt file and transcribed into .wav file for a Text To Speech Task.Text to Speech Task was performed using customized audio data. A Case study of Yoruba Language; 
Speech Recognition is is an interdisciplinary subfield of computer science and computational linguistics that develops methodologies and technologies that enable the recognition and translation of spoken language into text by computers. There are three categories of these concepts namely: Text To Speech(TTS); Automatic Speech Recognition(ASR) and Speech To Text(STT). 

# DATA COLLECTION:
The following stteps were taken in collecting data for the TTS
1. transcribing of text into an electronic format of .txt; the .txt file were organised into sessions, each session comprises of minimum of fifty(50) senetences.
2. Downloading and installing of the  LIG Aikuma API on an Android phone, to enable the transcription of the .txt file  to audio format of .wav.
3. On the LIG Aikuma API, the elicitation by Text was performed on each session of .txt file; which serves as input and the output were .json, .wav and linker file.
4. The output from the Android API was transferred to the laptop for preprocessing.
5. the audio files(.wav) were timed using vlc application and it reported a total of 2hrs 26 seconds.

# TEXT PRE-PROCESSING
Text preprocessing is an act of cleaning and preparing text data. In this project, the pre-processing was performed by developing a python script named: generate.py. This script was used to define the set of characters used in the yoruba language; it was also used to remove corrupted files in the data set, it was used to derive the all_session.txt file which was used for the model implementation. The all_session.txt file was tokenized and encoded into numeric format. 
The dataset was splitted into: train, validation and test using the ratio of 40%, 20%, and 1 hour respectively.

# MODEL TRAINING
In other to train the model, python libraries such as torchaudio, PyDrive, soundfile were installed and GoogleAuth, GoogleDrive, GoogleCredentials were imported using Python programming language in Colab environment. The task performed at this stage:

a. Contrastive Predictive Coding(CPC): The raw audio wave was paased through  the convolutional network encoder; then, the encoder’s output was given to a recurrent network that is the context. The prediction network was used to predict the furure embeddings of the encoder using the output of the context network.
b. Generating the CPC Loss: The CPCCriterion  was used to hold the prediction networks and the classification loss L was derived. The training loop was implemented using Adam optimizer, the dataloader provided by the CPC_audio library was used. An average Loss of 4.87 was derived at the end of the training loop.
c. The model parameters were Fine tunned by:
1. Performing Phone separability with aligned phonemes that is using CPC to recognise phonemes. An evaluation setting was trained in which there is phone labels for each timestep. A simple linear classifer was used to recognise the phonemes from the features prodiuced by cpc_model. Parameter: learning rate used: 2e-4 and Adam optimizer. The output of the Fine tuning gave an average loss of 3.445 and average accuracy of 0.0855 for validation dataset and 3.270 and 0.115 for average loss and average accuracy.
2. Performing Phone separabilty without alignment(PER)
In this case, the functions: tain_one_epoch_ctc, validation_step_ctc and run_ctc was implemented.

3. Performing Character Error Rate(CER)
This involves the use of Characters instead of Phonemes in evaluating the performance of the cpc-model. 

# Problems Encountered and Solution:
The following problems were encountered:
1. Corrupted .wav files: some .wav files were observed to be corrupted duing the preprocessing stage, which made it difficult for such files to the read by the scripts.
Solution: This was addressed using the preprcoessing code(generate.py), the corrupted files were scanned out and removed.
2. Unformatted text/sentences: it was observed that some sentences in the session were not preceeded with “##”, which made it difficult for the  LIG Aikuma API to read the text file as a .txt file.
Solution: the .txt files with these omission were identified and amended.
3. Uncaptured Character: During the preprocessing, it was observed that some characters were not captured in the list of alphabets allowed in the yoruba language; these uncaptured characters were reported as “Key Error”
Solution: generate.py script which was written was used to fix the problem and the set of alphabets were updated.

# Original Author: Esther Oduntan






