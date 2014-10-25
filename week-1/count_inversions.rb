def count_inversions(array)
	if array.length == 1
		return [array, 0]
	else
		n = array.length
		left_side = array[0..(n/2-1)]
		right_side = array[(n/2)..-1]
		
		left = count_inversions(left_side)
		right = count_inversions(right_side)

		left_arr = left[0]
		left_count = left[1]
		right_arr = right[0]
		right_count = right[1]

		split_count = 0
		sorted_arr = []
		total_length = left_arr.length + right_arr.length
		
		until left_arr.empty? || right_arr.empty? do
			if left_arr[0] < right_arr[0]
				sorted_arr << left_arr.shift
			else
				split_count += left_arr.length 
				sorted_arr << right_arr.shift
			end
		end	
		sorted_arr = sorted_arr + left_arr + right_arr
		
		return [sorted_arr, left_count + right_count + split_count]
	end
	# break into two arrays and count inversions on each
	# base case is when n=1, then inversion count increases by 0
	# sort while counting inversions
	# then go through and check how many inversions across two arrays
end

def file_to_array(file)
	File.open(file) do |f|
	end
end
