import win32com.client
import os.path

# returns a distribution of all the bytes in the file
def get_file_distribution(file):
    dists = [0 for i in range(256)]

    with open(file, "rb") as f:
        byte = f.read(1)
        while byte:
            dists[byte[0]] += 1
            byte = f.read(1)

    return dists

def get_file_metadata(path, filename):
    fullPath = path + "\\" + filename
    return os.path.getsize(fullPath) / 1000000, os.path.splitext(fullPath)[1]

if __name__ == '__main__':
    path = r"C:\Users\johne\PycharmProjects\CSC466-Project\images"
    filename = 'fish.jpg'
    print(get_file_metadata(path, filename))
