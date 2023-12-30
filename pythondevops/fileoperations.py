def update_file_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines=file.readlines()
    
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
                print("value for the key" + " " + key +" " + "updated to new value" + " " + value )
            else:
                file.write(line)
                # print("No updation done")

update_file_config("test.txt", "max_connection", "3000")
