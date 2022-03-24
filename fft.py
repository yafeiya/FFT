import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.fftpack import fft
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号


# 样本点数是否2的幂
def check_samples(sample_array):
    n = len(sample_array)
    if np.log2(n) % 1:
        return 0
    else:
        return int(np.log2(n))


# 样本点索引按位反转
def Decimal_to_bin(Decimal,times):
    _, bins = bin(Decimal).split('b')
    temp = bins.zfill(times)
    return int(temp[::-1], 2)


# 样本点重排序
def reorder_samples(sample_array):
    reorder_samples_array = []
    if check_samples(sample_array) == 0:
        print('ERROR:The number of samples in the signal is not a power of 2')
    else:
        # 样本点切分次数 == 索引位数
        times = check_samples(sample_array)
        for index, decimal in enumerate(sample_array):
            tmp = Decimal_to_bin(index, times)
            reorder_samples_array.append(sample_array[tmp])
    return reorder_samples_array

# 蝴蝶操作
def bufferfly(complex0,complex1):
    res = []
    res.append(complex0+complex1)
    res.append(complex0-complex1)
    return res


# 相位因子
def twiddle_factor(index, order):
    real = np.cos(2*np.pi*index/order)
    imaginary = -np.sin(2*np.pi*index/order)
    return complex(real, imaginary)


# 样本值转为复数
def create_complex(sample_value):
    return complex(sample_value, 0)


# 组合计算所有样本点
def cal_butterfly_array(sample_array):
    # 样本点切分次数
    times = check_samples(sample_array)
    complex_sample = []
    results = []
    for a in sample_array:
        complex_sample.append(create_complex(a))
    butterfly_array = reorder_samples(complex_sample)

    for time in range(times):
        order = 2**(time+1)  # 2点、4点、8点、16点蝶形
        group_num = len(sample_array)//order
        for group in range(group_num):  # 0-7; 0-3; 0-1; 0
            for sample_index in range(order//2):  #旋转因子个数1,2,4,8
                # 第二轮 order 4  group_num 4
                pair_index1 = group * order + sample_index # 0;1
                pair_index2 = pair_index1 + order//2   # 2;3

                W = twiddle_factor(sample_index,order)

                tmp = bufferfly(butterfly_array[pair_index1], W*butterfly_array[pair_index2])
                butterfly_array[pair_index1] = tmp[0]
                butterfly_array[pair_index2] = tmp[1]
        # print(butterfly_array)
        results.append(butterfly_array)
    return results


# 信号加窗
def choose_windows(name='Hamming', N=1024):
    if name == 'Hamming':
        window = np.array([0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
    elif name == 'Hanning':
        window = np.array([0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
    else:
        window = np.ones(N)
        print('no windows you inputed')
    return window

def correction_cmplitude_factor(name ='Hamming'):
    if name == 'Hamming':
        factor = 1.852
    elif name == 'Hanning':
        factor = 2
    else:
        print('no windows you inputed')
        factor = 1
    return factor

if __name__ == '__main__':

    # # 一、16个点实验信号
    # sample_array = [random.randint(1, 100) for _ in range(16)]
    # # sample_array = [91, 78, 6, 46, 31, 84, 9, 13, 22, 5, 1, 30, 61, 19, 60, 70]
    # print('原始离散信号\n', sample_array)
    # res = cal_butterfly_array(sample_array)
    # print('FFT计算结果\n', res[3])
    # y_fft = fft(sample_array)
    # print('FFT调库结果\n', y_fft)

    # 二、模拟真实信号、加窗、幅值修正
    window = choose_windows(name='Hanning')
    factor = correction_cmplitude_factor(name='Hanning')
    N = 1024
    freq_1 = 3
    t = np.arange(-5, 5, 10 / N)  # 离散时间10s,1024点数, 采样率为102.4HZ
    k = np.arange(0, N, 1)
    x = (2 * np.sin(2*np.pi * freq_1 * t) + np.random.normal(0, 0.05, 1024)) * window

    # 执行FFT
    fft_res = (cal_butterfly_array(x))[3]
    f_array = []
    for i in fft_res:
        # 幅值归一化，再乘恢复系数
        f_array.append(abs(i)/(N//2)*factor)

    # sample
    k0 = f_array.index(max(f_array))
    print("峰值索引k:{}, 对应频率f:{:.2f}".format
          (k0, k0*102.4/1024))
    print("峰值振幅A:{:.2f}".format(max(f_array)))


    # 绘图
    plt.subplot(211)
    plt.plot(t, x)
    plt.title('Signal')
    plt.xlabel('Time / s')
    plt.ylabel('Intencity / cd')

    plt.subplot(212)
    plt.plot(k, f_array)
    plt.title('Spectrogram')
    plt.xlabel('index ')
    plt.ylabel('Amplitude ')

    plt.show()