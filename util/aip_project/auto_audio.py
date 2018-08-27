# -*- coding: utf-8 -*-
import pyaudio
import wave
import numpy as np
# import time
'''
    当前三秒没有声音的时候自动结束监听。
    若三秒后仍未结束语音，则每1.6s检测一次
    直至完全没有声音输入为止停止监听
'''

def Monitor():
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    # 采样频率
    RATE = 16000
    RECORD_SECONDS = 5
    # 文件保存路径
    WAVE_OUTPUT_FILENAME = "cache.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("开始缓存录音")
    frames = []
    # start = time.time()
    print('begin ')
    for i in range(0, 100): # 100为3.2秒左右  50为1.6秒左右
            data = stream.read(CHUNK)
            frames.append(data)
    # print(time.time() - start)
    audio_data = np.fromstring(data, dtype=np.short)
    large_sample_count = np.sum(audio_data > 800)
    temp = np.max(audio_data)
    if temp < 800 :
        print('当前阈值：',temp)
        print("检测到信号,结束录音")
    else:
        while True:
            print('检测到声音，继续录音')
            for i in range(0, 50):
                data = stream.read(CHUNK)
                frames.append(data)
            audio_data = np.fromstring(data, dtype=np.short)
            large_sample_count = np.sum(audio_data > 800)
            temp = np.max(audio_data)
            # print('当前阈值：',temp)
            if temp < 800 :
                print('当前阈值：',temp)
                print("检测到信号")
                break
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return WAVE_OUTPUT_FILENAME

if __name__ == '__main__':
    Monitor()
