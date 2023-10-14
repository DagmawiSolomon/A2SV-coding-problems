class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        products = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                pos1, pos2 = i+j, i+j+1
                carry, value = divmod(product + products[pos2], 10)
                products[pos1] += carry
                products[pos2] = value

        result = ""
        for digit in products:
            if not (len(result) == 0 and digit == 0):
                result += str(digit)
        return result if len(result) > 0 else "0"
