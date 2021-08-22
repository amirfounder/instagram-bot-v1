from src.utils.FileLogger import FileLogger
# from src.utils.FileSystem import FileSystem as fs
# from src.utils.FileWriter import FileWriter as fw

# fs = fs()
# fw = fw()

sample_dir = 'C:\\this\\is\\a\\test'
# sample_file1 = 'C:\\this\\is\\a\\test\\file.txt'
# sample_file2 = 'C:\\this\\is\\a\\test\\file.js'
# fw.set_file_path(sample_file1)

# fs.build_directories_from_file_path(sample_file1)
# fw.write_to_file('lol')

# fw.set_file_path(sample_file2)
# fw.write_to_file('lol')

# dirs = fs.get_files_from_directory(sample_dir)
# print(dirs)

MAX_FILE_SIZE = 25 * 1000 * 1000

fl = FileLogger()
fl.set_log_directory(sample_dir)
fl.set_max_file_size(MAX_FILE_SIZE)

message = '7 bytes'
message *= 1000

for i in range(100000):
  fl.log(message)