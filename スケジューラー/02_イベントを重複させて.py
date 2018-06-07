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

def long_event(name):
    print("BEGIN_EVENT:",time.time(),name)
    time.sleep(10)
    print("FINISH_EVENT:",time.time(),name)

print("START:",time.time())
scheduler.enter(2,1,long_event,("first",))
scheduler.enter(3,1,long_event,("second",))

scheduler.run()
