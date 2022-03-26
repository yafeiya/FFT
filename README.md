# FFT

fft, window function, Amplitude correction



## 1.原理

参考知乎专栏文章或视频：https://www.zhihu.com/column/c_1481725623442128898



## 2.验证

### a. 16个样本点的信号，与知乎文章对应
![image](https://user-images.githubusercontent.com/102225985/160226236-d5a2d884-1e6e-4185-904d-6d1ad2d68a3b.png)

### b. 模拟真实信号1024个样本点，采样率102.4，加Hanning窗，幅值修正

![image](https://user-images.githubusercontent.com/102225985/160226252-84e70691-f142-44ed-b5e8-b4b9b3fb9660.png)

## 3. 相关技术

### a.位反转

如果以二进制形式重写样本索引，然后反转位的顺序，我们得到样本的顺序，正式FFT中分组排序，具体如下：

![image](https://user-images.githubusercontent.com/102225985/160226269-f147b9a2-8771-4281-8012-f5b37d52e732.png)


### b.振幅恢复系数

![image](https://user-images.githubusercontent.com/102225985/160226303-1ca7616b-d824-4e51-8307-68dbea5c95fb.png)

## 4.引用

[1]焦新涛,丁康.加窗频谱分析的恢复系数及其求法[J].汕头大学学报(自然科学版),2003(03):26-30+38.
