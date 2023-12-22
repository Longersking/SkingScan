from utils.character_tools import CharacterTools
from config.text_config import *
import json
import pandas as pd
from route import *
import pickle

class FileTools:
    @staticmethod
    def open_file(file_path, mode='r'):
        try:
            file = open(file_path, mode)
            return file
        except FileNotFoundError:
            CharacterTools.show(f"文件 '{file_path}' 未找到.",yellow)
        except Exception as e:
            CharacterTools.show(f"An error occurred: {e}",yellow)

    @staticmethod
    def read_file(file):
        if file:
            return file.read()
        else:
            CharacterTools.show("文件无法打开",yellow)

    @staticmethod
    def write_to_file(file, data):
        if file:
            file.write(data)
        else:
            CharacterTools.show("文件无法打开",yellow)

    @staticmethod
    def close_file(file):
        if file:
            file.close()
        else:
            CharacterTools.show("文件无法打开",yellow)

    @staticmethod
    def open_json_file(file_path, mode='r'):
        try:
            with open(file_path, mode) as file:
                return json.load(file)
        except FileNotFoundError:
            CharacterTools.show(f"JSON文件 '{file_path}' 未找到.", yellow)
        except Exception as e:
            CharacterTools.show(f"读取JSON文件时出错: {e}", yellow)

    @staticmethod
    def write_json_file(file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            CharacterTools.show(f"写入JSON文件时出错: {e}", yellow)

    @staticmethod
    def read_data_file(file_path):
        try:
            # 这里假设data文件是文本文件，可以按照需要自行处理数据格式
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            CharacterTools.show(f"Data文件 '{file_path}' 未找到.", yellow)
        except Exception as e:
            CharacterTools.show(f"读取Data文件时出错: {e}", yellow)

    @staticmethod
    def write_data_file(file_path, data):
        try:
            # 这里假设data文件是文本文件，可以按照需要自行处理数据格式
            with open(file_path, 'w') as file:
                file.write(data)
        except Exception as e:
            CharacterTools.show(f"写入Data文件时出错: {e}", yellow)

    @staticmethod
    def read_log_file(file_path):
        try:
            # 这里假设日志文件是文本文件，可以按照实际日志格式进行处理
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            CharacterTools.show(f"日志文件 '{file_path}' 未找到.", yellow)
        except Exception as e:
            CharacterTools.show(f"读取日志文件时出错: {e}", yellow)

    @staticmethod
    def write_log_file(file_path, log_data):
        try:
            # 这里假设日志文件是文本文件，可以按照实际日志格式进行处理
            with open(file_path, 'a') as file:
                file.write(log_data)
        except Exception as e:
            CharacterTools.show(f"写入日志文件时出错: {e}", yellow)

    @staticmethod
    def read_excel_file(file_path):
        try:
            # 使用Pandas库读取Excel文件
            return pd.read_excel(file_path)
        except FileNotFoundError:
            CharacterTools.show(f"Excel文件 '{file_path}' 未找到.", yellow)
        except Exception as e:
            CharacterTools.show(f"读取Excel文件时出错: {e}", yellow)

    @staticmethod
    def write_excel_file(file_path, data_frame):
        try:
            # 使用Pandas库将数据写入Excel文件
            data_frame.to_excel(file_path, index=False)
        except Exception as e:
            CharacterTools.show(f"写入Excel文件时出错: {e}", yellow)

    # 建立文件索引表
    @staticmethod
    def index_files(directory):
        file_index = {}
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_index[file] = file_path
        file_index = {str(index): {'filename': filename, 'path': path} for index, (filename, path) in
                        enumerate(file_index.items())}
        return file_index

    #保存索引
    @staticmethod
    def save_index(poc_dic,filename=DATA_DIR + r"\poc_dic.txt"):
        with open(filename, 'wb') as file:
            pickle.dump(poc_dic, file)

    #读取索引
    @staticmethod
    def load_index(filename=DATA_DIR + r"\poc_dic.txt"):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError as e:
            CharacterTools.show("[-]未建立文件索引",yellow)


if __name__ == '__main__':
    file_tools = FileTools()
    file_path = DATA_DIR + r"\pocs"
    #
    files_index = file_tools.index_files(file_path)
    file_tools.save_index(poc_dic=files_index)
    # # print(files_index)
    # poc_dic = file_path + r"\poc_dic"
    # # file_tools.save_index(poc_dic=files_index,filename=poc_dic)
    # index = file_tools.load_index(poc_dic)
    # print(index)
    # file_tools.save_index(files_index)
