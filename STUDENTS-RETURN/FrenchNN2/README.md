# french_speech_rec


The language used here is "french" and the text was extrated from the pages 

- https://fr.wikipedia.org
- https://fr.wikipedia.org/wiki/Histoire_de_l%27Afrique#:~:text=L'histoire%20de%20l'Afrique,sur%20le%20reste%20du%20globe
- https://fr.wikipedia.org/wiki/Roman_historique
- https://fr.wikipedia.org/wiki/Histoire_du_Cameroun#:~:text=Le%20Cameroun%20fran%C3%A7ais%20acquiert%20son,ethniques%20notamment%20en%20pays%20bamil%C3%A9k%C3%A9.


We created 14 text files which allows us tu records using the LIG-Aikuma app, we then get 14 sections recorded  that make up a total of 2hrs.Inside each section folder, we have the recording itself (.wav file), the json file and the .txt file.

### Data preprocessing

As the model code requiert a certain format, we need to preprosesse our data so that it will fit the model requierement.
We first start by calculating the total number of hour by using a script which browses the recording folder and get just the .wav and gives us the total number , the number of files and the number of the corrupted files.

Secondly, we organize our data by spliting the records folder into train, val and test sets.we then make a char file that will concatenate the audio name with the coding sentence and, a charset file that will contain all the characteres we used in our sentences.

Now that our datas are ready, we will pass them to the training to see hoe it performs.

### Build the model

we build and train a small CPC model using the repository CPC_audio, we first loads a context and an encoder newtorks, create a CPCmodel class
 
### Fine tuning
To fine tune the model, we first build a CharacterClassifier that will take as input a batch of sequences of CPC features and output a score vector for each phoneme, then we evaluate the Character Error Rate (CER), we Evaluate the PER on the validation dataset

### Characters recognition without pre-training
We estimate the impact of the pre-training by estimating the CER of a model trained from scratch on the labelled dataset.
