"""
イベントを遅滞なく実行
enter()で4つの引数を引き取る
・遅延を表す値
・優先順位の値
・呼び出す関数
・関数の引数のタプる
"""
import sched
import time

scheduler = sched.scheduler(time.time,time.sleep)

def print_event(name):
    print("EVENT:",time.time(),name)

print("START:",time.time())
scheduler.enter(2,1,print_event,("first",))
scheduler.enter(30,1,print_event,("second",))

scheduler.run()
