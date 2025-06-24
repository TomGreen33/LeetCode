class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def compute_quotient(max_quotient, divisor):
            two_pow_j_counter = 1
            quotient = divisor
            
            if divisor == 0:
                if dividend > 0:
                    return 2**31-1
                else:
                    return -2**31

            while quotient < max_quotient:
                quotient <<= 1
                two_pow_j_counter <<= 1

            if quotient > max_quotient:
                quotient >>= 1
                two_pow_j_counter >>= 1

            if max_quotient - quotient >= divisor:
                return two_pow_j_counter + compute_quotient(max_quotient - quotient, divisor)
            else:
                return two_pow_j_counter


        if (dividend > 0 and divisor < 0):
            result = compute_quotient(dividend, -divisor)
            result = -result
        elif (dividend < 0 and divisor > 0):
            result = compute_quotient(-dividend, divisor)
            result = -result
        elif  (dividend < 0 and divisor < 0):
            result = compute_quotient(-dividend, -divisor)
        else:
            result = compute_quotient(dividend, divisor)
            
        if result > 2**31-1:
            result = 2**31-1
        elif result < -2**31:
            result = -2**31
        
        return result
