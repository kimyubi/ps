class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        cnt = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i] and not flowerbed[i - 1] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                cnt += 1

        return True if n <= cnt else False

