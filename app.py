import pandas as pd
import making_html
import plot_logic


def corona(name):
    data_types = ['Coronavirus Cases', 'Deaths', 'Recovered']
    for data_type in data_types:
        with open(f'corona_{name}.csv') as f:
            data = f.read()
        data = data.replace('.', '')

        with open(f'corona_{name}.csv', 'w') as f:
            f.write(data)

        data_frame = pd.read_csv(f'corona_{name}.csv')
        data_frame.drop_duplicates(subset="Data", inplace=True)
        data_y_cases = data_frame[data_type]
        data_x_data = data_frame['Data']

        data_list_x = []
        for date in data_x_data:
            data_list_x.append(date[3:5])

        data_list_y = []
        for data in data_y_cases:
            data_list_y.append(data)

        result = plot_logic.draw_diagonal(data_list_x, data_list_y)

        x = result['label_x']
        y = result['label_y']
        html_x = result['pontos']

        html = making_html.drawing_html(x, y, html_x)
        making_html.save_html(f'corona_{name}', html)


if __name__ == '__main__':
    corona('world')
    #corona('italy')
    #corona('brazil')
    #corona('us')
    #corona('spain')

