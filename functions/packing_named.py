# **kwargs
def result_f1(**podium):
    for position, pilot in podium.items():
        print(f'{position} -> {pilot}')


if __name__ == '__main__':
    result_f1(first='L. Hamilton', second='M. Verstappen', third='S. Vettel')
