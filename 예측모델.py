#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:56:18 2020

@author: cpprhtn
"""


'''
SGD
Momentum
AdaGrad
Adam

4가지의 매개변수 갱신을 통해 가장 점수 잘 나오는 것을 쓸 예정


이후 논문 져지 크롤링후 자연어 처리
seq2seq같은걸루..
'''
import numpy as np
import os
from os.path import join


def img_paths(image_dir):
    image_filenames = os.listdir(image_dir)
    return [join(image_dir, filename) for filename in image_filenames if not filename.endswith('.DS_Store')]



#이미지 불러오기
train_normal_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/train/NORMAL'
test_normal_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/test/NORMAL'

train_normal_paths = img_paths(train_normal_dir)
test_normal_paths = img_paths(test_normal_dir)

train_pneumonia_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/train/PNEUMONIA'
test_pneumonia_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/test/PNEUMONIA'

train_pneumonia_paths = img_paths(train_pneumonia_dir)
test_pneumonia_paths = img_paths(test_pneumonia_dir)

val_normal_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/val/NORMAL'
val_normal_paths = img_paths(val_normal_dir)

val_pneumonia_dir = '/Users/cpprhtn/Desktop/git_local/Medical_science_project/chest_xray/chest_xray/val/PNEUMONIA'
val_pneumonia_paths = img_paths(val_pneumonia_dir)










