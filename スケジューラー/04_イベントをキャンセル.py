import sched
import threading
import time

scheduler = sched.scheduler(time.time,time.sleep)

# スレッドが変更できるグローバル変数をセット
counter = 0

def increment_counter(name):
    global counter
    print("EVENT:",time.time(),name)
    counter +=1
    print("NOW:",counter)

print("START:",time.time())
e1 = scheduler.enter(2,1,increment_counter,("E1",))
e2 = scheduler.enter(3,1,increment_counter,("E2",))

# イベントを実行するスレッドを開始
t = threading.Thread(target=scheduler.run)
t.start()

# メインスレッドに戻り、最初のイベントをキャンセル
scheduler.cancel(e1)

# スケジューラのスレッドの実行が終わるまで待つ
t.join()

print("FINAL:",counter)
