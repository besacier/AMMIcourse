# Nigerian_Pidgin_Speech_project

### Overview

I was previlledge to have been taught a course on Speech Recognition at the [African Masters for Machine Intelligence](https://aimsammi.org/) program, the course was given by Gabriel Synnaeve, Neil Zeghidour, Laurent Besacier and Emmanuel Dupoux.

Nigerian Pidgin or Pidgin (as most people call it) is an English-based pidgin and creole language (a stable natural language developed from a mixture of different languages. It's a simplified form develops as a means of communication between two or more groups) in Nigeria. 

To clone this repo, go to your terminal and enter the link below;

```git
git clone https://github.com/BlessingBassey/Nigerian_Pidgin_Speech_project
```
### The APP and Data Collection for the Project:

The speech recording of this project was done using the 
[Lig-Aikuma](https://lig-aikuma.imag.fr/tutorial/) Android app. It is a data collection App for language documentation. It proposes a range of different speech collection modes as follows;

- Recording : A Free recording of spontaneous speech
- Respeaking : Respeaking of a recording (previously recorded with the app or loaded from a wav file)
- Translating : Translation of a recording (previously recorded or loaded)
- Elicitation : Elicitation of speech from a text file, an image or a video, by loading it within the app

For the data collection process, the text dataset used was collected from [The Jehovah Witness People](https://www.jw.org/pcm/wetin-we-get/different-different-book/jesus/). The text consist of different Bible stories, for the purpose of this project, I choosed to study the life of Jesus. His birth as well as his mission before he aceended to the father. The motivation behind this text was because the life of Jesus teaches humility, and this is worth emulating by anyone. 

### The Tutorial:

The folder called `tutorial` consist of the Mercer Mayer wordless picture book of 1969 Frog (saved as frog story file), the image-by-image version of the book. Using the app discussed earlier, the `speech elicitation by image` was done on each of the pictures, using the Nigerian Pidgin, afterwards, each of the short speech were then concatenated using the online tools and then converted to `wav` file. Furthermore, the `translation` of the elicitated speech was done in the `ibibio language`. These two languages are from the western and southen part of Nigeria respectively. The tutorial was to prepare us for the main project discussed below.

### The Project:

The folder called `project` contains over 2 hours of recorded Nigerian Pidgin text recoreded by an Ibibio native speaker, text data was from [The Jehovah Witness People](https://www.jw.org/pcm/wetin-we-get/different-different-book/jesus/) as discussed in the `The APP and Data Collection for the project` paragraph.

##### Step 1 : Data Arrangement
Elicitation by text were made in the Ibibio language. 
 
The `project/sections` folder, contains the different sections of the recordings of each files in `project/text_files`. In the `project/text_files` each text file e.g `section1.txt` corresponds to the audio wave file conatained in `section_1` which is in the folder`project/sections`. 

Each of the `section1.txt` contains 10-15 words per sentence, and then I have 50-57 sentences making up a `section.txt` file. in all I have 20 sections of txt file with it's corresponding 20 sections of audio wav recordings. 
 
##### Step 2 : Data Preprocessing
 
After the recordings had been done, the next thing was to preprocess the data in the right format for CPC/CTC experiments. The lig-aikuma  App gives a wav file aligned to transcripts (the info about the link between txt and wav can be found in the ***_elicit_link.txt files). All preprocessing can be accessed through the notebook `Nigerian_Pidgin_preprocessing.ipynb` , 
 
Note that a python installation is required as well as some dependencies;

- numpy
- wave
- contextlib


##### Step 3 : Data Spliting

Still in the `Nigerian_Pidgin_preprocessing.ipynb`.
- The number of speech recorded was calculated as `2.20795 hours`.
- Corrupted files were discarded.
- Organizing the data by matching the recoding to its corresponding label text file using the linkers in each of the sections, this is found in the `project/data/raw_text_file.txt` file.
- Then the date was split into train, val and text set, this are found in `project/data/records`folder
- We also have the `chars.txt` file which contains the recordings and the corresponding indexis of each characters in the text file. 
- finally, the `charset.txt` files each of the characters and their frequency.

### Application

The dataset can be useful especially for low-resource speech modelling. NLP in Africa is still in its infancy; of about 2000 languages, a very few have  featured  in  NLP  research  and  resources, This project will add to the language  resources  for  Nigeria  as  part  of  a  corpus-based  project, This project can be useful if fine-tune on high-resource data like LibriSpeech for a Speech-to-text project. The `Blessing_Bassey_CTC_notebook` can be a start up point, as this was used for the project. 

### Chalenges
- The lig-aikuma app has so many versions, all were tried on my andriod mobile phone but unfortunately none worked for me (maybe they were not compatible with my phone), hence, I was left with the option of using an android studio version on my computer system.
- During the recording section, surrounding noice were very difficult to elliminate totally.

### Contributing and Licensing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[MIT](https://choosealicense.com/licenses/mit/) License
