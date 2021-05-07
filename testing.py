import win32com.client
import os.path

# returns a distribution of all the bytes in the file
# and the byte with the greatest consecutive count
def get_file_distribution(file):
    dists = [0 for i in range(256)]
    consecutive_byte = None
    consecutive_count = 0

    with open(file, "rb") as f:
        byte = f.read(1)
        curr_freq = 1
        prev_byte = byte
        
        while byte:
            dists[byte[0]] += 1

            if prev_byte != byte:
                if curr_freq > consecutive_count:
                    consecutive_byte, consecutive_count = prev_byte, curr_freq

                curr_freq = 0
                prev_byte = byte

            curr_freq += 1
            
            byte = f.read(1)

    return dists, consecutive_byte, consecutive_count

def get_file_metadata(path, filename):
    fullPath = path + "\\" + filename
    return os.path.getsize(fullPath) / 1000000, os.path.splitext(fullPath)[1]

if __name__ == '__main__':
    path = r"C:\Users\johne\PycharmProjects\CSC466-Project\images"
    filename = 'fish.jpg'
    print(get_file_metadata(path, filename))
