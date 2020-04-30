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
        build_label.append(f'<text x="{int(x1)}" y="425">{label_x_data[index]}</text>')

    dict_list = {
        "coordinates_x": coordinates_x,
        "labels": build_label
    }

    return dict_list


def draw_y_labels(label_y_data):
    label_len = len(label_y_data)
    max_label_value = max(label_y_data)

    build_label = []
    coordinates_y = []

    distance_dif = 400 // 8
    distance_label = max_label_value // 8

    # print('Distance label', distance_label)
    # print(distance_dif)

    number_list = []
    x1 = 0
    distance_label_y = 0
    distance_label_y_list = []
    for index in range(8):
        distance_label_y_list.append(distance_label_y)
        distance_label_y = distance_label + distance_label_y

    distance_label_y_list.sort(reverse=True)

    for index in range(8):
        x1 += distance_dif
        coordinates_y.append(int(x1))
        build_label.append(f'<text x="720" y="{int(x1)}">{distance_label_y_list[index]}</text>')

    dict_list = {
        "coordinates_y": coordinates_y,
        "labels": build_label,
        "rule": max_label_value
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

    # Pegando a regra para criacao dos pontos.
    rule = (dict_list_y["rule"] - 1)

    # Criando a sequencia que deve ser subtraida
    getting_rule_sequence = []
    for x in range(7):
        if x == 6:
            getting_rule_sequence.append(400)
        else:
            getting_rule_sequence.append((400 * label_y_data[x]) // rule)

    # Finalmente criando os pontos.

    rule_result = [400.0]
    for x in range(7):
        rule_result.append(400 - getting_rule_sequence[x])

    # Pegando valores de x

    list_x = dict_list_x['coordinates_x']

    str_value = []
    new_list_x = list_x[1:]

    length = len(list_x)
    list_x = list_x[:length - 1]
    print(new_list_x)
    print(list_x)
    # definindo y1 e y2

    y1 = rule_result[:len(rule_result) - 1]
    y2 = rule_result[1:]
    html_values = []
    for index in range(6):
        html_values.append(
            f'<line x1="{list_x[index]}" y1="{y1[index]}" x2="{new_list_x[index]}" y2="{y2[index]}" '
            f'style="stroke:rgb(255,0,0);stroke-width:2"/>')

    print('')

    for index in range(6):
        print(html_values[index])
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

    # for date in data_y_cases:
    #    data_list_y.append((date))
    data_list_y = [1200000, 1400000, 1600000, 1800000, 2000000, 2200000, 2400000, 2600000, 2800000]
    line_html_content = draw_diagonal(tempo, temperatura)

    # for line in line_html_content:
    # print(line)

