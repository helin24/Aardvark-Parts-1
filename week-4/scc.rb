class DirectedGraph
	attr_reader :vertices, :max_vertex, :reverse_vertices
	def initialize(filename)
		f = File.open(filename)
		@vertices = {}
		@reverse_vertices = {}
		f.each do |line|
			if line.length > 1
				edge = line.split(' ').map!{|num| num.to_i}
				origin = edge[0]
				destination = edge[1]
				if @vertices[origin] == nil
					@vertices[origin] = [destination]
				else
					@vertices[origin] << destination
				end
				if @reverse_vertices[destination] == nil
					@reverse_vertices[destination] = [origin]
				else
					@reverse_vertices[destination] << origin
				end
			end
		end
		puts "vertices done"
	#	@max_vertex = 875714
		@max_vertex = @vertices.keys.max
	end

	def largest_sccs(num_of_sccs)
		puts "finding topography"
		order = topography
		clusters = []
		vertex_order = order.sort_by{|_,o| o}.map{|pair| pair[0]}.reverse
		
		orders = {}
		vertex_order.each do |vertex|
			puts "SCC on vertex #{vertex}"
			# puts "each vertex in ordering"
			count = 0
			next if orders[vertex]
			discovered = [vertex]
			while !discovered.empty?
				# puts "in while loop"
				# puts "orders is #{orders}"
				current_vertex = discovered[-1]
				next_vertex = unexplored_destination(current_vertex, @vertices, discovered, orders)
				if next_vertex
					discovered << next_vertex
				else
					count += 1
					orders.merge!(current_vertex => true)
					discovered.pop
				end
			end
			clusters << count
		end	
		clusters[0..num_of_sccs - 1]
		# order the topographical hash by value, and for each
		# depth first same process but every time picking a fresh vertex, count number of connections as 0
		# every time there are further nodes to explore add 1 to count in scc
		# push these into an array of SCCs
		# return the top (num of sccs) SCCs
	end
	
	def topography
		# go through array 1..end
		# maintain a list of which vertices have been discovered (these will be dealt with LIFO)
		# start with order equal to highest number of vertices (will count down)
		# maintain a list of explored vertices - those that have no remaining unexplored vertices
		# when a vertex has been fully explored, add to hash vertex: order and increment order down
		discovered = []
		orders = {}
		count = @max_vertex
#		@reverse_vertices.each_pair do |vertex, destinations|
#			puts "topography on vertex #{vertex}"
#			next if orders[vertex]
#			discovered = [vertex]
#			while !discovered.empty?
#				current_vertex = discovered.last
#				next_vertex = next_destination(current_vertex,
#			end
#		end
		undiscovered = (1..@max_vertex).to_a
		while count > 0 do
			discovered = [undiscovered.shift]
			puts "topography on vertex #{discovered[0]}"
			while !discovered.empty? 
				current_vertex = discovered[-1]
				# puts "current vertex is #{current_vertex}"
				next_vertex = unexplored_destination(current_vertex, @reverse_vertices, discovered, orders)
				if next_vertex
					discovered << next_vertex
					undiscovered.delete(next_vertex)
					# puts "discovered is #{discovered}"
				else
					# puts "found an end"
					orders.merge!(current_vertex => count)
					# puts "orders is now #{orders}"
					count -= 1
					discovered.pop
				end
				puts "explored is #{orders.count}"
#				puts "discovered is #{discovered.count}"
			end		


		end
#		(1..@max_vertex).each do |vertex|
#			puts "topography on vertex #{vertex}"
#			next if orders[vertex] 
#			discovered = [vertex]
#			while !discovered.empty? 
#				current_vertex = discovered[-1]
#				# puts "current vertex is #{current_vertex}"
#				next_vertex = unexplored_destination(current_vertex, @reverse_vertices, discovered, orders)
#				if next_vertex
#					discovered << next_vertex
#					# puts "discovered is #{discovered}"
#				else
#					# puts "found an end"
#					orders.merge!(current_vertex => count)
#					# puts "orders is now #{orders}"
#					count -= 1
#					discovered.pop
#				end
#				puts "explored is #{orders.count}"
#				puts "discovered is #{discovered.count}"
#			end		
#
#			# unless no unexplored vertices from connections
#			# add vertex to discovered
#			# add edges to discovered 
#		end
		orders
	end

	def unexplored_destination(vertex, vertices, discovered, orders)
		# puts "exploring vertex #{vertex}"
		destinations = vertices[vertex]
		# puts "destinations are #{destinations}"
		return nil if destinations == nil
		destinations.each do |dest|
			if orders[dest] != nil
				next
			elsif discovered.include?(dest)
				next
			else
				return dest
			end
		end
		return nil
	end
end

require 'ruby-prof'
RubyProf.start
dg = DirectedGraph.new('test.txt')
dg.largest_sccs(5)
result = RubyProf.stop
printer = RubyProf::FlatPrinter.new(result)
printer.print(STDOUT)
