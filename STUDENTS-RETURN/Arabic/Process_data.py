
import os 
import nltk 
import wave 
from glob import glob 

arabic = "غ ظ ض ذ خ ث ت ش ر ق ص ف ع س ن م ل ك ي ط ح ز و ة ه د ج ب ا ى إ ء ئ آ ؤ أ 0 1 2 3 4 5 6 7 8 9 ـ ھ"
character_to_index = {j:i for i,j in enumerate(arabic.split())} 

def remove_punct(text):
    tokenizer = nltk.RegexpTokenizer(r"\w+") 
    new_words = tokenizer.tokenize(text) 
    t = '' 
    for i in new_words: 
        t+= i+' ' 
    return t 
path = '/home/zeinab/Documents/AMMI_Courses/14) Speech Recognition- Gabreil/Final Project & Data collection/txt files+Recor/data'

sessions = glob(f"{path}/*/*/file*.txt")
linkers = glob(f"{path}/*/*/*linker.txt")

# print('Session files:',len(sessions), 'Linker files:',len(linkers))

all_session_text = open(f'{path}/all_sessions.txt', 'w') 

for linker, sess in zip(linkers, sessions):
    sess_read = open(sess, 'r')
    link_read = open(linker, 'r')
    for link, sentence in zip(link_read.readlines(), sess_read.readlines()):
        wav_name = os.path.basename(link).replace('\n','')
        wav_path = glob(os.path.abspath(os.getcwd()) + "/data/*/*/{0}".format(wav_name)) 
        if len(wav_path)==0: 
            continue 
        wav_path = wav_path[0] 
        try: 
            w = wave.open(wav_path, 'r') 
            d = w.readframes(w.getnframes()) 
        except: 
            print('corrupted audio: {0} -- skipped: '.format(wav_name)) 
            # uncomment if you want to delete the corrupted file 
            # os.remove(wav_path) 
            continue 
        indices = '' 
        sentence = sentence.replace('##', '') 
        sentence = remove_punct(sentence) 
        for c in sentence: 
            if not c.isspace(): 
                indices+=str(character_to_index[c.lower()]) + ' ' 
        
        all_session_text.writelines(wav_name[:-4] + ' ' + indices + '\n')