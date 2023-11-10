import os

def delete_file(file_path):
   
    if os.path.exists(file_path):
       
        if os.access(file_path, os.W_OK):
            
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"Error: You do not have permission to delete the file '{file_path}'.")
    else:
        print(f"Error: File '{file_path}' not found.")


file_path_to_delete = 'your_file_path.txt'  # Replace with the path to the file you want to delete
delete_file(file_path_to_delete)
