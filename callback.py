def dosomething(callback):
	i = 0
	j = 2
	k = i + 2
	
	callback(k)
	# for i in range(size):
	# 	if i % reportSize==0:
	# 		callback("{0} items processed".format(i))

def test():
	def cb(msg):
		print(msg)
	dosomething(cb)

if __name__ == '__main__':
	test()


# http://www.dreamincode.net/forums/topic/268087-callback-function-in-python/


# def dosomething(callback):
# 	size, reportSize = 20000, 1000
# 	callback("begin processing {0} items".format(size))
# 	for i in range(size):
# 		if i % reportSize==0:
# 			callback("{0} items processed".format(i))

# def test():
# 	def cb(msg):
# 		print(msg)
# 	dosomething(cb)

# if __name__ == '__main__':
# 	test()


# # http://www.dreamincode.net/forums/topic/268087-callback-function-in-python/