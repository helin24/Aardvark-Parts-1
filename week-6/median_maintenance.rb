

def median_maintenance(file)
	arr = get_array_from_file(file)
	lower_half = Heap.new([arr.shift], false)
	upper_half = Heap.new([])
	sum_of_medians = lower_half.root
	arr.each do |new_num|
		original_median = lower_half.root
		if new_num < original_median
			if lower_half.length > upper_half.length
				removed = lower_half.remove_top
				upper_half.insert(removed)
			end
			lower_half.insert(new_num)
		elsif new_num == original_median
			if lower_half.length > upper_half.length
				upper_half.insert(new_num)
			else
				lower_half.insert(new_num)
			end
		elsif upper_half.length > 0 && new_num < upper_half.root
			if lower_half.length == upper_half.length
				lower_half.insert(new_num)
			else
				upper_half.insert(new_num)
			end
		else
			if lower_half.length == upper_half.length
				removed = upper_half.remove_top
				lower_half.insert(removed)
			end
			upper_half.insert(new_num)
		end
		
		median = lower_half.root
		sum_of_medians += median
#	puts "lower half is #{lower_half}"
#	puts "upper half is #{upper_half}"
	
#		puts "median is #{median}"
		puts "sum of medians is #{sum_of_medians}"
	end
	puts "length is #{arr.length}"
	sum_of_medians % 10000
end

def get_array_from_file(file)
	f = File.open(file)
	arr = []
	f.each do |line|
		arr << line.to_i
	end
	arr
end

class Heap
	def initialize(array, top_is_min = true)
		@heap = []
		@top_is_min = top_is_min
		array.each { |num| insert(num) }
		return self
	end

	def length
		@heap.length
	end

	def to_s
		@heap.inspect
	end

	def insert(num)
		@top_is_min ? @heap << num : @heap << -num
		position = @heap.length - 1
		until in_proper_place?(position) do
			position = bubble_up(position)
		end
	end

	def root
		@top_is_min ? @heap[0] : @heap[0] * -1
	end
	
	def remove_top
		top = @heap.shift
		last = @heap.pop
		@heap.unshift(last) if last != nil
		position = 0
		until in_proper_place?(position) do 
			position = bubble_down(position)
		end
		@top_is_min ? top : -top
	end

	def at_bottom?(position)
		@heap[2*position] + 1 == nil && @heap[2*position] + 2
	end
	
	def in_proper_place?(self_position)
		parents_right(self_position) && children_right(self_position)
	end
	
	def parents_right(self_position)
		return true if self_position == 0
		parent_position = (self_position + 1)/2 - 1
		@heap[self_position] >= @heap[parent_position]
	end
	
	def children_right(self_position)
		first_child = @heap[self_position *2 + 1]
		second_child = @heap[self_position *2 + 2]
		return true if first_child == nil && second_child == nil
		self_value = @heap[self_position]
		(first_child == nil || first_child >= self_value) && (second_child == nil || second_child >= self_value)
	end
	
	def bubble_up(self_position)
		parent_position = (self_position + 1)/2 - 1
		temp = @heap[self_position]
		@heap[self_position] = @heap[parent_position]
		@heap[parent_position] = temp
		parent_position
	end

	def bubble_down(self_position)
		first_child_position = self_position * 2 + 1
		second_child_position = first_child_position + 1
		temp = @heap[self_position]
		if @heap[second_child_position] == nil || @heap[first_child_position] <= @heap[second_child_position]
			@heap[self_position] = @heap[first_child_position]
			@heap[first_child_position] = temp
			return first_child_position
		else
			@heap[self_position] = @heap[second_child_position]
			@heap[second_child_position] = temp
			return second_child_position
		end
		
	end
end
