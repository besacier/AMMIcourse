# Arabic-Speech-Recognition-Dataset
This data was collected as part of the Speech Recognition course at AIMS Ghana, taught by Emmanuel Dupoux, Laurent Besacier, Gabriel Synnaeve and Neil Zeghidour.

The dataset consists of the following sections:
* data/records : path to the recordings, it further devides to:
  * data/records/train : training set wav files, it consists of ~48 minutes of audio
  * data/records/val : validation set, ~12 minutes of audio
  * data/records/test: test set, ~60 minutes of audio
* data/chars.txt : represents a mapping between all audio files and the corresponding label (sequence of characters). it's format is as follows

    ```file1_name c1 c2 c3 c4 ...```

    ```file2_name c1 c2 c3 c4 ...```
    
* data/charset.json : a dictionary specifying the mapping between the characters and the numbers in ```chars.txt```
* data/lm.arpa : an ngram language model trained using KenLM, consists of at most 4 gram sequences.

The dataset was recorded using LIG-Aikuma app and further processed for training purposes.
