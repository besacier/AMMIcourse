#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import the necessary files
from glob import glob
import os
import wave
import nltk


# In[9]:


# define all twi charaters
twi_chars = "A B C D E Ɛ F G H I K L M N O Ɔ P R S T U W Y" 

# separate twi characters
character_to_index = {j:i for i,j in enumerate(twi_chars.split())} 

# remove all punctuarions
def remove_punct(text): 
  tokenizer = nltk.RegexpTokenizer(r"\w+") 
  new_words = tokenizer.tokenize(text) 
  t = '' 
  for i in new_words: 
    t+= i+' ' 
  return t 

# define path for sessions and linkers
sessions = glob("/home/brefo/Downloads/CourseWork/Sp/Project/ALL_DATA/*/*/*ssion.txt")
linkers = glob("/home/brefo/Downloads/CourseWork/Sp/Project/ALL_DATA/*/*/*linker.txt")

# find the number of both .txt files, they must be the same
print(len(sessions))
print(len(linkers))

#create a txt file to write
all_session_text = open('all_sessions.txt', 'w')

# loop all files and convert them split char to corresponding numeric values
for linker, sess in zip(linkers, sessions):
   sess_read = open(sess, 'r')
   link_read = open(linker, 'r')
   for link, sentence in zip(link_read.readlines(), sess_read.readlines()):
       wav_name = os.path.basename(link).replace('\n','')
       wav_path = glob(os.path.abspath(os.getcwd()) + "/*/*/{0}".format(wav_name)) 
       
       if len(wav_path)==0: 
           continue 
       wav_path = wav_path[0] 
       #print(wav_path)
       try: 
           w = wave.open(wav_path, 'r') 
           d = w.readframes(w.getnframes()) 
       except: 
           print('corrupted audio: {0} -- skipped: '.format(wav_name)) 
           continue 
       indices = '' 
       sentence = sentence.replace('##', '') 
       sentence = remove_punct(sentence) 
       for c in sentence: 
           if not c.isspace(): 
               indices+=str(character_to_index[c.upper()]) + ' ' 
       
       all_session_text.writelines(wav_name[:-4] + ' ' + indices + '\n')


# In[ ]:




