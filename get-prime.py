def get_primes(higher_bound):
    if higher_bound <= 2:
        return
    prime_count = 0
    for num in range(2, higher_bound):
        is_prime = True
        for curr_num in range(2, int(num / 2) + 1):
            if num % curr_num == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

    print("Number of Primes between 2 and {} is {}".format(
        higher_bound, prime_count))
    return prime_count


higher = int(input("Enter a positive integer greater than 2: "))
prime_count = get_primes(higher)
# print("There are {} primes between 2 and {}".format(prime_count, higher))
