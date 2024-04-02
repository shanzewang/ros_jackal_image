import os
import fileinput

# Specify the path to the BARN folder
barn_folder = "/home/jidan/AVWorkSpace/new_jackal_ws/src/ros_jackal/jackal_helper/worlds/BARN"

# Traverse all files in the BARN folder
for filename in os.listdir(barn_folder):
    if filename.endswith(".world"):
        file_path = os.path.join(barn_folder, filename)
        
        # Modify the file content using the fileinput module
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if "<max_step_size>" in line:
                    print(" <max_step_size>0.01</max_step_size>")
                elif "<real_time_factor>" in line:
                    print(" <real_time_factor>10</real_time_factor>")
                else:
                    print(line, end="")
                    
print("Modification completed!")        