import sys, requests

if __name__ == '__main__':
    times = []
    totalTime = 0
    if len(sys.argv) != 3:
        print('Usage: {} <ip_server> <num_requests>'.format(sys.argv[0]))
        exit()
    
    for i in range(int(sys.argv[2])):
        time = requests.get(sys.argv[1]).elapsed.total_seconds()
        print('{} => {}'.format(i, time))
        times.append(time)

    for i in times:
        totalTime += float(i)

    print('Todas as Requisicoes => {}'.format(times))
    print('Media => {}'.format(totalTime/len(times)))


