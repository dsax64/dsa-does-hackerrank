import unittest


def largest_rectangle(ls):
    heights = []
    index = []
    largest_size = 0
    for i, x in enumerate(ls):
        if not heights or x > max(heights):
            heights.append(x)
            index.append(i)
        elif x < max(heights):
            while heights and x < max(heights):
                last_index = index.pop()
                temp_area_size = heights.pop() * (i - last_index)
                if largest_size < temp_area_size:
                    largest_size = temp_area_size
            heights.append(x)
            index.append(last_index)

    while heights:
        temp_area_size = heights.pop() * (len(ls) - index.pop())
        if largest_size < temp_area_size:
            largest_size = temp_area_size

    return largest_size


def solve():
    n = int(raw_input())
    numbers = map(int, raw_input().split(" "))
    print largest_rectangle(numbers)


class LargestRectangleTestCase(unittest.TestCase):
    def test_largest_rectangle_sample(self):
        self.assertEqual(largest_rectangle([1, 2, 3, 4, 5]), 9)

    def test_largest_rectangle_test_case1(self):
        self.assertEqual(largest_rectangle([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]), 26152)

    def test_largest_rectangle_test_case2(self):
        self.assertEqual(largest_rectangle([6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494]), 18060)

if __name__ == '__main__':
    unittest.main()
