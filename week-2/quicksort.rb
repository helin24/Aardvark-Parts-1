file = File.open('QuickSort.txt')

def quicksort(array)
	if array.length <= 1
		return [array, 0]
	end
	
	puts "#array starts out as #{array.inspect}"
	pivot = array[0]
	comparisons = 0
	comparisons += array.length - 1
	puts "#{comparisons} comparisons are made"
	
	first_greater_than_index = 1
	(array.length - 1).times do |index|
		location = index + 1
		if array[location] < pivot
			swap(array, location, first_greater_than_index)
			first_greater_than_index += 1
		end
	end
	puts "index of separation is #{first_greater_than_index}"
	swap(array, 0, first_greater_than_index - 1)
	left = quicksort(array[0..(first_greater_than_index - 1)])
	right = quicksort(array[first_greater_than_index..-1])
	
	array[0..(first_greater_than_index - 1)] = left[0]
	array[first_greater_than_index..-1] = right[0]
	comparisons += left[1] + right[1] 
	
	puts "array ends as #{array.inspect}"
	[array, comparisons]
	# base case is when there's only 1 number in array
	# otherwise each step involves choosing a pivot and comparing every other number in array with pivot
	# track number of comparisons
	# if number is smaller, then swap first >pivot with current number
	# else if number is bigger, leave it alone and move on to next number
	# once all numbers have been compared, swap pivot and the last number that is <pivot
	# recursive step - do the same thing for the numbers to the left of pivot and to the right of pivot
end

def swap(array, index1, index2)
	temp = array[index1]
	array[index1] = array[index2]
	array[index2] = temp
	array
end
