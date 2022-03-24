# FFT

fft, window function, Amplitude correction



## 1.原理

参考知乎专栏文章或视频：https://www.zhihu.com/column/c_1481725623442128898



## 2.验证

### a. 16个样本点的信号，与知乎文章对应

![image-20220324160842877](https://gitee.com/jubar/images/raw/master/typora/image-20220324160842877.png)

### b. 模拟真实信号1024个样本点，采样率102.4，加Hanning窗，幅值修正

![image-20220324161146101](https://gitee.com/jubar/images/raw/master/typora/image-20220324161146101.png)

## 3. 相关技术

### a.位反转

如果以二进制形式重写样本索引，然后反转位的顺序，我们得到样本的顺序，正式FFT中分组排序，具体如下：

![image-20220324161253534](https://gitee.com/jubar/images/raw/master/typora/image-20220324161253534.png)

### b.加窗后幅值修正

![image-20220324161403300](https://gitee.com/jubar/images/raw/master/typora/image-20220324161403300.png)

## 4.引用

[1]焦新涛,丁康.加窗频谱分析的恢复系数及其求法[J].汕头大学学报(自然科学版),2003(03):26-30+38.