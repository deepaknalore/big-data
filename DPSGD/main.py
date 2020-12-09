import matplotlib.pyplot as plt

FILE = ['dpsgd.csv', 'cpsgd_p2a.csv', 'cpsgd.csv']

def extract_from_file():
    data = {}
    for file in FILE:
        f = open(file, "r")
        lines = f.readlines()
        data[file.split('.')[0]] = {}
        data[file.split('.')[0]]['recv'] = []
        data[file.split('.')[0]]['send'] = []
        for line in lines:
            if '#' in line:
                continue
            line = line.split(",")
            data[file.split('.')[0]]['recv'].append(int(line[5]))
            data[file.split('.')[0]]['send'].append(int(line[6]))
    return data

def plot_graph(data, xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for algo in data:
        for i in ['send']:
            x_list = range(len(data[algo][i]))
            y_list = data[algo][i]
            plt.plot(x_list, y_list, label = algo+" - " + i)
            plt.legend()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = extract_from_file()
    #De-centralized
    plot_graph(data, "Time", "Communication (Bytes)")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
