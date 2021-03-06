#!/usr/bin/env python
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def train_valid_test_split(x_data, y_data, validation_size=0.1, test_size=0.1, shuffle=True):
    x_, x_test, y_, y_test = train_test_split(x_data, y_data, test_size=test_size, shuffle=shuffle)
    valid_size = validation_size / (1.0 - test_size)
    x_train, x_valid, y_train, y_valid = train_test_split(x_, y_, test_size=valid_size, shuffle=shuffle)

    return x_train, x_valid, x_test, y_train, y_valid, y_test

if __name__ == '__main__':

    def data_op(data_name):
        path = "data/" + data_name
        #pd_all = pd.read_csv(os.path.join(path, "imo_dis_test.csv"))
        pd_all = pd.read_excel(os.path.join(path, data_name + '.xlsx'))
        pd_all = shuffle(pd_all)
        x_data, y_data = pd_all.review, pd_all.label
        #x_data, y_data = pd_all.review.replace(r'\n\t\r', '', regex=True), pd_all.label

        x_train, x_valid, x_test, y_train, y_valid, y_test = train_valid_test_split(x_data, y_data, 0.1, 0.1)

        train = pd.DataFrame({'label':y_train, 'x_train': x_train})
        #train.to_csv(os.path.join(path, "train.csv"), index=False, sep='\t')
        with open(os.path.join(path, 'train.csv'), 'w', encoding='utf-8') as dstFile:
            dstFile.write('label\tx_train\n')
            for i in range(len(train)):
                dstFile.write(str(y_data[i]) + '\t' + ' '.join(str(x_data[i]).replace('\n', '').replace('\r', '').replace(';', ' ').split()) + '\n')
            dstFile.close()

        valid = pd.DataFrame({'label':y_valid, 'x_valid': x_valid})
        #valid.to_csv(os.path.join(path, "dev.csv"), index=False, sep='\t')
        with open(os.path.join(path, 'dev.csv'), 'w', encoding='utf-8') as dstFile:
            dstFile.write('label\tx_valid\n')
            for i in range(len(valid)):
                dstFile.write(str(y_data[i]) + '\t' + ' '.join(str(x_data[i]).replace('\n', '').replace('\r', '').replace(';', ' ').split()) + '\n')
            dstFile.close()

        test = pd.DataFrame({'label':y_test, 'x_test': x_test})
        #test.to_csv(os.path.join(path, "test.csv"), index=False, sep='\t')
        with open(os.path.join(path, 'test.csv'), 'w', encoding='utf-8') as dstFile:
            dstFile.write('label\tx_test\n')
            for i in range(len(test)):
                dstFile.write(str(y_data[i]) + '\t' + ' '.join(str(x_data[i]).replace('\n', '').replace('\r', '').replace(';', ' ').split()) + '\n')
            dstFile.close()


    data_name = input("训练文件夹:")
    data_op(data_name)

