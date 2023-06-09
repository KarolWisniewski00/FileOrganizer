import os
import shutil


class FileOrganizer:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.folder_path_abs = os.path.abspath(folder_path)

    def get_files(self):
        files = []
        for file in os.listdir(self.folder_path_abs):
            if os.path.isfile(os.path.join(self.folder_path_abs, file)):
                files.append(file)
        return files

    def get_folders(self):
        folders = []
        for folder in os.listdir(self.folder_path_abs):
            if os.path.isfile(os.path.join(self.folder_path_abs, folder)) != True:
                folders.append(folder)
        return folders

    def get_extension(self, file):
        return os.path.splitext(file)[1]

    def get_list_extensions(self, files):
        list_extensions = []

        for file in files:
            extension = self.get_extension(file)
            if extension not in list_extensions:
                list_extensions.append(extension)

        return list_extensions

    def create_folders(self, extensions):
        list_folders = []
        for extension in extensions:
            os.makedirs(os.path.join(
                self.folder_path_abs, extension[1:]), exist_ok=True)
            list_folders.append(extension)
        return list_folders

    def create_folder(self):
        os.makedirs(os.path.join(
            self.folder_path_abs, 'folders'), exist_ok=True)

    def move_files(self, files, list_folders):
        for file in files:
            extension = self.get_extension(file)
            for folder in list_folders:
                if extension == folder:
                    try:
                        shutil.move(
                            "{}\{}".format(self.folder_path_abs, file),
                            "{}\{}".format(self.folder_path_abs, folder[1:]))
                    except:
                        print("[ERROR] Can't move {} file.".format(file))
                    break

    def move_folders(self, folders):
        for folder in folders:
            try:
                shutil.move(
                    "{}\{}".format(self.folder_path_abs, folder),
                    "{}\{}".format(self.folder_path_abs, 'folders'))
            except:
                print("[ERROR] Can't move {} file.".format(folder))

    def sort_by_extension(self, folder:bool=True):
        try:
            if folder:
                folders = self.get_folders()
                self.create_folder()
                self.move_folders(folders)
            files = self.get_files()
            extensions = self.get_list_extensions(files)
            list_folders = self.create_folders(extensions)
            self.move_files(files, list_folders)
        except:
            print("[ERROR] Can't sort.")


def main():
    file_organizer = FileOrganizer('test')
    file_organizer.sort_by_extension(folder=False)


if __name__ == '__main__':
    main()
