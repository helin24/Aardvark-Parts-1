class DirectedGraph
	attr_reader :edges
	def initialize(filename)
		f = File.open(filename)
		@edges = []
		f.each do |line|
			@edges << line.split(' ').map!{|num| num.to_i} if line.length > 1
		end
	end
end

dg = DirectedGraph.new('test.txt')
puts dg.edges.inspect
