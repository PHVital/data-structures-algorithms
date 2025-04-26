"""
443. String Compression (Medium)

Comprime um array de caracteres in-place. Grupos consecutivos do mesmo caractere são
substituídos pelo caractere seguido pela contagem de ocorrências (se maior que 1).

Exemplo:
Input: ["a","a","b","b","c","c","c"]
Output: ["a","2","b","2","c","3"], Retorno: 6

Complexidade:
- Tempo: O(n)
- Espaço: O(1) extra, pois a compressão é feita in-place.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):
            char = chars[i]
            count = 0

            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
