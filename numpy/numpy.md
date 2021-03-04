## numpy库

#### 1.创建数组的方法

- np.zeros(shape)        创建形状为入参的全为0的数组
- np.ones(shape)         创建形状为入参的值全为1的数组
- np.full(shape,data)    创建形状为shape，值全为data的数组
- np.array(list)              list为序列，
- np.arange()              创建有规律的一维数组
- np.eye(data)            创建形状为（x,x）的对角线值为1其他全为0的数组
- np.random.random(shape)    创建形状为shape的值为随机的数组

<br/>

#### 2.numpy.where函数的妙用

- 可以使用where(条件)获取数组中满足条件的值
- 可以使用where(条件，替代值，数组)来在不改变原数组的情况下，将数组中满足条件的值替换成替代值并返回新数组