import pandas as pd


def draw_x_labels(label_x_data):
    label_len = len(label_x_data)
    build_label = []
    coordinates_x = []
    distance_dif = 700 // label_len
    x1 = 0
    for index, label in enumerate(label_x_data):
        x1 += distance_dif
        coordinates_x.append(int(x1))
        build_label.append(f'<text x="{int(x1)}" y="400">{label_x_data[index]}</text>')

    dict_list = {
        "coordinates_x": coordinates_x,
        "labels": build_label
    }

    return dict_list


def draw_y_labels(label_y_data):
    label_len = len(label_y_data)
    build_label = []
    coordinates_y = []
    another_label_y_data = label_y_data
    another_label_y_data.sort(reverse=True)
    distance_dif = 360 // label_len
    print(distance_dif)
    x1 = 0
    for index, label in enumerate(label_y_data):
        x1 += distance_dif
        coordinates_y.append(int(x1))
        build_label.append(f'<text x="80" y="{int(x1)}">{another_label_y_data[index]}</text>')

    dict_list = {
        "coordinates_y": coordinates_y,
        "labels": build_label
    }

    return dict_list


def draw_diagonal(label_x_data, label_y_data):
    list_values = []

    dict_list_x = draw_x_labels(label_x_data)
    dict_list_y = draw_y_labels(label_y_data)

    x_html_content = dict_list_x['labels']
    for x in x_html_content:
        print(x)

    print('')

    y_html_content = dict_list_y['labels']
    for y in y_html_content:
        print(y)

    print('')

    list_x = dict_list_x['coordinates_x']
    list_y = dict_list_y['coordinates_y']

    str_value = []
    list_y.sort(reverse=True)
    new_list_x = list_x[1:]
    new_list_y = list_y[1:]

    length = len(list_x)
    list_x = list_x[:length - 1]
    length = len(list_y)
    list_y = list_y[:length - 1]

    for index, value in enumerate(new_list_y):
        str_value.append(
            f'<line x1="{list_x[index]}" y1="{list_y[index]}" x2="{new_list_x[index]}" y2="{new_list_y[index]}" '
            f'style="stroke:rgb(255,0,0);stroke-width:2"/>')
    return str_value


def save_html(data):
    with open('chart.html', 'a') as f:
        f.write(data)


if __name__ == "__main__":
    tempo = [1, 2, 3, 4, 5, 6, 7]
    temperatura = [1, 4, 9, 16, 25, 36, 49]

    data_frame = pd.read_csv('corona_world.csv')

    data_frame.drop_duplicates(subset="Data", inplace=True)
    data_y_cases = data_frame['Coronavirus Cases']
    data_x_data = data_frame['Data']

    data_list_x = []
    data_list_y = []

    for date in data_x_data:
        data_list_x.append(date[3:5])

    #for date in data_y_cases:
    #    data_list_y.append((date))
    data_list_y = [1200000, 1400000, 1600000, 1800000, 2000000, 2200000, 2400000, 2600000, 2800000]
    line_html_content = draw_diagonal(tempo, temperatura)

    for line in line_html_content:
        print(line)


