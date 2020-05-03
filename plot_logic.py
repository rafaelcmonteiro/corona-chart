def create_label_x(x_list, range_y=700):
    labels = []
    coordinates_x = []

    x_list.append(int(max(x_list)) + 1)
    distance_dif = range_y // len(x_list)
    x1 = 0
    for index, label in enumerate(x_list):
        x1 += distance_dif
        coordinates_x.append(int(x1))
        labels.append(f'<text x="{int(x1)}" y="525">{x_list[index]}</text>')

    axis_x = {
        "coordinates_x": coordinates_x,
        "labels": labels
    }

    return axis_x


def create_label_y(y_list, range_y=500, div=8):
    step = max(y_list) / 8
    y_list.append(step + max(y_list))
    max_label_value = max(y_list)
    print(y_list)
    labels = []
    coordinates_y = []

    distance_dif = range_y / div
    distance_label = max_label_value / div

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
        labels.append(f'<text x="780" y="{int(x1)}">{distance_label_y_list[index]:.2f}</text>')

    dict_list = {
        "coordinates_y": coordinates_y,
        "labels": labels,
        "rule": max_label_value
    }
    return dict_list


def draw_diagonal(label_x_data, label_y_data):
    dict_list_x = create_label_x(label_x_data)
    dict_list_y = create_label_y(label_y_data)

    # Pegando a regra para criacao dos pontos.
    rule = (dict_list_y["rule"])

    # Criando a sequencia que deve ser subtraida
    getting_rule_sequence = []
    for index, y in enumerate(label_y_data):
        # Regra de três
        rule_of_three = (500 * label_y_data[index]) / max(label_y_data)
        if rule_of_three > 500:
            getting_rule_sequence.append(500)
        else:
            getting_rule_sequence.append(rule_of_three)

    # Finalmente criando os pontos.
    rule_result = [500]

    # Subtraio 400 por um numero da sequencia.
    for index, y in enumerate(getting_rule_sequence):
        rule_result.append(500 - getting_rule_sequence[index])

    # Pegando valores de x

    list_x = dict_list_x['coordinates_x']

    new_list_x = list_x[1:]
    new_list_x.insert(0, 100)

    length = len(list_x)
    list_x = list_x[:length - 1]
    list_x.insert(0, 0)
    # definindo y1 e y2

    y1 = rule_result[:len(rule_result) - 1]
    y2 = rule_result[1:]

    html_values = []
    for index, x in enumerate(list_x):
        if index == 0:
            html_values.append(
                f'<line x1="{new_list_x[index]}" y1="{y2[index]}" x2="{new_list_x[index]}" y2="{y2[index]}" '
                f'style="stroke:rgb(255,0,0);stroke-width:2"/>')
        else:
            html_values.append(
                f'<line x1="{list_x[index]}" y1="{y1[index]}" x2="{new_list_x[index]}" y2="{y2[index]}" '
                f'style="stroke:rgb(255,0,0);stroke-width:2"/>')

    html_result = {
        "label_x": dict_list_x["labels"],
        "label_y": dict_list_y["labels"],
        "pontos": html_values[:-1]
    }

    return html_result
