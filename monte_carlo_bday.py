from random import randint

def monte_carlo_bday(N,num_iter):
    s=0
    for _ in range(num_iter):
        bdays=[randint(1,366) for i in range(N)]
        if not len(set(bdays))==len(bdays):
            s+=1
    s/=num_iter
    return s

def main():
    n=int(input('Type the number of people: '))
    it=int(input('Type the number of simulations: '))
    print('Probability: %f'%monte_carlo_bday(n,it))

if __name__ == '__main__':
    main()