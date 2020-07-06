# Lik-Aikuma_Data_Collection
This repo contains speech data collection using Lik-Aikuma. The data was collected by speaking 2000 + words in Nigerian Pidgin recorded lightly above 2 hours.

## Downloading

To clone this repo, go to your terminal and type;

```git
git clone https://github.com/KANUBALAD/Lik-Aikuma_dataCollection.git
```

This adds a folder "Lik-Aikuma_dataCollection" to your local directory.

## Data Collection
Major part of this project, the data was collected from [Jehovah Witness People](https://www.jw.org/pcm/wetin-we-get/different-different-book). Some other sections of the recording were taken from [BBC](https://www.bbc.com/pidgin). The audio recordings were done using [LIG-Aikuma](https://lig-aikuma.imag.fr/tutorial/). It works by allowing the app to use your phone microphone to record speech. Before you download the app, please ensure that you check you andriod version of your phone first. You can do this by going to Settings on your mobile phone then to Andriod version. 
LIK-Aikuma is user friendly and provides an excellent user interface for recording speech or elicitation of either images, videos or text. Generally, the app provides 6 modes of usage:

- Recording
- Respeaking
- Translating
- Elicitation
- Check
- Share

For this work, we used elicitation by text. Text files were generted and put in sub sections and uploaded to LIG-Aikuma.

## Statistics

- A total of 1149 files were recorded with 88 corrupted files.
- A total of8069.399249999986  seconds ,  2.2414997916666626  hours.
- 18 folders containing different recording sections. 


## Tutorial:

The folder tutorial contians a narrated stroy using the frogstory whose folder has been added to this as well. This was just a simple and short tutorial on how to use the Likaikum app to collect data. The tutorial folder therefore contains all the recordings for this.

## Recordings_Pidgin:
This folder also contains  three additional folders. They include:

### 1. Data: 

In this sub folder we have:

- chars.txt
- charset.txt
- linker.txt
- raw_text_file.txt
- records( this contains folders of train, test and validation dataset)


### 2. Sections:

This contains subfolders of all audio recordings with their linker.txt files in them.

### 3. Text_files:

This contains all the .txt files used in recording.


### 4. Preprocessing:
This is the jupyter notebook with all the preprocessing used for the data. It contains the code on how the data is splitted into train, test and validation sets.


## 5. Application:

Usually, it is hard getting data for low-resource languages. This challenge therefore makes it hard to build useful models for  these languages depsite the huge number of users of these languages. This dataset will therefore serve as a start and hopefully additional data will be collected. If a large size of the data is collected, one can build a well developed speech to text model.


## 6. Challenges

- Some audio files were corrupted and I am still unsure how/ why these files were corrupted.
- I hard some difficulties pronucing some of the words.
- Some of the audio had some noice from the environment.
-

## 7. Suggestions:

The app should include a delete icon when recording so one can easily delete a current a wrongly recorded file.

##  8. Contributing
You are welcome to contribute to this project by recording audio files in pidgin and sending me a merge request.


## 9. License

[MIT](https://choosealicense.com/licenses/mit/)


