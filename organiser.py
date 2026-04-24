import os
import shutil

path = input('Enter path: ').strip()

if not os.path.exists(path):
    print('Invalid Path!')
    exit()

file_types = {
    'Images': ['jpg','jpeg','png','svg'],
    'Pdfs': ['pdf'],
    'Documents':['txt','pptx'],
    'Word':['docx','doc'],
    'Excell':['csv','xlsx'],
    'Videos':['mkv','mp4','avi'],
    'Audio':['mp3','wav'],
    'Zip':['zip'],
    'Others':[]
}

def move_file(source_path, dest_dir, filename):
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, filename)
    
    if not os.path.exists(dest_path):
        shutil.move(source_path, dest_path)
        return False # False means not a duplicate
    else:
        duplicates_dir = os.path.join(dest_dir, "duplicates")
        os.makedirs(duplicates_dir, exist_ok=True)
        
        base, extension = os.path.splitext(filename)
        counter = 1
        dup_path = os.path.join(duplicates_dir, filename)
        
        while os.path.exists(dup_path):
            new_name = f"{base}_{counter}{extension}"
            dup_path = os.path.join(duplicates_dir, new_name)
            counter += 1
            
        shutil.move(source_path, dup_path)
        return True # True means it was a duplicate

for file in os.listdir(path):
    filePath = os.path.join(path, file)

    if os.path.isfile(filePath):
        _, ext = os.path.splitext(file)
        ext = ext[1:].lower()
        moved = False

        for folder, extensions in file_types.items():
            if ext in extensions:
                is_duplicate = move_file(filePath, os.path.join(path, folder), file)
                if is_duplicate:
                    print(f'Duplicate: {file} → {folder}/duplicates/')
                else:
                    print(f'Moved: {file} → {folder}/')
                    
                moved = True
                break
        
        if not moved:
            is_duplicate = move_file(filePath, os.path.join(path, 'Others'), file)
            if is_duplicate:
                print(f'Duplicate: {file} → Others/duplicates/')
            else:
                print(f'Moved: {file} → Others/')

print('Files organized successfully!')
