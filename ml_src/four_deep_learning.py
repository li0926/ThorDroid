import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras import layers
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
from reader import read_constant
from my_generator import my_generator, get_apks_and_types, KFCV_index
from tools import folders_set
import random


def deep_learning(TYPE, TYPE_list, type_map, word2vec_model,globals):
    # 训练集,测试集
    x_train, y_train, train_apk_count = get_apks_and_types(globals['L'],globals['K'],globals['train_path'], TYPE, TYPE_list, type_map, word2vec_model)
    x_test, y_test, test_apk_count = get_apks_and_types(globals['L'],globals['K'],globals['test_path'], TYPE, TYPE_list, type_map, word2vec_model)
    all_apk_count = train_apk_count + test_apk_count
    seed = random.random()

    random.seed(seed)
    all_x = np.vstack((x_train, x_test))
    random.shuffle(all_x)

    random.seed(seed)
    all_y = np.vstack((y_train, y_test))
    random.shuffle(all_y)

    if globals['KFCV']:
        test_count = int(all_apk_count * globals['test_split'])
        x_train, y_train = all_x[test_count:], all_y[test_count:]

        train_count = all_apk_count - test_count
        x_test, y_test = all_x[:test_count], all_y[:test_count]

    else:
        val_count = int(all_apk_count * globals['val_split'])
        x_val, y_val = all_x[:val_count], all_y[:val_count]

        test_count = int(all_apk_count * globals['test_split'])
        x_test, y_test = all_x[all_apk_count - test_count:all_apk_count], all_y[
                                                                          all_apk_count - test_count:all_apk_count]

        train_count = all_apk_count - val_count - test_count
        x_train, y_train = all_x[val_count: all_apk_count - test_count], all_y[val_count: all_apk_count - test_count]

    # 神经网络
    model = Sequential()
    # 卷积
    model.add(layers.Conv2D(filters=globals['filter_count'], kernel_size=globals['kernel_size'], activation='relu', input_shape=(globals['L'], globals['K'], 1)))
    model.summary()
    # 池化
    model.add(layers.MaxPooling2D(globals['maxpooling_size']))
    model.add(layers.Flatten())
    model.summary()
    # 第一个全连接
    model.add(layers.Dense(units=globals['first_neuron_count'], activation='relu'))
    model.summary()
    # 正则化
    model.add(layers.Dropout(globals['dropout']))
    # 第二个全连接
    model.add(layers.Dense(units=TYPE, activation='softmax'))
    model.summary()

    model.compile(optimizer=RMSprop(lr=1e-4),
                  loss='binary_crossentropy',
                  metrics=['acc'])

    # history = model.fit(x_train, y_train,
    # epochs=epochs_,
    # batch_size=batch_size,
    # validation_split=validation_split_)
    if globals['KFCV']:
        for index in KFCV_index(globals['KFCV_K'], train_count):
            history = model.fit_generator(my_generator(x_train, y_train, index[0], globals['batch_size']),
                                          steps_per_epoch=int(index[2] / globals['batch_size']),
                                          validation_data=my_generator(x_train, y_train, index[1], 1),
                                          validation_steps=int(index[3] / 1),
                                          epochs=globals['epochs'], verbose=2)
    else:
        history = model.fit_generator(my_generator(x_train, y_train, [[0, train_count]], globals['batch_size']),
                                      steps_per_epoch=int(train_count / globals['batch_size']),
                                      validation_data=my_generator(x_val, y_val, [[0, val_count]], 1),
                                      validation_steps=int(val_count / 1),
                                      epochs=globals['epochs'], verbose=2)
    model.save(globals['save_model_path'])

    # 根据结果画图
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    # 测试集
    # test_loss, test_acc = model.evaluate(x_test, y_test)
    test_loss, test_acc = model.evaluate_generator(my_generator(x_test, y_test, [[0, test_count]], globals['batch_size']),
                                                   steps=int(test_count / globals['batch_size']))
    print('Testing and accuracy:', test_acc)

    plt.show()

    print("Having finished fourth step:deep learning!")


if __name__ == "__main__":
    from gensim.models import Word2Vec
    folders_set()
    globals = read_constant()

    word2vec_model = Word2Vec.load(globals['word2vec_model_path'])
    deep_learning(globals['TYPE'], globals['TYPE_list'], globals['type_map'], word2vec_model,globals)
