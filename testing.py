import os.path
import hashlib
import os
import glob
import csv 
# returns a distribution of all the bytes in the file
# and the byte with the greatest consecutive count
def get_file_distribution( path,filename,):
    dists = [0 for i in range(256)]
    consecutive_byte = None
    consecutive_count = 0
    file = filename

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
    fullPath =  filename
    return os.path.getsize(fullPath) / 1000000, os.path.splitext(fullPath)[1]

def dataGeneration():
    fields = ['filename', 'file size', 'file type', 'file dist of bytes', 'consecutiveByte', 'consecutiveCount' ,'SHA-256', 'SHA-1', 'MD5', 'SHA-3-256']
    file = open("jpgHash.csv", "w")
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    path = r"/mnt/f/natural_images/airplane/"
    print(path)
    count = 0
    for filename in glob.glob(os.path.join(path, '*.jpg')):
        with open(os.path.join(os.getcwd(), filename), 'rb') as f:
            readFile = f.read()
            sha3 = hashlib.sha3_256(readFile).hexdigest()
            md5 = hashlib.md5(readFile).hexdigest()
            sha2 = hashlib.sha256(readFile).hexdigest()
            sha1 = hashlib.sha1(readFile).hexdigest()
            bytedist, consecutiveByte, consecutiveCount = get_file_distribution(path, filename)
            fileSize, fileType = get_file_metadata(path, filename)
            row = [filename, fileSize, fileType, str(bytedist), consecutiveByte, str(consecutiveCount), sha2, sha1, md5, sha3]
            # print(sha2)
            print(count)
            count += 1
            csvwriter.writerow(row)
        # if count == 5:
        #     break
        # break

if __name__ == '__main__':
    # path = r"/mnt/f/pdfs/"
    # filename = '5-Level Paging and 5-Level EPT - Intel - Revision 1.0 (December, 2016).pdf'
    # # print(get_file_metadata(path, filename))
    # a,b,c= (get_file_distribution(path, filename))
    # print(str(a))
    dataGeneration()