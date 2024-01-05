Write a method, anagrams, that takes in two strings as arguments. The method should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

test_00

Source.anagrams("restful", "fluster"); // -> true

test_01

Source.anagrams("cats", "tocs"); // -> false

test_02

Source.anagrams("monkeyswrite", "newyorktimes"); // -> true

test_03

Source.anagrams("paper", "reapa"); // -> false

test_04

Source.anagrams("elbow", "below"); // -> true

test_05

Source.anagrams("tax", "taxi"); // -> false

test_06

Source.anagrams("taxi", "tax"); // -> false

test_07

Source.anagrams("night", "thing"); // -> true

test_08

Source.anagrams("abbc", "aabc"); // -> false

test_09

Source.anagrams("po", "popp"); // -> false

test_10

Source.anagrams("pp", "oo"); // -> false