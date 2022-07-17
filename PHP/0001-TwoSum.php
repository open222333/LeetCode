<?php
class Solution
{

	/**
	 * @param int|array $nums
	 * @param int $target
	 * @return int|array
	 */
	function twoSum(array $nums, int $target)
	{
		$map = [];
		foreach ($nums as $num) {
			$diff = $target - $num;
			if (array_key_exists($diff, $nums)) {
				$key_2 = array_search($diff, $map);
				$key_1 = array_search($num, $map);
				return [$key_1, $key_2];
			}
			$map[array_search($num, $nums)] = $num;
		}
	}
}

// A slightly optimized version of Approach 3 - One Pass Hash Table
// 8ms, 99%tile speed, 8%tile memory
class Solution1
{
	function twoSum(array $nums, int $target)
	{
		$map = [];
		// Important to not have count($nums) in the `for` loop. Else it will get executed every iteration.
		$size = count($nums);
		for ($i = 0; $i < $size; $i++) {
			$complement = $target - $nums[$i];
			if (array_key_exists($complement, $map)) {
				return [$i, $map[$complement]];
			}
			$map[$nums[$i]] = $i;
		}
	}
}
