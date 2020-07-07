# Lig-Aikuma-Data-Collection
This repository contains speech/text data collected using the Lig-Aikuma mobile App as well as some python notebooks 
used throughout this project.
# Data Collection
In this project, the data was collected from the book Voyage au Japon by Dhammadána. The recordings were done using the Lig-Aikuma mobile App installed on my Huawei Honor 8X. It works by allowing the app to use your phone microphone to record speech. Before you download the app, please ensure that you check the android version of your phone first. Lig-Aikuma is user friendly and provides an excellent user interface for recording speech or elicitation of either images, videos or text.

This folder also contains three additional folders. They include:
1. data:

In this sub folder we have:
    chars.txt
    charset.txt
    linker.txt
    raw_text_file.txt
    records(this contains folders of train, test and validation datasets)
2. recordings:

This sub folder contains the elicitation (by image) data of a Frog Story.

3. sessions:

In this one, we can find the raw text (txt files of sentences from the book)

4. Data-preprocessor.ipynb

This is the jupyter notebook with all the preprocessing used for the data.

5. CTC_Jean_N_Kouagou.ipynb

This is the notebook with the CTC/CPC models which were fine-tunned using the above data


# Acknowledgement

This would not have been able without the support of the African Master in Machine Intelligence through the full bursary, including a great study environment and a brand new laptop.

I am also grateful to Laurent Besacier, Gabriel Synnaeve and three of their other colleagues for the course material and the mobile App Lig-Aikuma, without which this project would not have been completed in such a short time.


