import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

sub_parsers = parser.add_subparsers(dest="command")
scan_parser = sub_parsers.add_parser("scan")
scan_parser.add_argument("path")

search_parser = sub_parsers.add_parser("search")
search_parser.add_argument("path")
search_parser.add_argument("keyword")

stats_parser = sub_parsers.add_parser("stats")
stats_parser.add_argument("path")

args = parser.parse_args()
command = args.command
# print("Command: ", args.command)
# print("Path: ",args.path)

path = Path(args.path)
# print("Path: ",path)
# print("Path: ",type(path))

# print("Path exists: ", path.exists())
# print("Path is a dir: ", path.is_dir())

def view_files_folders(files_folders):
    totalFiles = 0
    totalFolders = 0
    if files_folders:
        print("Files:\n")
        for item in files_folders:
            if item.is_file():
                print(item.name)
                totalFiles += 1
        print("\nDirectories:\n")
        for item in files_folders:
            if item.is_dir():
                print(item.name)
                totalFolders += 1
        print("\nTotal Files: ",totalFiles)
        print("Total Directories: ",totalFolders)
def format_size(totalFileSizeBytes):
    for unit in ["Bytes","KB","MB","GB","TB"]:
        if totalFileSizeBytes == 0:
            return f"{totalFileSizeBytes} Bytes"
        elif totalFileSizeBytes < 1024:
            return f"{totalFileSizeBytes:.2f} {unit}"
        totalFileSizeBytes /= 1024
    
def file_stats(files_folders):
    print("----------------- FILE STATISTICS ------------------------")
    totalFiles = 0
    totalFolders = 0
    totalFileSizeBytes = 0
    totalFileSize = 0
    

    if files_folders:
        for item in files_folders:
            if item.is_file():
                totalFiles += 1
                totalFileSizeBytes += item.stat().st_size
            if item.is_dir():
                totalFolders += 1
        totalFileSize = format_size(totalFileSizeBytes)
        print("Total Files: ",totalFiles)
        print("Total Folders: ",totalFolders)  
        print("Total Size: ",totalFileSize)
    else:
        print("Total Files: 0, Total Folders: 0, Total Size: 0 Bytes")
def search_files_folders(files_folders,search):
    total_matches = 0
    if files_folders:
        print("Search for files and folders")
        for item in files_folders:
            item_name_lower = item.name.lower()
            if search.lower() in item_name_lower:
                print(item.name)
                total_matches += 1
        if total_matches == 0:
            print("No matching files or folders found.")
        else:
            print("Search Results: ",total_matches)
    else:
        print("No files/folders available for search.")
      
print("----------------- File Manager -----------------")

if(path.exists() and path.is_dir()):
    files_folders = list(path.iterdir())
    match command:
        case "scan":
            view_files_folders(files_folders)
        case "search":
            search_files_folders(files_folders,args.keyword)
        case "stats":
            file_stats(files_folders)
    # totalFiles = 0
    # totalDirectories = 0
    # for item in path.iterdir():
    #     if item.is_file():
    #         totalFiles+=1
    #         # print(item.name) # file name
    #         # print(item.suffix) # file extension
    #         # print(item.stem) # file name without extension
    #     elif item.is_dir():
    #         # print(item.name)
    #         totalDirectories += 1
    # print("Total Files: ", totalFiles)
    # print("Total Directories: ", totalDirectories)
else:
    print("Enter a valid path for scanning.")


    
        
        