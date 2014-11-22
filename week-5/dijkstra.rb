require_relative 'graph'

class DijkstraGraph < Graph
	def line_to_vertex(line)
	# overwrites parent method
		pairs = line.split(/\t/)
		vertex = pairs.shift.to_i
		pairs.pop
		edges = {}
		pairs.each do |pair|
			pair = pair.split(',')
			edges.merge!(pair[0].to_i => pair[1].to_i)
		end
		{vertex => edges}
		# vertex format is {vertex => {other vertex => length, v3 => length, etc}}
	end

	def shortest_path(vertex)
		remaining_vertices = @vertices.dup
		x = remaining_vertices.delete(vertex)
		distances_within_x = {vertex => 0}
		distances_outside_x = {}
		min_distances(vertex, distances_outside_x, distances_within_x)
		#puts "remaining vertices = #{remaining_vertices} and @vertices is #{@vertices}"
		puts "min distances is #{distances_outside_x}"
		counter = 0
		while !distances_outside_x.empty? do
			puts counter
			counter += 1
			puts "distances outside x is #{distances_outside_x}"
			min_vertex = distances_outside_x.min_by {|outside_vertex,edge| edge[1]}
			puts "min vertex is #{min_vertex}"
			outside_vertex = min_vertex[0]
			closest_inside_vertex = min_vertex[1][0]
			distance_to_outside = min_vertex[1][1]
			distances_outside_x.delete(outside_vertex)
			total_distance = distances_within_x[closest_inside_vertex] + distance_to_outside
			puts "total distance between 1 and next vertex is #{total_distance}"
			distances_within_x.merge!(outside_vertex => total_distance)
			x.merge!(remaining_vertices.delete(outside_vertex))
			min_distances(outside_vertex, distances_outside_x,distances_within_x)
			# choose the closest next point
			# find distances of all vertices that could be reached from x
		end
		distances_within_x
	end

	def min_distances(new_vertex, distances_outside_x, distances_within_x)
		@vertices[new_vertex].each_pair do |other_vertex, new_length|
			# this should provide form {d4 => [d1,length], d5 => [d2, length]}
			break if distances_within_x.include?(other_vertex)
			current_closest= distances_outside_x[other_vertex]
			if current_closest == nil 
				distances_outside_x[other_vertex] = [new_vertex, new_length]
			else 
				current_length = current_closest[1]
				distances_outside_x[other_vertex] = [new_vertex, new_length] if current_length > new_length
			end
		end
	end
end
