# 导入tensorflow，顺序模型，以及神经网络层
# 导入序列化模块
import pickle

from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential

# 反序列化
X = pickle.load(open('X.pickle', 'rb'))
y = pickle.load(open('y.pickle', 'rb'))
# 归一化，像素值范围为0~255
X = X / 255.0
# 模型初始化
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))  # 添加卷积层
model.add(Activation('relu'))  # 添加激活函数
model.add(MaxPooling2D(pool_size=(2, 2)))  # 池化
# 以下同理
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# 模型配置 ：损失函数，优化方法，评价指标
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# 训练模型
model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1)
