import hashlib
import os
import glob

# file1 = open("a.pdf", "rb")
# file2 = open("b.pdf", "rb")
file = open("pdfHash.txt", "a")
path = "/mnt/f/Acads/CSC-466/CSC466-Project/pdfs/pdfs"
print(path)
for filename in glob.glob(os.path.join(path, '*.pdf')):
   with open(os.path.join(os.getcwd(), filename), 'rb') as f:
       pdf1 = hashlib.sha256(f.read()).hexdigest()
       file.write(filename + " " + pdf1 + "\n")
       file.flush()
# pdf1 = hashlib.md5(file1.read()).hexdigest()
# pdf2 = hashlib.sha256(file2.read()).hexdigest()
# filename, file size, file type,  metadata, file dist of bytes, ALG:hash (Ex: SHA1:c342f...) <- multiple ALG:hash colummns
# print(pdf1, pdf2)
# print(pdf1==pdf2)