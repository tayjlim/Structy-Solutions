Write a method, pairSum, that takes in an List and a target sum as arguments. The function should return an List containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

test_00

Source.pairSum(List.of(3, 2, 5, 4, 1), 8); // -> [0, 2]

test_01

Source.pairSum(List.of(4, 7, 9, 2, 5, 1), 5); // -> [0, 5]

test_02

Source.pairSum(List.of(4, 7, 9, 2, 5, 1), 3); // -> [3, 5]

test_03

Source.pairSum(List.of(1, 6, 7, 2), 13); // -> [1, 2]

test_04

Source.pairSum(List.of(9, 9), 18); // -> [0, 1]

test_05

Source.pairSum(List.of(6, 4, 2, 8 ), 12); // -> [1, 3]