#!/usr/bin/python3
"""
55. Jump Game
Difficulty: Medium

Success
Runtime: 5324 ms, faster than 8.17% of Python3 online submissions
Memory Usage: 16.5 MB, less than 5.51% of Python3 online submissions
"""
from typing import List
import time


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len <= 1: return True
        dp_list = {0: True}

        for i in range(nums_len):
            # see if current position reachable
            if i not in dp_list: return False

            # populating DP with all possible destination positions
            for j in range(nums[i]): dp_list[i + j + 1] = True

            # see if last position reachable
            if nums_len - 1 in dp_list: return True

        return True


sol = Solution()
print(sol.canJump(nums=[2, 0, 0]))

if sol.canJump(nums=[2, 3, 1, 1, 4]) != True: print('err-1')
if sol.canJump(nums=[3, 2, 1, 0, 4]) != False: print('err-2')
if sol.canJump(nums=[0]) != True: print('err-3')
if sol.canJump(nums=[2, 0]) != True: print('err-4')
if sol.canJump(nums=[2, 0, 0]) != True: print('err-5')
if sol.canJump(nums=[2, 5, 0, 0]) != True: print('err-6')

#
nums0 = [1 for _ in range(100000)]
print(f"list size = {len(nums0):,}")
stime = time.time()
if sol.canJump(nums=nums0) != True: print('err-74')
print(f'>>> runtime: {time.time() - stime:.2f}sec')

#
nums0 = [_ for _ in range(10000, -1, -1)]
nums0.append(0)
print(f"list size = {len(nums0):,}")
stime = time.time()
if sol.canJump(nums=nums0) != False: print('err-75')
print(f'>>> runtime: {time.time() - stime:.2f}sec')

