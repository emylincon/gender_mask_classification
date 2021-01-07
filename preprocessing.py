import hashlib
import os
import random as r

female = f'MASK/female'
male = f'MASK/male'


class Preprocessing:
    def __init__(self, path):
        self.dict = {}
        self.duplicates = {}
        self.path = path

    @staticmethod
    def get_hash(file_rb):
        ha = hashlib.md5(file_rb)
        hash_no = ha.hexdigest()
        return hash_no

    def show_duplicates(self):
        amt = 0
        for i in self.duplicates.values():
            amt += len(i) - 1
        print(f'Length is {amt} \n{self.duplicates}')

    def add_duplicates(self, file_hash, filename):
        if file_hash in self.duplicates:
            self.duplicates[file_hash].append(filename)
        else:
            self.duplicates[file_hash] = [filename]

    def find_duplicates(self):
        self.dict, self.duplicates = {}, {}
        files = os.listdir(path=self.path)
        for file in files:
            file_rb = open(f"{self.path}/{file}", "rb")
            file_hash = self.get_hash(file_rb.read())
            if file_hash in self.dict:
                self.add_duplicates(file_hash=file_hash, filename=file)
            else:
                self.dict[file_hash] = file
        for i in self.duplicates:
            self.duplicates[i].append(self.dict[i])
        # return self.duplicates

    def remove_duplicates(self):
        self.find_duplicates()
        amt = 0
        for dup_list in self.duplicates.values():
            for file in dup_list[1:]:
                amt += 1
                os.remove(f'{self.path}/{file}')
        print(f'{amt} files have been deleted!')

    def rename_files(self):
        files = os.listdir(path=self.path)
        for ind in range(len(files)):
            file = r.choice(files)
            files.remove(file)
            filename, ext = os.path.splitext(file)
            name = f'{ind}'.zfill(6) + ext
            os.rename(f'{self.path}/{file}', f'{self.path}/{name}')
        print('Files renamed!')


obj = Preprocessing(path=male)
# obj.remove_duplicates()
obj.rename_files()
# obj.show_duplicates()
