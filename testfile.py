import json


def test(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        print(file_data['features'][1])
        length = len(file_data['features'])
        print(length)




test()


# var fileStr = '{  "quote1":"texthere", "quote2":"texthere", "quote3":"texthere", "quote4":"texthere"}';
#
# var length = Object.keys(JSON.parse(fileStr)).length;
#
# console.log(length);
