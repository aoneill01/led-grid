from flask import Flask, request
from multiprocessing import Process, Queue
from mspacman import ms_pacman
from off import off
from rainbow import rainbow
from text import text

app = Flask(__name__)
queue = Queue()

@app.route('/set', methods=['GET', 'POST'])
def test():
    mode = request.args.get('mode')
    args = request.args.getlist('args')
    if mode != None:
        queue.put('done')
        queue.put(mode)
        for arg in args: queue.put(arg)
    return 'ok'

def get_mode_function(id):
    mode_map = {
        'mspacman': ms_pacman,
        'off': off,
        'rainbow': rainbow,
        'text': text,
    }
    return mode_map[id]

def mode_loop(shared_queue):
    while True:
        message = shared_queue.get()
        print(message)
        function = get_mode_function(message)
        function(shared_queue)

if __name__ == '__main__':
    p = Process(target=mode_loop, args=(queue,))
    p.start()
    queue.put('off')
    app.debug = True
    app.run(host='0.0.0.0')

