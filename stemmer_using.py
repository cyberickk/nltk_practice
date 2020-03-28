#class IndexedText(object):  # 首先定义了一个类
#        #初始化参数 stemmer是提取词干的方法，text待处理文本，self的作用大家可以直接忽视但是必不可少
#      def __init__(self, stemmer, text):
#          self._text = text  # 将文本赋予变量self._text 
#          self._stemmer = stemmer  # 将提取词干的防范赋予self._stemmer
#          self._index = nltk.Index((self._stem(word), i)  # 循环读取文本中的词，最后生成{词干1:(index1,index2,..)}的样式
#                            for (i, word) in enumerate(text))          
          # 找出带处理词所处的index，然后提取index上下40个长度内的词
#      def concordance(self, word, width=40): 
#          key = self._stem(word)  # 提取待处理词的词干 
#          wc = width//4  # 获取大概需要提取词的个数 
#          for i in self._index[key]:  # 循环开始获取上下文
#              lcontext = ' '.join(self._text[i-wc:i])
#              rcontext = ' '.join(self._text[i:i+wc]) 
#              ldisplay = '%*s' % (width, lcontext[-width:])  # %*s右对齐，让打印出的长度是width 
#              rdisplay = '%-*s' % (width, rcontext[:width])  # %-*s左对齐，让打印出的长度是width
#              print (ldisplay, rdisplay, '/n')
#      def _stem(self, word):  # 词干提取并全部改为小写         
#          return self._stemmer.stem(word).lower()

class IndexedText(object):
	def __init__(self, stemmer, text):
		self._text = text
		self._stemmer = stemmer
		self._index = nltk.Index((self._stem(word), i)
						 for (i, word) in enumerate(text))
	def concordance(self, word, width=40):
		key = self._stem(word)
		wc = width//4
		for i in self._index[key]:
			lcontext = ' '.join(self._text[i-wc:i])
			rcontext = ' '.join(self._text[i:i+wc])
			ldisplay = '%*s' % (width, lcontext[-width:])
			rdisplay = '%-*s' % (width, rcontext[:width])
			print (ldisplay, rdisplay)
	def _stem(self, word):
		return self._stemmer.stem(word).lower()
