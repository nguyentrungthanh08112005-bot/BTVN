primes_gen = (
    n for n in range(2, 21) 
    if all(n % i != 0 for i in range(2, int(n**0.5) + 1))
)

print("--- Bắt đầu lấy các số nguyên tố bằng next() ---")

print(f"Số thứ 1: {next(primes_gen)}")
print(f"Số thứ 2: {next(primes_gen)}")
print(f"Số thứ 3: {next(primes_gen)}")
print(f"Số thứ 4: {next(primes_gen)}")
print(f"Số thứ 5: {next(primes_gen)}")