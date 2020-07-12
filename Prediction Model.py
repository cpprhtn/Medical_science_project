#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:56:18 2020

@author: cpprhtn
"""


'''
#SGD
#Momentum
#AdaGrad
#Adam
#4가지의 매개변수 갱신을 통해 가장 점수 잘 나오는 것을 쓸 예정

=>Conv2D 모델 사용


논문 져지 페이지 크롤링 -> beautifulSuop4 사용??


자연어 처리 예상과정
 NLTK 사용
 불용어 삭제 -> 사이킷런에서 불용어 단어 더 많이 제공
 단어 중요도에 따라 가중치 부여
         

가중치에 따라 단어 선택후, 그 단어를 이용한 문장 생성      
 seq2seq 사용
 어텐션 적용
 
'''
import numpy as np
import os
from os.path import join
from keras.preprocessing.image import load_img, img_to_array
from keras.models import Sequential
from keras.layers import ZeroPadding2D, Conv2D, MaxPooling2D
from keras.layers import Dropout, Dense, Flatten
from keras.optimizers import SGD

def img_paths(image_dir):
    image_filenames = os.listdir(image_dir)
    return [join(image_dir, filename) for filename in image_filenames if not filename.endswith('.DS_Store')]



#Images Load
train_normal_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/train/NORMAL'
test_normal_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/test/NORMAL'

train_normal_paths = img_paths(train_normal_dir)
test_normal_paths = img_paths(test_normal_dir)

train_pneumonia_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/train/PNEUMONIA'
test_pneumonia_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/test/PNEUMONIA'

train_pneumonia_paths = img_paths(train_pneumonia_dir)
test_pneumonia_paths = img_paths(test_pneumonia_dir)

val_normal_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/val/NORMAL'
val_normal_paths = img_paths(val_normal_dir)

val_pneumonia_dir = 'E:\Git_Hub\Medical_science_project/chest_xray/chest_xray/val/PNEUMONIA'
val_pneumonia_paths = img_paths(val_pneumonia_dir)



#Data preprocessing
image_size = 224

def read_and_prep_images(img_paths, img_height=image_size, img_width=image_size):
    imgs = [load_img(img_path, target_size=(img_height, img_width), grayscale=True) for img_path in img_paths]
    img_array = np.array([img_to_array(img) for img in imgs])
    return img_array

def make_data(normal_paths, pneumonia_paths):
    normal = read_and_prep_images(normal_paths)
    pneumonia = read_and_prep_images(pneumonia_paths)
    #print("normal's shape: ", normal.shape)
    #print("pneumonia's shape: ", pneumonia.shape)
    X = np.concatenate((normal, pneumonia))
    y = np.concatenate((np.zeros([normal.shape[0]], dtype=int), np.ones([pneumonia.shape[0]], dtype=int)))
    return X, y


X_train, y_train = make_data(train_normal_paths, train_pneumonia_paths)
print("X_train's shape: ", X_train.shape) #X_train's shape:  (5216, 224, 224, 1)
print("y_train's shape: ", y_train.shape) #y_train's shape:  (5216,)

X_test, y_test = make_data(test_normal_paths, test_pneumonia_paths)
print("X_test's shape: ", X_test.shape) #X_test's shape:  (624, 224, 224, 1)
print("y_test's shape: ", y_test.shape) #y_test's shape:  (624,)



#Hyperparameter Definition
learning_rate = 0.0001
batch_size = 128
epochs = 5
dropout = 0.25
seed = 0


#Conv2D + Maxpool + Conv2D + FC(전결합 레이어) + FC + softmax 모델 사용예정

model = Sequential()

model.add(ZeroPadding2D((1, 1)))
model.add(Conv2D(16, (4, 4), strides=(2, 2), activation='relu', input_shape=(image_size, image_size, 1)))
model.add(MaxPooling2D((2, 2), strides=(2, 2)))
model.add(Dropout(dropout, seed=seed))

model.add(ZeroPadding2D((2, 2)))
model.add(Conv2D(32, (8, 8), strides=(4, 4), activation='relu'))
model.add(Dropout(dropout, seed=seed))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(dropout, seed=seed))
model.add(Dense(1, activation='softmax'))

sgd = SGD(lr=learning_rate, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy', optimizer=sgd)

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
score = model.evaluate(X_test, y_test, batch_size=batch_size)


print(score)