#
stime = time.time()
if sol.canJump(
        nums=
        [14846, 18384, 13228, 11466, 6044, 8581, 2463, 8409, 16771, 5828, 9921, 17968, 16743, 266, 7398, 11849, 9176,
         8492, 3615, 12761, 19231, 5019, 899, 18700, 6844, 11404, 5737, 12006, 15351, 1197, 4812, 16677, 13715, 8361,
         6026, 10481, 9504, 15881, 5111, 12805, 15092, 5353, 11810, 1585, 9463, 6962, 16336, 19259, 8058, 19839, 19895,
         2484, 18093, 4654, 9012, 700, 16469, 368, 7062, 8080, 16281, 14375, 10685, 19734, 3738, 12634, 9837, 14291,
         10974, 18665, 1117, 12836, 18124, 15031, 4561, 2873, 14676, 15043, 1879, 15403, 13787, 3035, 1024, 2766, 19256,
         18073, 8194, 6913, 6208, 18134, 14157, 6796, 17399, 3464, 8527, 18973, 1867, 3445, 14051, 5157, 8552, 721,
         12912, 7104, 11992, 345, 14427, 2852, 11834, 6434, 3234, 4606, 10948, 11234, 4718, 861, 727, 18825, 9753,
         14365, 3070, 1725, 11303, 15844, 17072, 1172, 5232, 10219, 13744, 4615, 2749, 12763, 2063, 14238, 7563, 10462,
         13501, 11574, 11583, 8820, 6117, 844, 9577, 15681, 16478, 8812, 7721, 8204, 5949, 8740, 12730, 2357, 3354,
         4969, 18649, 15016, 10845, 6688, 8173, 5759, 5570, 691, 6136, 2205, 3064, 4230, 11687, 17559, 4751, 16775,
         7558, 19914, 9069, 13779, 17058, 7108, 18087, 18668, 14775, 13062, 17426, 10121, 9199, 13303, 795, 4950, 3249,
         9693, 19189, 17572, 3135, 7419, 16557, 6861, 17832, 1735, 2111, 18029, 9973, 15694, 6159, 2169, 2121, 7456,
         19218, 15263, 8007, 5583, 9125, 343, 10395, 19752, 19002, 5446, 2278, 5119, 4111, 3078, 14580, 19659, 2674,
         7738, 2228, 13495, 9910, 17867, 12330, 7396, 6643, 14094, 14286, 18242, 7994, 5001, 12487, 875, 14777, 5161,
         7476, 11744, 8568, 7187, 8771, 12068, 16495, 17961, 14591, 11036, 10484, 3333, 16075, 16287, 4928, 7119, 2321,
         9507, 11185, 8706, 3949, 5917, 17165, 10902, 14121, 2082, 2767, 14522, 8822, 6508, 5885, 9483, 17818, 18549,
         10830, 9279, 12318, 752, 19213, 16220, 12886, 10930, 7352, 18683, 5343, 12947, 12646, 13170, 2270, 16349,
         11286, 13927, 12862, 6817, 1133, 2954, 5424, 12856, 13252, 13989, 17570, 6923, 10389, 16956, 7967, 9656, 3569,
         16267, 5283, 6742, 2360, 15314, 19834, 5756, 6634, 11846, 93, 18601, 5550, 5523, 7783, 1173, 3476, 8351, 4990,
         4291, 2421, 14081, 12703, 4561, 17650, 14017, 7659, 6555, 19592, 581, 11371, 16975, 9447, 14570, 1917, 18330,
         1739, 14367, 6890, 2387, 3395, 7624, 8263, 5573, 9904, 3846, 3355, 15429, 9376, 4981, 15534, 17077, 10579,
         11576, 18464, 18283, 9003, 9160, 14116, 18648, 213, 16072, 12690, 4364, 15114, 4115, 19249, 14704, 12253, 4116,
         4956, 18151, 6951, 12477, 6865, 17355, 7501, 16913, 13478, 2359, 4718, 13005, 4101, 12315, 4472, 6375, 14442,
         16681, 7753, 394, 1538, 13261, 10904, 3803, 569, 271, 197, 7753, 745, 8040, 4765, 7054, 17806, 18088, 8207,
         9843, 13863, 17113, 18885, 7735, 6588, 14360, 6088, 11862, 19070, 5462, 361, 19864, 19312, 16717, 13734, 12722,
         8750, 13801, 3738, 19460, 12267, 7675, 15486, 9520, 2550, 19191, 121, 4185, 9336, 11802, 8049, 2819, 12623,
         3294, 2980, 9047, 6663, 9858, 17357, 15099, 13518, 9857, 17747, 12358, 19118, 14398, 11797, 6596, 5345, 773,
         14166, 16316, 13966, 9839, 6081, 7081, 18960, 1986, 6087, 9548, 6111, 11539, 18950, 9536, 4001, 4863, 2995,
         6364, 6789, 648, 3171, 17667, 13237, 13055, 11349, 10752, 19468, 13174, 14437, 18260, 1331, 6879, 15745, 2729,
         7265, 14877, 19929, 3750, 15996, 2009, 9074, 17727, 1854, 5286, 11262, 4411, 19871, 5279, 812, 15338, 12573,
         1699, 389, 2035, 425, 4312, 8559, 14451, 12078, 4564, 12072, 16368, 7901, 477, 7164, 11461, 7853, 11104, 385,
         14072, 15505, 9835, 19922, 17741, 3731, 13525, 15694, 13552, 3955, 1099, 15568, 14883, 13538, 16589, 2293,
         3080, 10758, 11608, 15842, 3897, 13703, 15673, 1743, 17319, 2729, 15315, 12379, 7974, 7016, 7325, 8864, 4980,
         14976, 19893, 11932, 11249, 7091, 6361, 3024, 10534, 6347, 2202, 4066, 128, 6842, 18370, 15935, 1559, 18115,
         17340, 8539, 10420, 9692, 16644, 5520, 18768, 13938, 9686, 19761, 17716, 9754, 3554, 4881, 15908, 14587, 3271,
         1535, 18453, 9796, 18563, 19518, 3782, 449, 15003, 18232, 1676, 9345, 14243, 5280, 10526, 17355, 5649, 3720,
         10324, 1224, 2117, 6897, 12519, 15139, 4018, 17460, 5958, 15935, 5295, 16415, 15207, 15714, 13501, 9983, 11983,
         15292, 16169, 11823, 1672, 19167, 8646, 6561, 15133, 2182, 10540, 14461, 19609, 17646, 641, 14723, 18092,
         12717, 307, 10872, 2350, 19916, 11241, 19602, 9641, 1857, 10879, 7435, 12492, 4403, 5322, 14442, 11463, 13203,
         16681, 7, 12558, 7549, 7633, 14320, 249, 7699, 4155, 4499, 9890, 17163, 3602, 11385, 10685, 3314, 14701, 10566,
         15661, 14648, 4935, 489, 13514, 7255, 9108, 17931, 15237, 17524, 8771, 15650, 18584, 12892, 5167, 15850, 1958,
         7295, 15813, 2815, 10942, 14999, 9677, 9816, 5696, 9284, 18277, 11977, 7510, 10300, 14795, 7810, 16801, 17801,
         19543, 13808, 11555, 12032, 16408, 480, 12309, 14525, 11749, 10174, 5446, 7335, 10822, 1855, 7993, 4472, 4320,
         8046, 2233, 12751, 15280, 19999, 552, 178, 16411, 3813, 16799, 7018, 3353, 16237, 8426, 16977, 453, 13591,
         4590, 11264, 4883, 6740, 2466, 132, 7047, 9856, 19569, 13862, 15227, 8298, 5819, 8790, 717, 2288, 3723, 2256,
         16542, 4696, 2746, 18493, 8566, 18474, 4190, 19761, 14188, 12050, 397, 16538]) != True: print('err-86')
print(f'>>> runtime: {time.time() - stime:.2f}sec')