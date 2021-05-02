import win32com.client

# returns a distribution of all the bytes in the file
def get_file_distribution(file):
    dists = [0 for i in range(256)]

    with open(file, "rb") as f:
        byte = f.read(1)
        while byte:
            dists[byte[0]] += 1
            byte = f.read(1)

    return dists

def get_file_metadata(path, filename, metadata):
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
    ns = sh.NameSpace(path)
    file_metadata = dict()
    item = ns.ParseName(str(filename))
    for ind, attribute in enumerate(metadata):
        attr_value = ns.GetDetailsOf(item, ind)
        if attr_value:
            file_metadata[attribute] = attr_value
    return file_metadata

if __name__ == '__main__':
    folder = r"C:\Users\johne\PycharmProjects\CSC466-Project\pdfs"
    filename = 'fish.jpg'
    metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created']
    print(get_file_metadata(folder, filename, metadata))
