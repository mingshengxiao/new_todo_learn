# -*- coding:utf-8 -*-
import threading

'''
使用线程，可以在一个进程中，同时进行多个操作。
'''

def worker(n):
	print('worker' + str(n))
	print(threading.current_thread().getName())

threads = []
for i in range(3):
	t = threading.Thread(target=worker, args = (i,))
	t.start()


class A(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
		args=(),kwargs=None,daemon=None):
		super().__init__(group=group, target=target, name=name,daemon=daemon)
		self.args = args
		self.kwargs = kwargs

	def run(self):
		print('running args: {!r} kwargs: {!r}'.format(self.args, self.kwargs))

for i in range(3):
	t = A(args=(i,), kwargs={'foo': 'bar'})
	t.start()

