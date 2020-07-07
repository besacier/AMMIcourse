# Nigerian_Hausa_Speech_project

### Overview

I was previlledge to have been taught a course on Speech Recognition at the [African Masters for Machine Intelligence](https://aimsammi.org/) program, the course was given by Gabriel Synnaeve, Neil Zeghidour, Laurent Besacier and Emmanuel Dupoux.

Nigerian Hausa or Hausa (as most people call it) is a language widely spoken in the northern part of Nigeria and also in many africa countries including Ghana. 

To clone this repo, go to your terminal and enter the link below;

```git
git clone https://github.com/BlessingBassey/Nigerian_Hausa_Speech_project
```
### The APP and Data Collection for the Project:

The speech recording of this project was done using the 
[Lig-Aikuma](https://lig-aikuma.imag.fr/tutorial/) Android app. It is a data collection App for language documentation. It proposes a range of different speech collection modes as follows;

- Recording : A Free recording of spontaneous speech
- Respeaking : Respeaking of a recording (previously recorded with the app or loaded from a wav file)
- Translating : Translation of a recording (previously recorded or loaded)
- Elicitation : Elicitation of speech from a text file, an image or a video, by loading it within the app

For the data collection process, the text dataset used was collected from [AfriSauti Hausa Text Corpus](https://github.com/afrisauti/hausa_text_corpus).

### The Frog Story Tutorial:

The folder called `frog-story` consist of the Mercer Mayer wordless picture book of 1969 Frog (saved as frog story file), the image-by-image version of the book. Using the app discussed earlier, the `speech elicitation by image` was done on each of the pictures, using the Nigerian Hausa Language, afterwards, each of the short speech were then concatenated using the online tools and then converted to `wav` file. Furthermore, the `translation` of the elicitated speech was done in the `Hausa language`.

### The Project:

The folder called `project` contains over 2 hours of recorded Nigerian Hausa text recoreded by a native speaker, text data was from [AfriSauti
 Hausa Text Corpus](https://github.com/afrisauti/hausa_text_corpus) as discussed in the `The APP and Data Collection for the project` paragraph.

##### Data Arrangement
 
The `project/data` folder, contains the recordings and allignment text. The recordings have been splitted into train, val and test

#####  Data Preprocessing
 
After the recordings had been done, the next thing was to preprocess the data in the right format for CPC/CTC experiments. The lig-aikuma  App gives a wav file aligned to transcripts (the info about the link between txt and wav can be found in the ***_elicit_link.txt files). All preprocessing can be accessed through the notebook `Nigerian_Hausa_preprocessing.ipynb` , 
 
Note that a python installation is required as well as some dependencies;

- numpy
- wave
- contextlib


##### Step 3 : Data Spliting

Still in the `Nigerian_Hausa_preprocessing.ipynb`.
- The period of speech recorded was around `1.7 hours`.
- Corrupted files were discarded.
- Organizing the data by matching the recoding to its corresponding label text file using the linkers in each of the sections, this is found in the `project/data/raw_text_file.txt` file.
- Then the date was split into train, val and text set, this are found in `project/data/records`folder
- We also have the `chars.txt` file which contains the recordings and the corresponding indexis of each characters in the text file. 
- finally, the `charset.txt` files each of the characters and their frequency.

### Application

The dataset can be useful especially for low-resource speech modelling. NLP in Africa is still in its infancy; of about 2000 languages, a very few have  featured  in  NLP  research  and  resources, This project will add to the language  resources  for  Nigeria  as  part  of  a  corpus-based  project, This project can be useful if fine-tune on high-resource data like LibriSpeech for a Speech-to-text project. 

### chalenges
- The lig-aikuma app has so many versions, all were tried on my andriod mobile phone but unfortunately none worked for me (maybe they were not compatible with my phone), hence, I was left with the option of using an android studio version on my computer system.
- During the recording section, surrounding noice were very difficult to elliminate totally.
