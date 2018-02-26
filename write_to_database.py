import json

game_list = json.load(open("database.json"))



while True:
    try:
        input_name = raw_input("Game name")
        input_path = raw_input("Save path")
        game_list.append((input_name, input_path))
    except KeyboardInterrupt:
        print "done"
        json.dump(game_list, open("database.json", "w"), indent=4)
        exit()
