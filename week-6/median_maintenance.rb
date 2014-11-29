

def median_maintenance(file)
	arr = get_array_from_file(file)
	heap = Heap.new(arr)
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
		top_is_min = top_is_min
		array.each { |num| insert(num) }
		return self
	end

	def insert(num)
		@heap << top_is_min ? num : -num
		position = @heap.length - 1
		until in_proper_place?(position) do
			position = bubble_up(position)
		end
	end
	
	def in_proper_place?(self_position)
		return true if self_position == 0
		parent_position = (self_position + 1)/2 - 1
		@heap[self_position] >= @heap[parent_position]
	end
	
	def bubble_up(self_position)
		parent_position = (self_position + 1)/2 - 1
		temp = @heap[self_position]
		@heap[self_position] = @heap[parent_position]
		@heap[parent_position] = temp
		parent_position
	end
end
