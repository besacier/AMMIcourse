# Speech_recognition_AMMI
Speech  Recognition for Low Resource Language(Twi)

- This was an in-class project on speech recognition for low-resource language such as Twi my local dialect. The repos is made up of the following:
    - Data collected using an app called ligaikuma. 
    - Writtten text of the holy scriptures in our local dialect. 
    - Texts with their corresponding recordings 
    - Two hours of data audio recordings. The [calculate](load_wav.py) the total recordings. 

- The next phase of the project is to model the data using CPC model. 
    - We built Automatic Speech Recognition (ASR) system by using a pretrained model with Connectionist Temporal Classification on top of it. 
    - We had a Character Error Rate of 0.98 and 0.908 for both training and validation set respectively [notebook](Speech_recognition_Twi.ipynb). 


## License:

- Under the license of [MIT](License.txt) 
