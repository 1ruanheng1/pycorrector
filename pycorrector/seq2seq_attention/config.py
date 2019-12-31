# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: Use CGED corpus
import os

pwd_path = os.path.abspath(os.path.dirname(__file__))

# Training data path.
# chinese corpus
raw_train_paths = [
    # os.path.join(pwd_path, '../data/cn/CGED/CGED18_HSK_TrainingSet.xml'),
    # os.path.join(pwd_path, '../data/cn/CGED/CGED17_HSK_TrainingSet.xml'),
    # os.path.join(pwd_path, '../data/cn/CGED/CGED16_HSK_TrainingSet.xml'),
    os.path.join(pwd_path, '../data/cn/CGED/sample_HSK_TrainingSet.xml'),
]

output_dir = os.path.join(pwd_path, 'output')
# Training data path.
train_path = os.path.join(output_dir, 'train.txt')
# Validation data path.
test_path = os.path.join(output_dir, 'test.txt')

# seq2seq_attn_train config
save_src_vocab_path = os.path.join(output_dir, 'vocab_srouce.txt')
save_trg_vocab_path = os.path.join(output_dir, 'vocab_target.txt')
model_dir = os.path.join(output_dir, 'models')
attention_image_path = os.path.join(output_dir, 'attention.png')

vocab_max_size = 6000
vocab_min_count = 5

batch_size = 64
epochs = 1
embedding_dim = 256
hidden_dim = 1024
maxlen = 128
gpu_id = 0

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
