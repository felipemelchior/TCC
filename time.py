import sys, requests

if __name__ == '__main__':
    times = []
    totalTime = 0
    urls = ['applications.php', 'logado.php?nome=normal', 'logado.php?nome=<script>alert(1);</script>']
    
    if len(sys.argv) < 3:
        print('Usage: {} <ip_server> <num_requests> <verbose>'.format(sys.argv[0]))
        exit()
    
    for url in urls:
        print(url   )
        for i in range(int(sys.argv[2])):
            time = requests.get(sys.argv[1]+'/Vulnerabilidades/'+url).elapsed.total_seconds()
            #print('{} => {}'.format(i, time))
            times.append(time)            

        for j in times:
            totalTime += float(j)
        
        print('Media => {}'.format(totalTime/len(times)))
        totalTime = 0
        times = []