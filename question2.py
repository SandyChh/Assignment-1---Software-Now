# Name: Sandeep Chhetri
# Student ID: s396070

def is_prime(num):
    for n in range(2,num):
        #checking reminder
        if num%n == 0:
            return False
    return True

def prime_numbers_upto(limit):
    primeNumbers = []
    #checking the prime numbers up to the limit
    for num in range(2,(limit+1)):
        if is_prime(num):               #calling the function to check if num is prime or not
            primeNumbers.append(num)    #saving the number into the list if it is a prime number
    return(primeNumbers)

def main():
    while(True):
        #exception handling for wrong input
        try:
            limit = int(input('Enter a limit(Max:100): '))
        except:
            print('Invalid input!')
            continue
        if limit <= 100:
            break
        print('Limit is up to 100. Enter again!')
        
    #calling the function to get list of prime numbers
    primeNumbers = prime_numbers_upto(limit)

    #converting the numbers into string first before joining them
    print('Prime numbers found:', (' '.join(str(num) for num in primeNumbers)))

    print('Total primes found:', len(primeNumbers))
    print('Largest prime:', max(primeNumbers))          #max function gives the largest number in a list
    print('Smallest prime:', min(primeNumbers))         #min function gives the smallest number in a list
    print('Sum of all primes:', sum(primeNumbers))      #sum function gives the sum of all numbers in a list

if __name__ == '__main__':
    main()