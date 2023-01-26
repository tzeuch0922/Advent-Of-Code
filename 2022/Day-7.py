# Tree class
class Folder_Node:
    def __init__(self, name):
        self.files = []
        self.folders = []
        self.size = 0
        self.name = name
        self.parent = None
        
    def get_size(self):
        return self.size
        
    def get_name(self):
        return self.name
        
    def get_parent(self):
        return self.parent
        
    def get_folder(self, name):
        idx = 0
        while True:
            if self.folders[idx].get_name() == name:
                return self.folders[idx]
            idx += 1
                
    def get_folder_array(self):
        return self.folders
        
    def add_file(self, file):
        self.files.append(file)
        
    def add_folder(self, folder):
        self.folders.append(folder)
        folder.update_parent(self)
        
    def update_parent(self, parent):
        self.parent = parent
        
    def update_size(self):
        size = 0
        for folder in self.folders:
            folder.update_size()
            size += folder.get_size()
        for file in self.files:
            size += file.get_size()
        self.size = size
        
# Tree File class
class File_Node:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name
        
    def get_size(self):
        return self.size

def sum_folders_under_threshold(folder):
    sum = 0
    for directory in folder.get_folder_array():
        sum += sum_folders_under_threshold(directory)
        directory_size = directory.get_size()
        if directory_size <= 100000:
            sum += directory_size
    return sum
    
def find_smallest_folder_over_threshold(folder, size, space_needed):
    small_size = size
    if folder.get_size() > space_needed and folder.get_size() < small_size:
        small_size = folder.get_size()
    for directory in folder.get_folder_array():
        dir_size = find_smallest_folder_over_threshold(directory, small_size, space_needed)
        if dir_size > space_needed and dir_size < small_size:
            small_size = dir_size
    return small_size

# Main
if __name__ == "__main__":
    input_file = open("Day-7-Input.txt", "r")
    line = input_file.readline()
    root = Folder_Node('/')
    current_directory = root
    line = input_file.readline()
    while line != "":
        if line.find("$ ls") == 0:
            line = input_file.readline()
            while line != "" and line[0] != "$":
                if line.find("dir") == 0:
                    folder_name = line[4:]
                    current_directory.add_folder(Folder_Node(folder_name))
                    child = current_directory.get_folder(folder_name)
                    child.update_parent(current_directory)
                else:
                    current_directory.add_file(File_Node(line[:line.find(" ")], line[line.find(" ")+1:]))
                line = input_file.readline()
        elif line.find("$ cd ..") == 0:
            current_directory = current_directory.get_parent()
            line = input_file.readline()
        elif line.find("$ cd ") == 0:
            current_directory = current_directory.get_folder(line[5:])
            line = input_file.readline()
    root.update_size()
    
    low_size_sum = sum_folders_under_threshold(root)
    
    total_space = 70000000
    root_space = root.get_size()
    space_needed = 30000000 - (total_space - root_space)
    smallest_folder_size = find_smallest_folder_over_threshold(root, root_space, space_needed)
    
    print("Part 1: " + str(low_size_sum))
    print("Part 2: " + str(smallest_folder_size))