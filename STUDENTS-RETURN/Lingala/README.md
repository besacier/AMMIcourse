# MaseseSpeech

1. General information

======================

MaseseSpeech is a corpus of read speech in Lingala, based on 11 books of proverbs in the Bible. Its purpose is to enable the training and testing of automatic
speech recognition(ASR) systems for Lingala. 

Lingala (Ngala) is a Bantu language spoken throughout the northwestern part of the Democratic Republic of the Congo and a large part of the Republic of the Congo. It is spoken to a lesser degree in Angola and the Central African Republic. There are over 70 million lingalophones.

You can use this [notebook](https://github.com/Kabongosalomon/MaseseSpeech/blob/master/Main_MaseseSpeech_ASR.ipynb) for a quick look of a working ASR example using PyTorch.
 
2. Structure

============

The corpus is split into two parts : train-lean and dev-lean. The subsets are
disjoint.

The parts of the corpus are as follows:

    * train-clean - training set, of approximately 1 hours of "clean" speech
    * dev-clean - development set of approximately 1 hours of "clean" speech


2.1 Organization of the training and test subsets
-------------------------------------------------

When extracted, each of the {dev,train} sets re-creates MaseseSpeech's root
directory, containing some metadata, and a dedicated subdirectory for the subset
itself. The audio for each individual verse is stored under a dedicated 
subdirectory in the subset's directory, and each audio verse is stored in separate subsubdirectory. The following ASCII diagram 
depicts the directory structure:


    <corpus root>
        |
        .- README.TXT
        |
        .- train-clean/
                |
                .- 020/
                    |
                    .- 001/
                    |    |
                    |    .- 020-001.trans.txt
                    |    |    
                    |    .- 020-001-0001.wav
                    |    |
                    |    .- 020-001-0002.wav
                    |    |
                    |    ...
                    |
                    .- 002/
                        | ...


where 020 is the ID of the book (which is always proverbs in this dataset), and 001 and 002 are the IDs of the chapters
read by this speaker. The *.trans.txt files contain the transcripts for each
of the utterances, derived from the respective chapter and the wav files contain
the audio itself.

3. Data Download

================

- [train-clean](https://drive.google.com/file/d/1CfqHBiOEVnJiuwZoqBJMlGO-N97JD3sR/view?usp=sharing)
- [dev-clean](https://drive.google.com/file/d/1Y1CiB7TbrGdghVokwMTBQA1fRza2NZUP/view?usp=sharing)


Acknowledgments

===============

First and foremost, I would like to thank the [African Master in Machine Intelligence](https://aimsammi.org/) 
for givin me the environnement to run this project and create this dataset.

The successful completion of this project would have been much more difficult, if it wasn't for the
generous support, provided by Professor Laurent Besacier, Univ. Grenoble Alpes.

Thanks also to the [Lig-Aikuma](https://lig-aikuma.imag.fr/lig-aikuma-in-90mn/) project for providing the platform to record and create this dataset. 

---
Salomon KABONGO,
Jul. 6, 2020 
