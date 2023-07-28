from mpmath import mp


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_first_10_digit_prime_of_pi():
    decimal_places = 1000

    mp.dps = decimal_places
    pi = mp.pi

    pi_str = str(pi).replace(".", "")

    for i in range(len(pi_str) - 9):
        substr = pi_str[i:i + 10]
        number = int(substr)
        if is_prime(number):
            return substr

    return None


result = find_first_10_digit_prime_of_pi()
print("最初の10桁の素数:", result)
