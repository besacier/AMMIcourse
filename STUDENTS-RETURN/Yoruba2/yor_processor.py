import math

import os
from random import randint, uniform
import re
import numpy as np
import wave
import contextlib
import re

# MAX_SENTENCE_LEN = 20
# SOURCE_PATH = 'yor_trans.txt'
# DEST_TEMP_PATH = 'yor_split.txt'
# DEST_TEMP_CLEAN_PATH = 'yor_clean_split.txt'
# NUM_FOLDER_SPLIT = 50
# FOLDER_PATH="split_text"
# PARTIAL_NAME= "yor_split"


def split_file(source_path, dest_path, max_sentence_len, end_of_file="## .\n"):
    f = open(source_path, 'r')
    new_f = open(dest_path, 'w')
    for line in f:
        line = line.lower().replace('\n', '')
        splitted_text = line.split(" ")
        total_words = len(splitted_text)
        if total_words > 1:
            if total_words <= max_sentence_len:
                line = line + " " + end_of_file
                new_f.write(line)
            else:
                # sentence longer than "max_sentence_len"
                num_split = math.ceil(total_words/max_sentence_len)
                for i in range(num_split):
                    cut_sentence = splitted_text[i*max_sentence_len: (i+1)*max_sentence_len]
                    cut_sentence.append(end_of_file)
                    cut_sentence = " ".join(cut_sentence)
                    new_f.write(cut_sentence)
    
    f.close()
    new_f.close()
    return "done"

def split_file_into_folders(folder_path, source_path, partial_file_name, num_folder_split):
    f = open(source_path, 'r')
    count = 0
    text = ""
    for idx, line in enumerate(f):
        text = text+line
        if idx % (num_folder_split-1) == 0 and idx!=0:
            file_name = folder_path+"/"+partial_file_name+"_"+str(count)+".txt"
            with open(file_name, 'w') as new_split_f:
                new_split_f.write(text)
            text = ""
            count += 1

def calculate_recording_len(path="./recordings/", file_format=".wav"):
    total = 0
    corrupted=0
    files=0
    for directory in os.listdir(path):
        if os.path.isdir(path+directory):
            for file in os.listdir(path+directory):
                if file.endswith(file_format):
                    files+=1
                    fname = path+directory+"/"+file
                    try:
                        with contextlib.closing(wave.open(fname,'r')) as f:
                            frames = f.getnframes()
                            rate = f.getframerate()
                            duration = frames / float(rate)
                            total+=duration
                    except Exception as e:
                        corrupted+=1

    return total, files, corrupted

def extract_non_corrupted_files(path="./recordings/"):
    # Extracting all the non-corrupted files
    wav_files = []
    all_linkers = dict()
    for directory in os.listdir("./recordings/"): # parent directory of the recordings, it should contain folders that contain wav,json and txt files
        if os.path.isdir("./recordings/"+directory):
            linker = []
            to_remove = []
            linker_file = [file for file in os.listdir("./recordings/"+directory) if file.endswith(".txt")][0]
            linker_data = open("./recordings/"+directory+"/"+linker_file).readlines()
            for file in os.listdir("./recordings/"+directory):                
                if file.endswith(".wav"):
                    fname = "./recordings/"+directory+"/"+file
                    try:
                        with contextlib.closing(wave.open(fname,'r')) as f:
                            frames = f.getnframes()
                            rate = f.getframerate()
                            duration = frames / float(rate)
                            wav_files.append(fname)
                    except Exception as e:
                        to_remove.append(file)
            for file in to_remove:
                i=0
                while i<len(linker_data):
                    if file in linker_data[i]:
                        linker_data.pop(i)
                    i+=1
            
            linker.extend(linker_data)
            all_linkers[directory] = linker

    return wav_files, all_linkers

def split_train_val_test(wav_files, num_splits, val_split):
    np.random.seed(0)
    all_indices = np.random.permutation(len(wav_files))

    # calculate length of splits
    if num_splits > 2:
        index_start = len(all_indices)//num_splits
    else:
        index_start = 0
        
    indices = all_indices[index_start:]

    if num_splits > 2:
        extra_idx = all_indices[:index_start]
    test_idx = indices[:len(indices)//2]
    validation_portion = int(len(indices)//2 * val_split)
    train_idx = indices[len(indices)//2:-validation_portion]
    valid_idx = indices[-validation_portion:]

    # prepare paths for copy
    extra_files = []
    if num_splits > 2:
        extra_files = [wav_files[i].split("/")[-1] for i in extra_idx]
    train_set_files = [wav_files[i].split("/")[-1] for i in train_idx]
    valid_set_files = [wav_files[i].split("/")[-1] for i in valid_idx]
    test_set_files = [wav_files[i].split("/")[-1] for i in test_idx]

    # copy to folders
    if len(extra_files) >= 1:
        to_copy_extra = "./data/records/" + " ./data/records/".join(extra_files)
    else:
        to_copy_extra = []
    to_copy_train = "./data/records/" + " ./data/records/".join(train_set_files)
    to_copy_valid = "./data/records/" + " ./data/records/".join(valid_set_files)
    to_copy_test = "./data/records/" + " ./data/records/".join(test_set_files)

    return to_copy_train, to_copy_valid, to_copy_test, to_copy_extra


def create_char_set(linkers, path="./split_text/", exclude="",):

    chars = {" ":1, "ε":0}
    text_data = []
    char_idx = 2
    for section_id, linker in linkers.items():
        text_file = open(path+section_id,"r").readlines() # Modify this to the directory of your txt file that you recorded with
        
        for link in linker:
            #print(link)
            file, idx = link.split(":")[0],int(link.split(":")[1].split(" ")[1])-1
            line = text_file[idx]
            line = line.split("##")[0].strip()
            
            line = re.sub(exclude, "", line) # Clean unnecessary characters from the data, this is for arabic
            text_data.append((line,file.split(".")[0]))
            char_set = set(line)
            for c in char_set:
                if c not in chars:
                    chars[c]=char_idx
                    char_idx+=1
    return chars, text_data

def create_data_format(text_data, chars_dict):
    raw_text = "\n".join([wav+":"+line for line, wav in text_data])
    with open("data/raw_text_file.txt","w") as f:
        f.write(raw_text)

    indices_text = []
    for line, wav in text_data:
        line = list(line)
        indices = []
        for c in line:
            indices.append(str(chars_dict[c]))
        indices_text.append(wav+" "+" ".join(indices))
    
    indices_text = "\n".join(indices_text)
    with open("data/chars.txt","w") as f:
        f.write(indices_text)

    with open("data/charset.txt", "w") as js:
        js.write(str(chars_dict))
    
    with open("data/charset.txt") as js:
        charset = eval(js.read())
    
    print("files created for training")

