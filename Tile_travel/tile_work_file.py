def save_progress(filename, instance_of_grid, instance_of_player):
    with open(filename, "w") as file_content:
        file_content.write(instance_of_grid)
        file_content.write(instance_of_player)
        

filename = "save.txt"
instance_of_grid = "Dimension of board:\n4\nLocation of walls:\n1,1-2,1 2,1-3,1 2,2-3,2 2,2-2,3 3,2-3,3\nLocation of levers:\n0"
instance_of_player = "\nGold coins\n0\nPlayer position:\n1,1"
save_progress(filename, instance_of_grid, instance_of_player)