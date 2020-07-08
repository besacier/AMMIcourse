import wave
import os
from pathlib import Path
import shutil

def main():
    path = Path('/home/thompson/Documents/Speech-Recognition-for-the-Ga-Adangbe-Language/Prepared DATA')
    audio_files = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.wav'):
                audio_files.append(os.path.join(dirname, filename))
    total_len = 0
    print('total number of files:{}'.format(len(audio_files)))

    read_files = 0

    output_path = 'not-working'
    if not os.path.exists(output_path):
        os.mkdir(output_path)


    for i in range(len(audio_files)):
        path = audio_files[i]
        try:
            with wave.open(audio_files[i]) as audio_file:
                frames = audio_file.getnframes()
                rate = audio_file.getframerate()

                total_len+=frames/float(rate)
            read_files+=1
        except:
            print('Unable to read "{}"'.format(path))
            _, filename = os.path.split(audio_files[i])
            shutil.move(audio_files[i], os.path.join(output_path, filename))
            pass
    print('Total length: {} hours'.format(total_len/3600.0))
    print('read {} files out of {} files'.format(read_files, len(audio_files)))
    print(f"The number of corrupted files: {len(os.listdir(output_path))}")
    

if __name__ == "__main__":
    main()