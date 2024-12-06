import os

def get_file_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

def analyze_folder(folder_path):
    file_details = []
    total_size = 0
    total_files = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                total_size += file_size
                total_files += 1
                file_details.append((file_path, file_size))
            except OSError:
                print(f"Could not access file: {file_path}")

    file_details.sort(key=lambda x: x[1], reverse=True)
    
    return total_files, total_size, file_details

def main():
    print("Welcome to Local Folder Analyzer!")
    folder_path = input("Enter the path of the folder to analyze: ").strip()

    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return
    
    total_files, total_size, file_details = analyze_folder(folder_path)

    print("\n--- Folder Analysis Report ---")
    print(f"Total Files: {total_files}")
    print(f"Total Storage Used: {get_file_size(total_size)}\n")
    print("Top 10 Largest Files:")
    
    for idx, (file_path, file_size) in enumerate(file_details[:10], start=1):
        human_readable_size = get_file_size(file_size)
        relative_path = os.path.relpath(file_path, folder_path)
        print(f"{idx}. {relative_path} - {human_readable_size}")

if __name__ == "__main__":
    main()
