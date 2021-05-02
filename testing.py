import win32com.client

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