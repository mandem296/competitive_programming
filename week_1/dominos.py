class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # initializing
        output = []
        dict = {3: "Fizz", 5: "Buzz"}
        divisors = [3, 5]

        for number in range(1, n + 1):
            result = []
            for div in divisors:
                if number % div == 0:
                    # where the result is divisible by either 3 or 5 we replace the no. in
                    # the array with what is defined in the dictionary {dict}

                    result.append(dict[div])
            if not result:
                result.append(str(number))
            output.append(''.join(result))
        return output