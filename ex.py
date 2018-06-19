import os, re

docid, title, author, created, topic, tagging = [],[],[],[],[],[]

def files_in_dir(): #список файлов в дир.
    return os.listdir()

def change_dir(dir_name): #меняет директорию
    os.chdir(dir_name)

def opn(name):
    with open(name, encoding='windows-1251') as f:
        text = f.read()  
    return text

def find_inf(file_names):
    for file in file_names:
        global docid, title, author, created, topic, tagging
        txt = opn(file)
        docid.extend(re.findall(r'\<meta\scontent=\"([\w0-9\.]+)\"\sname=\"docid', txt))
        author.extend(re.findall(r'\<meta\scontent=\"([а-яА-Я\s]+)\"\sname=\"author', txt))
        created.extend(re.findall(r'\<meta\scontent=\"([0-9\.]+)\"\sname=\"created', txt))
        topic.extend(re.findall(r'\<meta\scontent=\"([\,\s\w]+)\"\sname=\"topic', txt))
        tagging.extend(re.findall(r'<meta\scontent=\"(\w+)\"\sname=\"tagging', txt))
        title.extend(re.findall(r'\<title\>([^\<]+)', txt))
def main():
    change_dir('news')
    find_inf(files_in_dir())
