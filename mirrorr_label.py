import os

path = r"F:\Programy\CrowdCounter\data\labels"
destination_path = r"F:\Programy\CrowdCounter\data\labels_mirrored"

items = os.listdir(path)

for item in items:
    if item.endswith(".txt"):  
        file_path = os.path.join(path, item)
        
        try:
            
            with open(file_path, "r") as file:  
                lines = file.readlines()  
            
            dest_file_path = os.path.join(destination_path, item)

            with open(dest_file_path, "w") as file:  
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 5:  
                        label = parts[0]
                        x = float(parts[1])
                        new_x = 1 - x
                        y = parts[2]
                        w = parts[3]
                        h = parts[4]

                        
                        modified_line = f"{label} {new_x:.6f} {y} {w} {h}\n"
                        file.write(modified_line)

            print(f"File {item} processed and updated.")
        
        except Exception as e:
            print(f"Cannot open or process file {item}: {e}")
