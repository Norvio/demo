import logging, os, signal, time
from prometheus_client import Counter, Gauge, start_http_server

logging.basicConfig(level=logging.INFO)
TICKS = Counter("worker_loop_iterations_total", "Worker loop iterations")
UP = Gauge("worker_up", "1 while the worker loop is running")
running = True

def stop(*_):
    global running
    running = False

signal.signal(signal.SIGTERM, stop)

def main():
    start_http_server(int(os.environ.get("METRICS_PORT", "9000")))
    interval = float(os.environ.get("INTERVAL_SECONDS", "10"))
    UP.set(1)
    while running:
        TICKS.inc()
        logging.info("tick")
        time.sleep(interval)
    UP.set(0)
    logging.info("shutting down cleanly")

if __name__ == "__main__":
    main()