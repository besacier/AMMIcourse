## Malagasy audio dataset

The repository raw_recordings contains the direct output of lig-aikuma after recording. It contains 59 folders, each containing around 50 audio accompanged with .json files describing each of them. 

- mlg_data contains 
	- a text file transcriptions.txt containing the audio names and their transcriptions, in the format 
		audio_name.wav, TRANSCRIPTION
	- A folder containing all the audios retrieved from the raw_recordings folder, that are not corrupted. This is the dataset used in the .ipynb file. 

- txt_files contains 64 text files that were taken as input for the elicitation by text in lig-aikuma

- MG_ASR.ipynb is a notebook with the codes training one ASR system on the data.


### Contributors 
Emmanuella Sandratra Rambeloson and Andriamahazoosa Dimbinantenaina Rabeariony, AMMI Ghana.
