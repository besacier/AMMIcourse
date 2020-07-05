import wave 
import numpy as np 
import os 
import shutil 
import glob 


path = "/home/emmanuel/Speech_project/voice_recording/"


def estimate_recording(path):
    """
    Args: 
        Take the path to the folders 

    Return:
        Number of voice recording and total voice recording made. 
    """

    waves = []

    for path , _ , files  in os.walk(path):
        for record in files: 
            if record.endswith("wav"):
                waves.append(os.path.join(path,record))


    total_duration = 0

    for recording in waves:
            try:
                with wave.open(recording,"r") as file:
                    frames = file.getnframes()
                    rates  = file.getframerate()
                    total_duration += (1.0 * frames) / rates 
            except:
                print("Faulty file in the directory: ")
                print("The faulty file: ", recording)


    return waves , total_duration / 3600.0


if __name__ == "__main__":
    ### execute the code 
    waves , duration = estimate_recording(path)
    print(f"Number of wave {len(waves)}")
    print(f"Total time duration : {round(duration,2)} hours")




