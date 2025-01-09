import numpy as np
import sounddevice as sd

# 音符的频率（以赫兹为单位）
notes = {
    "Do": 261.63,  # C4
    "Re": 293.66,  # D4
    "Mi": 329.63   # E4
}

# 生成一个指定频率的音频
def generate_sound(frequency, duration=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # 生成时间数组
    waveform = np.sin(2 * np.pi * frequency * t)  # 生成正弦波
    return waveform

# 播放音符
def play_notes():
    for note in ["Do", "Re", "Mi"]:
        sound = generate_sound(notes[note])  # 获取音符对应的波形
        sd.play(sound, 44100)  # 播放音频
        sd.wait()  # 等待播放完成

# 播放音符序列
play_notes()
