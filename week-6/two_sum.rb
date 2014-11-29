require_relative '../week-2/quicksort.rb'

def two_sum(file)
	all_numbers = hash_file(file)
	number_array = all_numbers.keys
	count = 0
	(-10000..10000).each do |num|
		if sum_exists?(num, all_numbers, number_array)
			count += 1
			puts "#{num} exists"
			#puts "#{num} exists" if num % 100 == 0
		else
			puts "#{num} does not exist" if num % 100 == 0
		end
	end
	count
# each value goes into hash
# for each value -10,000 to 10,000
	# for each value in hash
	# check whether complementary value is in hash
end

def sum_exists?(num, hash, array)
	array.each do |key|
		return true if hash[num-key]
	end
	return false
end

def hash_file(file)
	f = File.open(file)
	hash = {}
	count = 0
	f.each do |line|
		num = line.to_i
		hash[num] = 1
		count += 1
		puts "#{count/10000.00}%" if count % 10000 == 0
	end
	hash
end
