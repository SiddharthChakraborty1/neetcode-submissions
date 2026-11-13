class Solution:

    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return

        if len(temperatures) == 1:
            return [0]

        results = [0 for i in range(len(temperatures))]
        i, j = 0, 0
        temperature_len = len(temperatures)
        while i < temperature_len:
            current = temperatures[i]
            j = i+1
            distance = 1
            while j < temperature_len:
                if temperatures[j] > current:
                    results[i] = distance
                    break
                else:
                    distance += 1
                j +=1

            i += 1

        return results