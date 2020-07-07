import os 
import nltk 
import wave 
from glob import glob 
bemba_chars = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ŋ É Ó Ë Ñ Ñ À Ï Ù È Ê Û Ç Ô"  
character_to_index = {j:i for i,j in enumerate(bemba_chars.split())} 

def remove_punct(text): 
  tokenizer = nltk.RegexpTokenizer(r"\w+") 
  new_words = tokenizer.tokenize(text) 
  t = '' 
  for i in new_words: 
    t+= i+' ' 
  return t 

sessions = glob("/home/gueye/Documents/dataset/data/*/*/*ssion.txt")
linkers = glob("/home/gueye/Documents/dataset/data/*/*/*linker.txt")

all_session_text = open('all_sessions.txt', 'w') 

for linker, sess in zip(linkers, sessions):
    sess_read = open(sess, 'r')
    link_read = open(linker, 'r')
    for link, sentence in zip(link_read.readlines(), sess_read.readlines()):
        wav_name = os.path.basename(link).replace('\n','')
        wav_path = glob(os.path.abspath(os.getcwd()) + "/*/*/*/{0}".format(wav_name)) 
        # print(os.path.abspath(os.getcwd()))
        # print(wav_path)
        if len(wav_path)==0: 
            continue 
        wav_path = wav_path[0] 
        try: 
            w = wave.open(wav_path, 'r') 
            d = w.readframes(w.getnframes()) 
        except: 
            print('corrupted audio: {0} -- skipped: '.format(wav_name)) 
            # uncomment if you want to delete the corrupted file 
            os.remove(wav_path) 
            continue 
        indices = '' 
        sentence = sentence.replace('##', '') 
        sentence = remove_punct(sentence) 
        for c in sentence: 
            if not c.isspace(): 
                indices+=str(character_to_index[c.upper()]) + ' ' 
        
        all_session_text.writelines(wav_name[:-4] + ' ' + indices + '\n')
