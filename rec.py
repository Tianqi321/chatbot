# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 02:53:57 2021

@author: Nene
"""

import json
from random import shuffle
import multiprocessing
import gensim
import csv


def train_song2vec():
    songlist_sequence = []
    for i in range(1, 1292):
        with open(r"D:\project\recommend_system_learning-master\neteasy_playlist_data/{0}.json".format(i), 'r', encoding='UTF-8') as load_f:
            load_dict = json.load(load_f)
            parse_songlist_get_sequence(load_dict, songlist_sequence)

    cores = multiprocessing.cpu_count()
    print('Using all {cores} cores'.format(cores=cores))
    print('Training word2vec model...')
    model = gensim.models.Word2Vec(sentences=songlist_sequence, size=150, min_count=3, window=7, workers=cores)
    print('Save model..')
    model.save('songVec.model')
def parse_songlist_get_sequence(load_dict, songlist_sequence):
    song_sequence = []
    for item in load_dict['playlist']['tracks']:
        try:
            song = [item['id'], item['name'], item['ar'][0]['name'], item['pop']]
            song_id, *song_name, artist, pop = song
            song_sequence.append(str(song_id))
        except:
            print('song format error')

    for i in range(len(song_sequence)):
        shuffle(song_sequence)
        songlist_sequence.append(list(song_sequence))


def song_data_preprocessing():
    csv_reader = csv.reader(open(r'D:\project\recommend_system_learning-master\neteasy_song_id_to_name_data.csv', encoding='utf-8'))
    id_name_dic = {}
    name_id_dic = {}
    for row in csv_reader:
        id_name_dic[row[0]] = row[1]
        name_id_dic[row[1]] = row[0]
    return id_name_dic, name_id_dic


train_song2vec()

model_str = 'songVec.model'
model = gensim.models.Word2Vec.load(model_str)
id_name_dic, name_id_dic = song_data_preprocessing()

song_id_list = list(id_name_dic.keys())[4000:5000:200]
for song_id in song_id_list:
    result_song_list = model.most_similar(song_id)
    print(song_id, id_name_dic[song_id])
    print('\n top sim score songs：')
    for song in result_song_list:
        print('\t' + id_name_dic[song[0]], song[1])
    print('\n')
