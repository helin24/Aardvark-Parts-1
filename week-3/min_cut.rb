

def min_cut(graph)
	# choose random edge
	# for the two vertices
	# collapse the two vertices together
end

class Graph
	def initialize(file)
		@vertices = {}
		f = File.open(file)
		f.each do |line|
			numbers = line.split(/\t/)
			@vertices.merge!(numbers[0].to_i => numbers[1..-2].map!{|char| char.to_i})
		end
	end
	
	def edges
		edge_pairs = []
		@vertices.each_pair do |v, edges|
			edges.each do |e| 
				edge_pairs << [v, e] if !edge_pairs.include?([e,v])
			end
		end
		edge_pairs
	end
	
	def collapse(edge_pair)
		# find the first one in vertices
		# save its array of connections
		# find second one in vertices
		# save its array of connections
		# make a new vertex that is [first vertex, second vertex]
		# new vertex points to all of the connections from the two
		merged_edges = @vertices[edge_pair[0]] + @vertices[edge_pair[1]]
		@vertices.merge!(edge_pair => merged_edges)
		edge_pair.each do |edge|
			@vertices.delete(edge)
		end
		@vertices		
		# remove self join
		# remove the old vertices

	end
end


