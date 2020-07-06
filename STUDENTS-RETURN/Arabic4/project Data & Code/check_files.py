from glob import glob
import os
path = "/home/zeinab/Documents/AMMI_Courses/14) Speech Recognition- Gabreil/Final Project & Data collection/txt files+Recor/data"

for portion in ['Train', 'Test']:
    folders = os.listdir(os.path.join(path,portion))
    for folder in folders:
        # np_audios = len(glob(os.path.join(path, portion, folder)+'/*.wav'))
        # print(os.path.join(path, portion, folder))
        # print(glob(os.path.join(path, portion, folder)+'/*linker.txt')[0]
        sessions = open(glob(os.path.join(path, portion, folder)+'/file*.txt')[0], 'r')
        np_lines_ss = len([line for line in sessions.readlines()])
        
        linker = open(glob(os.path.join(path, portion, folder)+'/*linker.txt')[0], 'r')
        np_lines_lr = len([line for line in linker.readlines()])
        if np_lines_ss != np_lines_lr:
            print(os.path.join(path, portion, folder), 'np_lines_ss:', np_lines_ss, 'np_lines_lr:', np_lines_lr)

print('everything okey')