#coding=utf8
def gen_pnext(p):
	'''前缀后缀表'''
	i,k,m = 0,-1,len(p)
	pnext = [-1] * m
	while i < m-1:
		if k == -1 or p[i] == p[k]:
			i,k = i+1,k+1#后移
			pnext[i] = k
		else:
			k = pnext[k]#回溯
	return pnext

def matching_KMP(text,pattern):
	'''
	KMP算法
	返回pattern在text中出现的次数和位置列表
	'''
	j = 0#j指向text
	i = 0#i指向pattern
	str_count = 0#记录已匹配的字符数
	sum = 0
	n = len(text)
	m = len(pattern)
	des = []#存储位置的列表
	pnext = gen_pnext(pattern)#调用函数得到pnext数组
	# while j < n and i < m:
	while j < n:
		if i == -1 or text[j] == pattern[i]:
			#移向下一个字符
			j = j+1
			i = i+1
			str_count = str_count + 1
			if str_count == m:#字符串查找成功
				sum += 1
				des.append(j-i)#匹配成功的字符串起始下标
				str_count = 0#已匹配字符数清零
				i = 0#指向pattern游标清零
		else:
			i = pnext[i]#不匹配，考虑pnext决定的下一个字符
	
	if des:
		print '次数',sum
		return des 
	else:
		return -1

if __name__ == '__main__':
	# print gen_pnext('abcaabcba')
	# print len('abcaabcba')
	print matching_KMP('gabcaabcbaabcaabcba','abcaabcba')

