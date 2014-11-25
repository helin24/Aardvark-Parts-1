require_relative 'graph'
require 'pry'

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
	end

	def shortest_path(vertex)
		remaining_vertices = @vertices.dup
		x = remaining_vertices.delete(vertex)
		distances_within_x = {vertex => 0}
		distances_outside_x = {}
		min_distances(vertex, distances_outside_x, distances_within_x)
		while !distances_outside_x.empty? do
			min_vertex = distances_outside_x.min_by {|outside_vertex,edge| edge[1]}
			outside_vertex = min_vertex[0]
			closest_inside_vertex = min_vertex[1][0]
			distance_to_outside = min_vertex[1][1]
			distances_outside_x.delete(outside_vertex)
			distances_within_x.merge!(outside_vertex => distance_to_outside)
			x.merge!(remaining_vertices.delete(outside_vertex))
			min_distances(outside_vertex, distances_outside_x,distances_within_x)
		end
		distances_within_x
	end

	def min_distances(new_vertex, distances_outside_x, distances_within_x)
		@vertices[new_vertex].each_pair do |other_vertex, new_length|
			next if distances_within_x.include?(other_vertex)
			distance_from_origin = distances_within_x[new_vertex]
			current_closest = distances_outside_x[other_vertex]
			total_length = distance_from_origin + new_length
			if current_closest == nil
				distances_outside_x[other_vertex] = [new_vertex, total_length]
			else 
				current_length = current_closest[1]
				if current_length > total_length 
					distances_outside_x[other_vertex] = [new_vertex, total_length]
				end
			end
		end
	end
end
