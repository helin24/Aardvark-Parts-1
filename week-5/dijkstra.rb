require_relative 'graph'

class DijkstraGraph < Graph
	def line_to_vertex(line)
	# overwrites parent method
		pairs = line.split(/\t/)
		vertex = pairs.shift
		pairs.pop
		edges = {}
		pairs.each do |pair|
			pair = pair.split(',')
			edges.merge!(pair[0] => pair[1])
		end
		{vertex => edges}
		# vertex format is {vertex => {other vertex => length, v3 => length, etc}}
	end
end
