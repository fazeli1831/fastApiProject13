import multiprocessing
from fastapi import FastAPI

app = FastAPI()

class MyProcess(multiprocessing.Process):
    def run(self):
        print('Execution run process %s' % self.name)

@app.get("/start_processes/{num_processes}")
async def start_processes(num_processes: int):
    processes = []

    # ایجاد و راه‌اندازی پردازه‌ها
    for i in range(num_processes):
        process = MyProcess()
        processes.append(process)
        process.start()

    # انتظار برای اتمام همه پردازه‌ها
    for process in processes:
        process.join()

    return {"message": f"Started and completed {num_processes} processes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
