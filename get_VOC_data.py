__author__ = 'JGG'
import numpy as np
import os
import random
#from tensorflow.python.platform import gfile
import glob

#import TensorflowUtils as utils

def read_dataset(image_dir):
    # train_dataset = 'train.txt'
    # validation_dataset = 'val.txt'
    # f = open(train_dataset,'r')
    # train_image_name = []
    # for line in f :
    #     train_image_name.append(line.strip())
    # f.close()
    # f = open(validation_dataset,'r')
    # validation_image_name = []
    # for line in f:
    #     validation_image_name.append(line.strip())
    # f.close
    # print(len(train_image_name),len(validation_image_name))
    #print(validation_image_name)
    
    directories = ['training','validation']
    image_list={}

    for directory in directories:
        file_list = []
        image_list[directory] = []
        #file_glob = os.getcwd()+'/Data_zoo_pascal_ori'+'/image_data'+'/images'+'/'+directory+'/*.jpg'
        file_glob = os.getcwd()+'/Data_zoo'+'/image_data'+'/images'+'/'+directory+'/*.jpg'
        #print(file_glob)
        #print(glob.glob(file_glob))
        file_list.extend(glob.glob(file_glob))
        
        #if directory =='training':
            #for filename in train_image_name:
                #train_name = filename + '.jpg'
        #print(file_list)
        if not file_list:
            print('NO files found')
        else:
            for f in file_list:
                filename = os.path.splitext(f.split("/")[-1])[0]
                #print(filename)
                #annotation_file = os.getcwd() +'/Data_zoo_pascal_ori'+'/image_data'+'/annotations'+'/'+directory+'/'+filename+'.png'
                annotation_file = os.getcwd() +'/Data_zoo'+'/image_data'+'/annotations'+'/'+directory+'/'+filename+'.png'
                #print(annotation_file)
                record = {'image':f,'annotation':annotation_file,'filename':filename}
                image_list[directory].append(record)
        random.shuffle(image_list[directory])  
        no_of_images = len(image_list[directory])
        print ('No. of %s files: %d' % (directory, no_of_images))
    training_records = image_list['training']
    validation_records = image_list['validation']
    return training_records ,validation_records
#image_dir = '\\image_data'
#read_dataset(image_dir)

    