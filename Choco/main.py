import matplotlib.pyplot as plt

# FILE = 'Choco/decen_cen.txt'
# FILTER = ['decentralized-exact:', 'centralized:']

FILE = 'Choco/algo_comp.txt'
FILTER = ['EAMSGD-sync:', 'EAMSGD-async:', 'SGP:', 'AD-PSGD:']


def extract_from_file():
    data = {}
    f = open(FILE, "r")
    lines = f.readlines()
    for line in lines:
        for filter in FILTER:
            if filter in line:
                if filter not in data:
                    data[filter] = []
                line = line.split(':')[1]
                line = line.split(',')
                info = [l.split(" = ")[1] for l in line]
                info[4] = 1 - float(info[4])
                info[5] = info[5].split(' ')[0]
                info[6] = info[6].split(' ')[0]
                data[filter].append(info)
    return data

def plot_graph(data, x, y, xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for feature in FILTER:
        info = data[feature]
        x_list = []
        y_list = []
        for i in info:
            x_list.append(float(i[x]))
            y_list.append(float(i[y]))
        plt.plot(x_list, y_list, label = feature[:-1])
        plt.legend()
    plt.show()

def plot_average_graph(data, x, y, xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for feature in FILTER:
        info = data[feature]
        x_list = []
        y_list = []
        dict = {}
        for i in info:
            if int(i[x]) not in dict:
                dict[int(i[x])] = 0
            dict[int(i[x])] += float(i[y])

        for key in dict:
            x_list.append(key)
            y_list.append(dict[key]/len(dict))
        plt.plot(x_list, y_list, label = feature[:-1])
        plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = extract_from_file()
    #De-centralized
    plot_graph(data, 5, 3, "Training Time(s)", "Training Loss")
    plot_graph(data, 5, 4, "Training Time(s)", "Training Error")
    plot_average_graph(data, 1, 3, "Epoch", "Training Loss")
    plot_average_graph(data, 1, 4, "Epoch", "Training Error")
    plot_graph(data, 6, 3, "MiB Transmitted", "Training Loss")
    plot_graph(data, 6, 4, "MiB Transmitted", "Training Loss")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
