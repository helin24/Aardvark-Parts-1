class Graph
	attr_reader :vertices

	def initialize(file)
		@vertices = {}
		f = File.open(file)
		f.each do |line|
			vertex = line_to_vertex(line)
			@vertices.merge!(vertex)
		end
	end
	
	def line_to_vertex(line)
		numbers = line.split(/\t/)
		{numbers[0].to_i => numbers[1..-2].map!{|char| char.to_i}}
	end
	
	def edges
		edge_pairs = []
		@vertices.each_pair do |v, edges|
			edges.each do |e| 
				edge_pairs << [v, e]
			end
		end
		edge_pairs # will give repeat pairs, e.g. [1,4] and [4,1]
	end
	
	def collapse(edge_pair)
		merged_edges = @vertices[edge_pair[0]] + @vertices[edge_pair[1]]
		edge_pair.each do |vertex|
			@vertices.delete(vertex)
		end
		@vertices.merge!(edge_pair => merged_edges)

		@vertices.each_pair do |vertex, edges|
			edges.map!{|edge| edge == edge_pair[0] || edge == edge_pair[1] ? edge_pair : edge }
		end

		@vertices[edge_pair].delete(edge_pair)
	end
end


