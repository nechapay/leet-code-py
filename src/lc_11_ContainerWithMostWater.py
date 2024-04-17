# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are(i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
def maxArea(height):
    if len(height) < 2:
        return 0

    n = 0
    m = len(height) - 1
    mx = 0

    while n < m:
        dx = min(height[n], height[m])
        mx = max(mx, dx * (m-n))
        if height[m] > height[n]:
            n += 1
        else:
            m -= 1

    return mx


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))
